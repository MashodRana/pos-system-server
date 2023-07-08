
# POS System Server

This repository contains the backend code of Point of Sale(POS) System.

Tech Stack

- Django
- DRF
- Sqlite(initially)

## How to run your local machine

Go to the project root directory

    cd pos-system-server

#### 1. Create virtual environment with python 3 and activate your virtual environment and install required packages.

To install required packages run the following command 

    pip install -r requirements.txt 

#### 2. Run the following commands for the database  

    python manage.py makemigrations 
    ptyhon manage.py migrate

#### 3. Run project with following command 

    python manage.py runserver
