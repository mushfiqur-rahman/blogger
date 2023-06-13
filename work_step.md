### _Folder Structure_

## blogger
---
 
- venv
- manage.py
- core
    - setting
        - base.py (base settings)
        - local.py
        - production.py
    
        
2. To run project 

```python
$ (venv) PS blogger>> manage.py runserver
```        


3. Added condition to manage.py for DEBUG true or false condition

4. Secret key generate command

```python
 $ .\manage.py shell
 ```
 ```python
 >>> from django.core.management.utils import get_random_secret_key
 ```
 ```python
 >>> print(get_random_secret_key())
 ```
 ```python
 >>> exit()
 ```
5. Install [python-dotenv](https://pypi.org/project/python-dotenv/)

6. Create .env within the project directory. File stracture 

blogger
> core
    > .env    
   
and put the code

```python
SECRET_KEY = 

DEBUG = True
``` 

7. Add below line into the base.py file
```python
from dotenv import load_dotenv
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG') == 'True'
```
8. install [pytest-django](https://pytest-django.readthedocs.io/en/latest/) and create a file at root directory as name 
```bash
pytest.ini
```
9. To run test use below command
```bash
pytest
```
10. Create a new app 

```python
 $ (venv) PS D:blogger> ./manage.py startapp blog
```

11. install pip pytest cov

```bash
pytest --cov
```
12. 
```bash
 pytest --cov-report html --cov=./
 ```