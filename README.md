# Chitara

The Chitara project is a AI-powered song generation created by Django-based application that provides a backend for managing users, libraries, and songs. It includes features such as user authentication, song generation limits, and CRUD operations for the main domain models.

# prerequisites
- Python 3.8+

## Setup
1. Create virtual environment & Install Django
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    python -m pip install Django
```
2. Run migrations:
```bash
   python manage.py migrate
```
3. Run server:
```bash
   python manage.py runserver
```
open server at http://127.0.0.1:8000/

4. (Optional) Create a superuser:
```bash
   python manage.py createsuperuser
```

## Features
- User, Library, Song domain models
- Enum-based attributes
- CRUD via Django Admin

## Demo CRUD video
![CRUD Demo](./demo.mp4)