import peewee
from model import Users

db = peewee.SqliteDatabase("user_data.db")

if __name__ == "__main__":
    try:
        db.connect(reuse_if_open=True)
        models = [Users]
        db.create_tables(models)
        db.close()
    except peewee.OperationalError as error:
        print(error)