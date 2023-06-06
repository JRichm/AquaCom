""" ### Models for commission  ### """

from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


## user model
class User(db.Model):
    __tablename__ = "users"
    
    user_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    user_status = db.Column(db.Integer(), nullable=False)
    
    def __repr__(self):
        return f"<{self.username}#{self.user_id} LS{self.user_status}>"


## pending commission model
class Commission(db.Model):
    __tablename__ = "commissions"
    
    comm_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"), nullable=False)
    description = db.Column(db.String())
    num_characters = db.Column(db.Integer(), nullable=False)
    level_of_detail = db.Column(db.Integer(), nullable=False)
    request_date = db.Column(db.DateTime(), nullable=False)
    confirm_date = db.Column(db.DateTime(), nullable=True)
    price_estimate = db.Column(db.Numeric())
    price_charged = db.Column(db.Numeric())
    
    user = db.relationship("User", backref='commissions')
    
    def __repr__(self):
        return f"<{self.user}>"


## image model


""" ### Database Config ### """

def connect_to_db(flask_app, db_uri="postgresql:///AquaCom", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

