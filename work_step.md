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
    
        
* To run project 

```python
$ (venv) PS blogger>> manage.py runserver
```        


* Added condition to manage.py for DEBUG true or false condition

* Secret key generate command

```shell
 $ .\manage.py shell
 ```
 ```shell
 >>> from django.djblog.management.utils import get_random_secret_key
 ```
 ```shell
>>> print(get_random_secret_key())
 ```
 ```shell
 >>> exit()
 ```
* Install [python-dotenv](https://pypi.org/project/python-dotenv/)

* Create .env within the project directory. File stracture 

blogger
> core
    > .env    
   
and put the code

```python
SECRET_KEY =SECRET_KEY

DEBUG = True
``` 

* Add below line into the base.py file
```python
from dotenv import load_dotenv
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG') == 'True'
```
* install [pytest-django](https://pytest-django.readthedocs.io/en/latest/) and create a file at root directory as name 
```bash script
pytest.ini
```
* To run test use below command
```bash script
pytest
```
* Create a new app 

```python script
 $ (venv) PS D:blogger> ./manage.py startapp blog
```

* install pip pytest cov

```bash script
pytest --cov
```
```shell
 pytest --cov-report html --cov=./
 ```
* After configure Factory boy

```shell
(venv) PS D:\PROJECT\djblogger> py manage.py shell
```
```shell
>>> from blog.factory import PostFactory
```
```shell
>>> x = PostFactory.create_batch(200)
```
```shell
>>> exit()
```
