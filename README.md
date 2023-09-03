# Guess the Capital

1. Start with creating a virtual environment, run-
`python -m venv <env name>`
and activate it.

2. Clone this repository in the folder where your venv is located.
And move into it with `cd <repository-name>`

4. Install rhe dependencies-
`pip install -r requirements.txt`

5. Create an .env file in the 'capital' folder and add these parameters-
`SECRET_KEY=<Your secret key>
DEBUG=True
DATA_API=https://countriesnow.space/api/v0.1/countries/capital`

Create your own secret key using-

1. #from django.core.management.utils import get_random_secret_key
2. #print(get_random_secret_key())


5. Make migrations, run-
`python manage.py makemigrations`
`python manage.py migrate`

6. Run `python manage.py populate_coutries_table` in the terminal to populate the db.

7. Now, run `python manage.py runserver`, your api is up and running on the local server.
