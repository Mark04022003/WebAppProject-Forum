
## Project Setup

This guide outlines the steps to set up and run the Django forum application, including Python environment setup, Django project dependencies, database integration via MySQL dump, and email verification configuration.

## Prerequisites

* Python 3.12.x (Download from [python.org](https://www.python.org/downloads/))
* MySQL Server & MySQL Workbench ([Download here](https://dev.mysql.com/downloads/workbench/))

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd <repository_name>
```

### Step 2: Setup Python Virtual Environment

Create and activate a virtual environment to isolate project dependencies:

```bash
python -m venv venv

# On Windows
.\venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate
```

### Step 3: Install Dependencies

Install required Python packages via pip:

```bash
pip install -r requirements.txt
```

Make sure your `requirements.txt` contains at least:

```
Django==5.2.1
mysqlclient
```

### Step 4: Configure the Database

1. Open MySQL Workbench and create a new database.
2. Import the provided MySQL dump (`database_dump.sql`):

   * Open MySQL Workbench
   * Select your database
   * Click on `Server > Data Import`
   * Choose your dump file (`database_dump.sql`)
   * Execute the import

### Step 5: Configure Django Settings

Edit your Django project settings (`settings.py`) to connect to your MySQL database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your_database_name>',
        'USER': '<your_mysql_username>',
        'PASSWORD': '<your_mysql_password>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Step 6: Apply Migrations

```bash
python manage.py migrate
```

### Step 7: Configure Email Verification

To send email verification messages to your terminal (useful for development), update your settings as follows:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Step 8: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Your application should now be running at `http://127.0.0.1:8000/`

## Additional Notes

* Make sure MySQL Server is running during application startup.
* For production deployment, configure a real email backend and consider secure hosting solutions.
* 127.0.0.1:8000/admin should be opened in a cognito-mode browser window
