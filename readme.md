Python +3.9

## Generar migraciones


Cuando se esten gerando migraciones en la base de datos se deben de editar los siguientes archivos

api\manage.py
    - descomentar
        # INSTALLED_APPS=[
        #     "db",
        # ],
    -  comentar
        INSTALLED_APPS=[
            "api.db",
        ],

api\db\models.py
    - descomentar
        from manage import init_django
    - Comentar
        from api.manage import init_django

cd api
python manage.py makemigrations db
python manage.py migrate db