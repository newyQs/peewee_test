from peewee import *

sqlite_db = SqliteDatabase('my_app.db', pragmas={'journal_mode': 'wal'})


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = sqlite_db


class User(BaseModel):
    username = TextField()
    # etc, etc
