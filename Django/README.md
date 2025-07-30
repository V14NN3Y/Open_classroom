# Merch Exchange

Merch Exchange is a Django-based web application that serves as a marketplace for music-related items. This project allows users to browse, create, and manage listings for various music merchandise.

## Project Structure

The project consists of the following main components:

- **listings/**: The main application that handles the core functionality of the marketplace.
  - **migrations/**: Contains migration files for managing database schema changes.
  - **static/**: Contains static files such as CSS styles.
    - **listings/**: Directory for listing-specific static files.
      - **styles.css**: CSS styles defining the visual appearance of the web application.
  - **templates/**: Contains HTML templates for rendering views.
    - **listings/**: Directory for listing-specific templates.
      - **base.html**: The base template providing the structure for other HTML templates.
      - **other_templates.html**: Additional HTML templates extending the base template.
  - **admin.py**: Registers models with the Django admin site for easy data management.
  - **apps.py**: Configuration for the listings application.
  - **models.py**: Defines the data models representing the structure of the database tables.
  - **tests.py**: Contains test cases to ensure functionality works as expected.
  - **views.py**: Handles requests and returns responses.

- **manage.py**: Command-line utility for interacting with the Django project (running the server, applying migrations, etc.).

- **merchex/**: The project directory containing configuration files.
  - **settings.py**: Configuration settings for the Django project.
  - **urls.py**: Defines URL routing for the application.
  - **wsgi.py**: Used for deploying the application with WSGI servers.
  - **asgi.py**: Used for deploying the application with ASGI servers.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd merchex
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.
- Use the navigation links to explore groups, listings, and other features.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.