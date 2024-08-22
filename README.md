Django Books

A Django-based web application that allows users to manage books. This project demonstrates how to build a simple CRUD (Create, Read, Update, Delete) application with Django.


Table of Contents

Features

Installation

Usage

Project Structure

Technologies Used

License

Contributing

Contact



Features

Add, view, update, and delete books.

Search books by title or author.

User authentication and registration.

Responsive design with Bootstrap.


Installation

Clone the repository:


git clone https://github.com/dangluva/django-books.git

cd django-books


Create and activate a virtual environment:


python -m venv venv

source venv/bin/activate  
# On Windows use `venv\Scripts\activate`

Install dependencies:


pip install -r requirements.txt

Set up environment variables:

Create a .env file in the root directory and add your environment variables, like SECRET_KEY and DEBUG.

Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Usage

Access the app at http://127.0.0.1:8000/.

Create an account, log in, and start managing books.

Project Structure


django_books/
│
├── WebBooks/# Main Django application
│   ├── settings.py         # Django settings file
│   ├── urls.py             # URL routing
│   ├── views.py            # Views for the application
│   └── ...
│
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, Images)
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies

Technologies Used

Django

Python

SQLite

Bootstrap

License

This project is licensed under the MIT License.

Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

Contact

GitHub: dangluva

Email: dangluva@gmail.com