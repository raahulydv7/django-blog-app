# 📝 Django Blog App

A simple Django-powered blog application where users can register, create blog posts, follow/unfollow users, and manage their own profiles.

## 🚀 Features

- User registration and login
- Create, edit, and delete blog posts
- User profile management
- Follow and unfollow users
- View posts from followed users on the home page
- Search users by username or full name
- Responsive UI with Bootstrap 4 and Font Awesome icons

## 🏗️ Project Structure
<pre>
blog_project/
    ├── blog_app/
    │   ├── templates/
    │   ├── static/
    │   ├── forms.py
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    ├──── blog_project/
    │   ├── settings.py
    │   ├── urls.py
    ├── manage.py
    ├── .env
    ├── requirements.txt

</pre>

<pre>

    ## ⚙️ Setup Instructions

    1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/django-blog-app.git
    cd django-blog-app

    2. Create Virtual Environment & Install Dependencies
        python -m venv env
        source env/bin/activate  # On Windows: env\Scripts\activate
        pip install -r requirements.txt

    3. Set Up .env File
        Create a .env file in the root with the following:

        ENGINE=postgresql
        NAME=db_name
        USER=your_db_user
        PASSWORD=your_db_password
        HOST=localhost
        PORT=5432

    4. Run Migrations

        python manage.py makemigrations
        python manage.py migrate

    5. Create Superuser (Admin)
        python manage.py runserver

    6. Run the Development Server
        python manage.py runserver

    7. Visit http://127.0.0.1:8000 to get started.

</pre>

<pre>
    🔐 Admin Panel
    Access the admin panel at /admin/ using your superuser credentials.
</pre>