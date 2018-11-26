import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-LogoHome",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    license='',
    description='A Django-Postgres-React app to display relevant logo printing and embroiding informations',
    long_description=README,
    url='https://www.example.com',
    author='Haitao',
    author_email='erichht71@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1.2',
        'Intended Audience :: Developers',
        'License :: ',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6.6',
        'Topic :: Internet :: WWW/HTTP',
        'TOpic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
)