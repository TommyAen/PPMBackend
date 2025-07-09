# Social App
A Django-based networking platform.
Users can create profiles, submit posts, comment and add friends.
Created as a Project for the course PPM at University of Florence.
## Features
- **User Registration and Authentication**: Users can sign up and log into the platform.

- **User Profiles**: Each user has a customizable profile with a bio and profile picture.

- **Friend Requests**: Users can send, accept, and reject friend requests.

- **Friends List**: Users can view their accepted friends.

## Installation
### Setting up the project
1. **Clone the repository**:
   ```shell
   git clone https://https://github.com/TommyAen/PPMBackend
   cd PPMBackend
   ```
2. **Create a virtual environment:**
    Use Python 3.13.5 (or a compatible version)
    ```shell
    python -m venv env
    source env/bin/activate #On Windows: env\Scripts\activate
    ```
   
3. **Install dependencies**:
    ```shell
   pip install -r requirements.txt
    ```
   
4. **Configure the database**
    Ensure the `db.sqlite3` file exists in the root directory, or it will be created after running migration
5. **Create a `.env` file the project root with the following content**:
    ```env
   SECRET_KEY= add_your_secret_key 
   ```
   
6. **Run migrations:**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
    ```
7. **Collect static files:**

   ```sh
   python manage.py collectstatic
    ```
8. **Run the development server:**

   ```sh
   python manage.py runserver
    ```
Project will be available at `http://127.0.0.1:8000/`.

## Deployment
The project is deployed on Railway and is available here: https://web-production-ebf1.up.railway.app/