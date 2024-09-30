# Financial Manager Project

## Project Overview

The **Financial Manager** is a comprehensive personal finance management application designed to help users keep track of their income, expenses, and savings. Utilizing **Flask** for backend operations, **HTML**, **CSS**, and **JavaScript** for the frontend, and **SQLite** for data management, this application offers a robust solution for managing personal finances. The goal is to provide users with a straightforward and efficient way to monitor their financial health and make informed decisions.

## File Descriptions and Functionality

### `/app/__init__.py`

This file initializes the Flask application and sets up essential components, including database connections via SQLAlchemy and localization with Flask-Babel. It imports `routes.py` and `models.py` to establish the application context. This central setup ensures all components work together cohesively.

### `/app/models.py`

Defines the database models using SQLAlchemy:
- **User Model**: Manages user credentials and profile information. Passwords are hashed for security.
- **Transaction Model**: Captures financial transactions categorized as income or expenses and links them to individual users.

The design emphasizes simplicity and scalability, providing a clear structure for managing user data and transactions. Future versions might introduce more detailed transaction categories based on user feedback.

### `/app/routes.py`

Handles routing for various application functionalities:
- **`/register` and /login`**: Manage user registration and login securely.
- **`/dashboard`**: Displays an overview of the user's financial data, including total income, expenses, and savings.
- **`/add_transaction` and /edit_transaction`**: Facilitate the addition and editing of transactions.

This separation of routes helps maintain clarity and flexibility in handling form submissions and data processing.

### `/app/templates/`

Contains HTML templates rendered by Flask using Jinja2:
- **`base.html`**: The primary layout template used by other templates for consistent design.
- **`dashboard.html`**: Provides a summary of financial data and options to add new transactions.
- **`login.html` and **`register.html`**: Forms for user authentication.
- **`add_transaction.html` and **`edit_transaction.html`**: Forms for managing transactions.
- **`index.html`**: The application’s landing page.
- **`overview.html`**: Shows account balances and financial summaries.

Using a base layout template ensures design consistency across pages and reduces redundancy.

### `/app/static/`

Holds static files such as CSS and JavaScript:
- **`styles.css`**: Manages the visual styling of the application.
- **`login.js`** and **`register.js`**: Handle dynamic features like password visibility toggling and form submission.

The design focuses on a clean, minimal interface to enhance user experience and mobile responsiveness.

### `config.py`

Contains configuration settings for the Flask application, including the secret key, database URI, and localization settings. Environment variables are used where applicable to enhance security and flexibility.

### `run.py`

The entry point for the application, which starts the Flask development server. This script is essential for local testing and development.

### `requirements.txt`

Lists all dependencies needed for the project, such as Flask, Flask-SQLAlchemy, and Flask-Babel. This file facilitates easy installation of necessary packages and ensures consistent environment setup.
