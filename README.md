# Kids-edu-game

A fun and educational game for kids, built with Django.

## Project Structure

- `backend/`: Contains the Django application logic, templates, and static files.
- `api/`: API endpoints for the game.
- `Frontend/`: HTML files for the game interface.
- `kids_edu_game/`: Project configuration (settings, URLs, etc.).

## Setup Instructions

### 1. Prerequisites
- Python 3.9+
- pip (Python package manager)

### 2. Environment Setup
Create a virtual environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Database Initialization
Run the migrations to set up the database:

```bash
python manage.py migrate
```

### 4. Running the Project
Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

## Features
- Interactive educational games for kids.
- Django-powered backend for data management.
- Responsive design.

## License
MIT License
