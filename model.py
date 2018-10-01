import peewee
from datetime import datetime

db = peewee.SqliteDatabase("user_data.db")

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Users(BaseModel):
    id = peewee.IntegerField(index=True, primary_key=True)
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    password = peewee.FixedCharField(max_length=30)
    created_date = peewee.DateTimeField(default=datetime.now)