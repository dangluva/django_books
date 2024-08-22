
# Django Books

A Django-based web application that allows users to manage books. This project demonstrates how to build a simple CRUD (Create, Read, Update, Delete) application with Django.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Add, view, update, and delete books.
- Search books by title or author.
- User authentication and registration.
- Responsive design with Bootstrap.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/dangluva/django-books.git
   cd django-books
   ```

2. **Create and activate a virtual environment**:

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the root directory and add your environment variables, like `SECRET_KEY` and `DEBUG`.

5. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

## Usage

- Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
- Create an account, log in, and start managing books.

## Project Structure

```plaintext
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
```

## Technologies Used

- Django
- Python
- SQLite
- Bootstrap

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## Contact

- **GitHub**: [dangluva](https://github.com/dangluva)
- **Email**: verslogalimybes1@gmail.com
