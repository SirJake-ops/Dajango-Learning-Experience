# Django Learning Experience 

## Overview
`Django Learning Experience` is a Django-based web application that provides user management functionalities, including user creation and authentication using JWT (JSON Web Tokens).

## Features
- User registration
- User login with JWT authentication
- Custom authentication backend using email

## Technologies Used
- Python
- Django
- Django REST Framework
- Django REST Framework SimpleJWT

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/didactic-enigma.git
    cd didactic-enigma
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

### API Endpoints

- **User Registration**: `POST /api/users/`
- **User Login**: `POST /api/token/`

### Custom Authentication Backend

The project uses a custom authentication backend (`EmailBackend`) to authenticate users using their email addresses.

## Project Structure

- `views.py`: Contains the views for user registration and login.
- `apps.py`: Configuration for the `application_user` app.
- `backends.py`: Custom authentication backend.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.# didactic-enigma
