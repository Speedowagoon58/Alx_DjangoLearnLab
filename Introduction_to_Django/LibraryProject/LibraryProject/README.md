# LibraryProject

Welcome to the LibraryProject! This project is a simple Django application designed to manage a library system.

## Features

- Add, update, and delete books
- Manage library members
- Track borrowed and returned books
- Search for books and members

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/LibraryProject.git
    ```
2. Navigate to the project directory:
    ```bash
    cd LibraryProject
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply the migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
8. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin` to manage books and members.
- Use the main application to search for books and manage borrowing/returning.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainer at your.email@example.com.
