========
LogoHome
========

LogoHome is a Django-Postgres-React app to display relative informations of Web-based logo printing and embroiding service.

Detailed documents are in the "docs" directory.

Quick Start
-----------

1. Add "LogoHome" to your INSTALLED_APPS setting like this::
    INSTALLED_APPS = [
        ...
        'LogoHome', 
    ]

2. Include the LogoHome URLconf in your project urls.py like this::
    path('LogoHome/', include('LogoHome.urls')),

3. Run `python3 manage.py migrate` to create the LogoHome models.

4. Start the development server and visit http://127.0.0.1/admin to create the logo printing relevant informations (you'll need the Admin app enabled).

5. Visit http://127.0.0.1/LogoHome to browse logo printing relevant informations.