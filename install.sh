python -m pip install -r requirements.txt
chmod +x launch.sh
cd HCapp
python manage.py makemigrations
python manage.py migrate
cd ..

