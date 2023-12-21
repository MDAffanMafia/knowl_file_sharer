# Django File Sharing Platform -  knowl_file_sharer

This is a simple Django-based file-sharing platform that allows users to upload files, share them with other users, and manage their files in a secure environment.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functionalities](#functionalities)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/MDAffanMafia/knowl_file_sharer.git
   cd knowl_file_sharer
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

Now you can access the project locally at 'http://localhost:8000'.

## Usage

1. Visit 'http://localhost:8000' in your web browser.
2. Sign up for a new account or log in if you already have one.
3. Upload files using the file upload form.
4. View and manage your uploaded files on the main dashboard.
5. Search for other users and share files with them.

## Functionalities

- **Sign Up:** Users can create a new account with a unique username and email.
- **Login:** Users can log in with their username and password.
- **File Upload:** Users can upload files to the platform.
- **File Sharing:** Users can share their files with other registered users.
- **File Management:** Users can view and manage their uploaded files.
- **Search Users:** Users can search for other users by email and share files with them.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.
6. Please adhere to the code style and formatting guidelines.

If you encounter any issues or have ideas for improvements, please open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
