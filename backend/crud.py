""" ### CRUD functions ### """

import model

""" #   CREATE   # """
def create_user(username, password, email):
    user = model.User(
        username=username,
        email=email,
        password=password
    )
    

""" #   READ   # """


""" #   UPDATE   # """


""" #   DELETE   # """


""" ### CRUD config ### """
if __name__ == "__main__":
    from server import app
    model.connect_to_db(app)