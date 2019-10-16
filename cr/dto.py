from peewee import *

db = SqliteDatabase('mail_service.db')


class Mails(Model):
    # Used to save email to databases to later use them
    text = CharField()
    mail_to = CharField()
    date = CharField()
    details = TextField

    class Meta:
        database = db
