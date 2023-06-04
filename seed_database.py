""" Script for seeding database """

import os

import crud
import model
from server import app

os.system("drop -U jamcam aquacom")
os.system("createdb -U jamcam aquacom")

with app.app_context():
    model.connect_to_db(app)
    model.db.create_all()
    

    
