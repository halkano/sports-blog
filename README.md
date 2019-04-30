# pitch rater
#### This is a platform for web developers where they will be able to post their projects to be rated by other users or developers, 15/03/2019.
#### By **henry halkano**
## Description
This application is a simplest web clone of a website called awards. A user can create an account and sign into it. The site supports uploading projects. User can see projects of other users on the home page. user can also rate them or goto the site to experience it.
## Specifications
### User
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Register new account | Fill in the registration form in the home page | Sends activation link to the registration email. The link should be clicked to activate the account |
| Login | Fill in the login form with correct username and password | Redirects the user to the homepage of the user |
| Edit Bio | Click on the edit profile button in the homepage. Upload picture, and fill in the username and password | Redirects the user to the profile with changes made to profile |
| Rate a project | Click on the rate tab to view the project and its details. Rate the app in the rates field | Refreshed the page and reflects the changes |

## Setup/Installation Requirements
- Python 3.6
- Django Framework
- HTML, CSS, JavaScript and Bootstrap
- PostgreSQL
- python virtual environment
## Running the Application
   * To run the application, in your terminal:
   1. Clone or download the Repository
       2. Create a virtual environment
       3. Read the requirements file and Install all the requirements. Or run pip3 install -r requirements.txt to automatically install all the requirements
       4. Prepare environment variables
       -export DATABASE_URL='postgresql+psycopg2://username:password@localhost/blog'
       -export SECRET_KEY='Your secret key',etc
       5. Run initial migration
       python3.6 manage.py makemigrations rater
       python3.6 manage.py migrate
       6. Run the application
       python3.6 manage.py runserver
       7. Access the application through `localhost:8000`
