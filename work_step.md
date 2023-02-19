# Folder Structure

blogger

 
- venv
- manage.py
- core
    - setting
        - base.py (base settings)
        - local.py
        - production.py
    
        
2. To run project 

```
$ (venv) PS blogger>> manage.py runserver
```        


3. Added condition to manage.py for DEBUG true or false condition

4. Secret key generate command

```
 $ .\manage.py shell
 ```
 ```
 >>> from django.core.management.utils import get_random_secret_key
 ```
 ```
 >>> print(get_random_secret_key())
 ```
 ```
 >>> exit()
 ```
5. Install [python-dotenv](https://pypi.org/project/python-dotenv/)

6. Create .env within the project directory. File stracture 

blogger
> core
    > .env    
   
and put the code

```
SECRET_KEY = 

DEBUG = True
``` 

7. Add below line into the base.py file
```
from dotenv import load_dotenv
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG') == 'True'
```
8. install [pytest-django](https://pytest-django.readthedocs.io/en/latest/) and create a file at root directory as name 
```
pytest.ini
```
9. To run test use below command
```
pytest
```
10. Create a new app 

```
 $ (venv) PS D:blogger> ./manage.py startapp blog
```