""" Script for seeding database """

import os

import crud
import model
from server import app


# delete db to start fresh
os.system("dropdb -U jamcam aquacom")
os.system("createdb -U jamcam aquacom")

# create tables from model.py
with app.app_context():
    model.connect_to_db(app)
    model.db.create_all()