import click
from models.baseModel import db
from app import app

from models import *


@app.cli.command()
def initdb():
    db.drop_all()
    db.create_all()
    user = User(user_name='admin', user_pwd='admin', role='admin',create_user='sys')
    db.session.add(user)
    db.session.commit()
    click.echo('Init Finished!')
