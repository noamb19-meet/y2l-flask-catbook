
from flask import Flask, render_template, request,redirect,url_for
from flask import Flask
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def catbook_home():
	if request.method == 'GET':
		cat = get_all_cats()
		return render_template("home.html", cats=cat)

@app.route('/cats/<int:id>')
def catbook_profile(id):
	cat = get_cat_by_id(id)
	return render_template("cat.html", cat=cat)

@app.route('/new_cat',methods=['GET','POST'])
def new_cat():
	if request.method == 'POST':
		name = request.form['cat_name']
		cat_added = create_cat(name)
		cat=get_all_cats()
		return render_template("home.html",cats=cat)
	else:
		return render_template("new_cat.html")

@app.route('/vote/<int:id>',methods=['GET','POST'])
def vote_cat(id):
	vote(id)
	return redirect(url_for('catbook_home'))






if __name__ == '__main__':
	app.run(debug = True)
