Django Books
A Django-based web application that allows users to manage books. This project demonstrates how to build a simple CRUD (Create, Read, Update, Delete) application with Django.
Table of Contents
•	Features
•	Installation
•	Usage
•	Project Structure
•	Technologies Used
•	License
•	Contributing
•	Contact
Features
•	Add, view, update, and delete books.
•	Search books by title or author.
•	User authentication and registration.
•	Responsive design with Bootstrap.
Installation
1.	Clone the repository:
git clone https://github.com/dangluva/django-books.git
cd django-books
2.	Create a virtual environment:
python -m venv venv

3.	Activate the virtual environment:
On Windows:
venv\Scripts\activate

On MacOS/Linux:
source venv/bin/activate

4.	Install dependencies:
pip install -r requirements.txt

5.	Set up environment variables:
Create a .env file in the root directory and add the following (adjust accordingly):
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

6.	Apply migrations:
python manage.py migrate

7.	Create a superuser (optional):
python manage.py createsuperuser

8.	Run the development server:
python manage.py runserver

9.	Access the application:
Open your browser and go to http://127.0.0.1:8000/.

Usage
1.	Register or log in as a user.
2.	Add books to the collection.
3.	Search, update, or delete books.
4.	Admin users can manage all users and books from the admin panel.
Project Structure
django_books/
│
├── WebBooks/               # Main Django application
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
•	Django - Python web framework
•	SQLite - Default Django database (for development)
•	Bootstrap - Front-end styling
•	django-environ - Managing environment variables
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or fixes.
Contact
If you have any questions or feedback, feel free to reach out:
•	GitHub: dangluva
•	Email: dangluva@gmail.com

