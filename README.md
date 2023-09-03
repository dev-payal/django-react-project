# Guess the Capital

## Getting Started

1. **Create a Virtual Environment**: Start by creating a virtual environment. Run the following command, replacing `<env name>` with your desired environment name, and activate it.

   python -m venv <env name>
   source <env name>/bin/activate  

2. **Clone the Repository**: Clone this repository into the folder where your virtual environment is located. Move into the repository folder.
`git clone <repository-url>`
`cd <repository-name>`
Install Dependencies: Install project dependencies using pip by running the following command:
`pip install -r requirements.txt`

3. **Create an .env File**: Create an .env file in the 'capital' folder and add the following parameters:
`SECRET_KEY=<Your secret key>
DEBUG=True
DATA_API=https://countriesnow.space/api/v0.1/countries/capital`

4. **Generate Your Own Secret Key**: To generate your own secret key, you can use the following code. Replace the SECRET_KEY value in your .env file with the generated key.
# Uncomment these lines and run them in a Python environment to generate a secret key
# from django.core.management.utils import get_random_secret_key
# print(get_random_secret_key())

5. **Apply Migrations**: Create database tables by making migrations and then applying them.
`python manage.py makemigrations
python manage.py migrate`

6. **Populate Countries Table**: Populate the database with country data by running the following command:
`python manage.py populate_countries_table`

7. **Run the Server**: Start the local server.
python manage.py runserver
Your API is now up and running on the local server.
