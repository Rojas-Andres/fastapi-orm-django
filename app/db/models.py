from bujango.db import models

from app.manage import init_django

# from manage import init_django


init_django()


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
