""" ### Server File ### """

from jinja2 import StrictUndefined
from model import connect_to_db
from flask import (
    Flask,
    render_template,
    flash,
    session,
    request,
    redirect,
    url_for,
    send_from_directory,
)

app = Flask(__name__)
app.secret_key = "aqua"
app.jinja_env.undefined = StrictUndefined


""" ### Server Routes ### """

# index
@app.route('/')
def index():
    return render_template("index.html")


""" ### Server Config ### """

#favicon
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, "favicon.png")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)