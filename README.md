# CS253_StarBugs
This is the repository containing all the sourcecodes for Health++, the Health Centre Automation Website.
---
## Launching the Website

### Dependencies

```
python -m pip install -r requirements.txt
```

### Installing the required files

- In the required directory clone the repository
```
git clone  git@github.com:atulyasndrm/CS253_StarBugs.git
```

### Running the App

- Go to the directory from the directory you cloned the repository in 
```
cd CS253_Starbugs/HCApp
```

- Now, run the following code to make the required databases and tables
```
python manage.py makemigrations
python manage.py migrate
```

- Finally,
```
python manage.py runserver
```

- Now type the following IP address in your preffered web browser
```
http://127.0.0.1:8000/
```
