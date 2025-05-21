import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the current directory to the path to ensure imports work correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Determine which framework to use based on environment variable
FRAMEWORK = os.getenv("FRAMEWORK", "nicegui").lower()

if FRAMEWORK == "nicegui":
    from app.frontend.nicegui_app import ui, app
    application = app
else:
    from app.main import app
    application = app

# This is used by ASGI servers like Uvicorn
app = application

if __name__ == "__main__":
    if FRAMEWORK == "nicegui":
        ui.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
    else:
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)