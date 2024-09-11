# Google_Integration_Portal


 # Project Overview

 This project aims to develop a centralized web application that allows business users to efficiently manage and respond to customer reviews on their business accounts. The application uses a dummy API to simulate review data and provides a user-friendly interface for replying to customer feedback.

# Key Features

**Dummy API for Reviews:** Simulated review data for development purposes.

**Authentication and Security:** Implements user authentication using Django Allauth and customized the login page for enhanced user experience and security.

**Responsive UI Design:** Ensures the application is fully responsive and works seamlessly across different devices.

# Technical Stack

**Frontend:** HTML, CSS, JavaScript

**Backend:** Django, Django Allauth

**Framework:** Bootstrap, REST framework

**Database:** SQLite

# Prerequisites
* Python 3.x
* Django 3.x or higher
* pip (Python package installer)
* Virtualenv (optional but recommended)

# Installation
   
  Follow these steps to set up the project locally:

1. Clone the repository

   git clone "repository-url"

   cd "repository-directory"

3. Create and activate a virtual Environment (optional but recommended):

     python -m venv venv
   
     **(On Windows use)** venv\Scripts\activate

3. Install Dependencies:
   
   pip install -r requirements.txt

5. Run Migrations:
   
   python manage.py makemigrations
   
   python manage.py migrate

7. Create a Superuser:
   
   python manage.py createsuperuser

9. Run the Development Server:
    
   python manage.py runserver

Access the Application: Open your web browser and go to http://127.0.0.1:8000/ to access the application.

# Usage
1. Login: Use the superuser credentials to log in to the application.
2. Register Business Details: Upon first login, you will be prompted to enter your business details.
3. Add Reviews via Admin Panel:
  * Navigate to the Django admin panel at http://127.0.0.1:8000/admin/.
  *  Log in with your superuser credentials.
  *  Add reviews to your business profile through the admin interface.
4. Manage Reviews: Access the “My Business” section to view and respond to customer reviews.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.
