Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Python dateutil : 

from datetime import *
from dateutil.relativedelta import *
now = datetime.now()

Six :

for item in dictionary.items():
    #do something

Requests:

import requests
r = requests.get(‘https://api.spotify.com/’)
r.status_code

Setuptools : 

from setuptools import setup
setup(name=‘package_name’,
version=‘0.1’,
description=‘an example of a package’,
url=‘http://github.com/user/example_package’,
author=‘Dante’,
author_email=‘dante@example.com’,
license=‘MIT’,
packages=[‘example’],
zip_safe=False)

Pytest: 

def inc(x):
    return x + 1
def >test_answer():
    assert inc(3) == 5