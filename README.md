# Django Text Analysis Web App

This is a simple Django web application that allows users to input a URL, stores it in a database, can perform some action on the URL , and will return an analyzed text.

## Getting Started

### Prerequisites

- Python
- Django

### Installation

1. Clone the repository:

```
   bash
   git clone https://github.com/yourusername/django-text-analysis.git
   cd django-text-analysis
```

2. Set up django project

```
    pipenv install django
    pipenv shell
    - Change interpreter to current venv
```

3. Apply database migrations

```
    python3 manage.py makemigrations
    python3 manage.py migrate
```

4. Run server locally

```
    python3 manage.py runserver
```

### Usage

After running the server, the initial page will be the index view. The input view will be 'localhost/input'
