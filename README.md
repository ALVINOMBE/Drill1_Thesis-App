# Thesis Blog

A Django-based web application for managing and displaying thesis papers, with pagination and a comment system. Users can perform basic CRUD operations on thesis papers.

## Features

- Display thesis papers with title, author, description, date, and status (draft or published).
- Pagination for the thesis list.
- Add and display comments for each thesis.
- Basic CRUD operations for thesis papers.

## Requirements

- Python 3.x
- Django 3.x or later

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/thesis_blog.git
   cd thesis_blog
   
2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3.Install dependencies:
pip install -r requirements.txt

4.Apply migrations:
python manage.py makemigrations
python manage.py migrate

5. Create a superuser:
python manage.py createsuperuser

6.Run the development server:
python manage.py runserver

7. Access the application:
Open your web browser and go to http://127.0.0.1:8000/
