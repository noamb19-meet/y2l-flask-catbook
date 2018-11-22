

from flask import Flask
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
	if request.method = get
	cats = get_all_cats()
	return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def catbook_profile(id):
	cat = get_cat_by_id(id)
	return render_template("cat.html", cat=cat)

@app.route('/new_cat')
def new_cat():
	return render_template("new_cat.html")







if __name__ == '__main__':
   app.run(debug = True)
