Python +3.9

## Generar migraciones


Cuando se esten gerando migraciones en la base de datos se deben de editar los siguientes archivos

- api\manage.py
    - descomentar
        # INSTALLED_APPS=[
        #     "db",
        # ],
    - comentar
        INSTALLED_APPS=[
            "api.db",
        ],

- api\db\models.py
    - descomentar
        from manage import init_django
    - Comentar
        from api.manage import init_django

cd api
python manage.py makemigrations db
python manage.py migrate db


# Docker
docker build -t fastapi-orm-django .
docker run -p 8000:8000 fastapi-orm-django

# Docker-compose


docker build -t fastapi-orm-django-docker .
docker-compose -t fastapi-orm-django-docker up --force-recreate --build
### Run migrations docker-compose
- docker-compose run fast-api python ./app/migrate.py
