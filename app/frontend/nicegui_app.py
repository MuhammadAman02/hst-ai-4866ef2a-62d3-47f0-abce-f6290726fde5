from nicegui import ui, app
from fastapi import FastAPI
from app.core.config import settings

# Initialize FastAPI app
fast_app = FastAPI()
app.include(fast_app)

# Portfolio data
portfolio_data = {
    "name": "Alex Johnson",
    "title": "AI Engineer specializing in LLMs",
    "about": "Passionate AI engineer with 5+ years of experience in developing and deploying large language models. Expertise in natural language processing, transformer architectures, and scalable AI systems.",
    "skills": ["PyTorch", "TensorFlow", "Hugging Face Transformers", "BERT", "GPT", "T5", "RAG", "Fine-tuning LLMs", "Prompt Engineering", "MLOps"],
    "projects": [
        {
            "title": "Multilingual Customer Support Chatbot",
            "description": "Developed a BERT-based chatbot capable of handling customer queries in 10 languages, improving response times by 40%.",
        },
        {
            "title": "AI-powered Content Summarization Tool",
            "description": "Created a T5-based summarization tool that generates concise summaries of long-form content, increasing user engagement by 25%.",
        },
        {
            "title": "Sentiment Analysis for Social Media Monitoring",
            "description": "Implemented a RoBERTa-based sentiment analysis model for real-time social media monitoring, achieving 92% accuracy.",
        },
    ],
    "contact": {
        "email": "alex.johnson@example.com",
        "linkedin": "https://www.linkedin.com/in/alexjohnson",
        "github": "https://github.com/alexjohnson",
    }
}

@ui.page('/')
def portfolio():
    with ui.column().classes('w-full max-w-3xl mx-auto p-4'):
        ui.markdown(f"# {portfolio_data['name']}").classes('text-3xl font-bold mb-2')
        ui.markdown(f"## {portfolio_data['title']}").classes('text-xl text-gray-600 mb-4')
        
        with ui.card().classes('w-full mb-4'):
            ui.markdown("## About Me").classes('text-2xl font-bold mb-2')
            ui.markdown(portfolio_data['about'])
        
        with ui.card().classes('w-full mb-4'):
            ui.markdown("## Skills").classes('text-2xl font-bold mb-2')
            with ui.row().classes('flex flex-wrap'):
                for skill in portfolio_data['skills']:
                    ui.badge(skill).classes('m-1')
        
        with ui.card().classes('w-full mb-4'):
            ui.markdown("## Projects").classes('text-2xl font-bold mb-2')
            for project in portfolio_data['projects']:
                with ui.card().classes('w-full mb-2'):
                    ui.markdown(f"### {project['title']}").classes('text-xl font-bold')
                    ui.markdown(project['description'])
        
        with ui.card().classes('w-full'):
            ui.markdown("## Contact").classes('text-2xl font-bold mb-2')
            ui.markdown(f"Email: {portfolio_data['contact']['email']}")
            ui.link("LinkedIn", portfolio_data['contact']['linkedin']).classes('block')
            ui.link("GitHub", portfolio_data['contact']['github']).classes('block')

# API endpoint for portfolio data
@app.get('/api/portfolio')
def get_portfolio_data():
    return portfolio_data

# Dark mode toggle
@ui.page('/')
def dark_mode_toggle():
    dark = ui.dark_mode()
    ui.button('Toggle Dark Mode', on_click=dark.toggle).classes('fixed top-2 right-2')

# Run the app
ui.run(title=settings.APP_NAME)