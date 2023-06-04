""" Script for seeding database """

import os

import crud
import model
from server import app

os.system("dropdb -U jamcam aquacom")
os.system("createdb -U jamcam aquacom")

aqua = crud.create_user()

with app.app_context():
    model.connect_to_db(app)
    model.db.create_all()