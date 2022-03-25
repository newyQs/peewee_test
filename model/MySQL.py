from peewee import *

mysql_db = MySQLDatabase('my_database')


class BaseModel(Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = mysql_db


class User(BaseModel):
    username = CharField()
    # etc, etc
