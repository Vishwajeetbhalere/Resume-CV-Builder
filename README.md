# Resume-CV-Builder

Resume-CV-Builder is a web application designed to help users create, manage, and export professional resumes/CVs. Built using Django, AJAX, HTML, CSS, and jQuery, this application offers a seamless experience for users to handle all aspects of their resume, from creation to exportation. 

## Features

### User Authentication
- **Login and Registration**: Users can create an account and log in to access their personal dashboard.
- **Authentication**: Ensures secure access to user-specific data and functionalities.

### Resume Management
- **CRUD Operations**: Users can Create, Read, Update, and Delete sections of their resume. This includes adding new sections, updating existing information, and removing unnecessary sections.
- **Dynamic Updates**: Changes made to the resume are dynamically updated without requiring a page refresh, thanks to AJAX and jQuery.

### Export to PDF
- **PDF Export**: Users can export their resume/CV to a PDF format with a single click. The exported PDF is formatted to be professional and ready for job applications.

### Object-Relational Mapping (ORM)
- **Django ORM**: Utilizes Django's powerful ORM to manage database interactions seamlessly. This ensures efficient data retrieval and manipulation while abstracting complex SQL queries.

### User-Friendly Interface
- **Responsive Design**: The application is designed to be responsive, ensuring a smooth experience on both desktop and mobile devices.
- **Intuitive UI**: Easy-to-use interface for managing resume sections and content, making it accessible for users with varying levels of technical expertise.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, jQuery
- **AJAX**: For asynchronous data updates and dynamic user interactions
- **PDF Generation**: Utilizes libraries to convert resume content into a downloadable PDF format
- **ORM**: Django ORM for efficient database management
- **Database**: SQLite for storing user data and resume details

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.7.16
- Django  5.0.6
- Other dependencies as listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Vishwajeetbhalere/Resume-CV-Builder.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Resume-CV-Builder
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser to access the admin interface:
   ```sh
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

### Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. Register a new account or log in with existing credentials.
3. Start creating your resume by adding sections and filling in the details.
4. Update or delete sections as needed.
5. Export your resume to a PDF when you are satisfied with the content.

## Contributing

We welcome contributions! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Acknowledgements

- Thanks to the Django community for providing extensive documentation and support.

