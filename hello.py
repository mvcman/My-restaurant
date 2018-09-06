from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import Column, ForeignKey, Integer, String, true, false
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base, Restaurant, MenuItems
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

app=Flask(__name__)
@app.route('/')
@app.route('/hello')
def hellomandy():
	return '<h1>Welcome to my restaurant!</h1>'
@app.route('/hello/<int:resto_id>/')
def hello(resto_id):
	restaurant = session.query(Restaurant).filter_by(id = resto_id).one()
	items = session.query(MenuItems).filter_by(restaurant_id = restaurant.id)
	return render_template('menu.html',restaurant = restaurant, items = items)


@app.route('/hello/<int:resto_id>/new/', methods=['GET','POST'])
def newMenuItem(resto_id):
	if request.method == 'POST':
		newItem = MenuItems(name=request.form['name'], description = request.form['description'], price =request.form['price'], restaurant_id = resto_id)
		session.add(newItem)
		session.commit()
		flash("new menu item created!")
		return redirect(url_for('hello', resto_id = resto_id))
	else:
		return render_template('newmenuitem.html', restaurant_id = resto_id)


@app.route('/hello/<int:resto_id>/<int:menu_id>/edit/', methods = ['GET','POST'])
def editMenuItem(resto_id,menu_id):
	editedItem = session.query(MenuItems).filter_by(id = menu_id).one()
	if request.method == 'POST':
		if request.form['edit_name']:
			editedItem.name = request.form['edit_name']
		session.add(editedItem)
		session.commit()
		flash("new menu item Edited!")
		return redirect(url_for('hello', resto_id = resto_id))
	else:
		return render_template('edititem.html', restaurant_id = resto_id, menu_id = menu_id, item = editedItem)


@app.route('/hello/<int:resto_id>/<int:menu_id>/delete/',methods = ['GET','POST'])
def deleteMenuItem(resto_id,menu_id):
	itemToDelete = session.query(MenuItems).filter_by(id = menu_id).one()
	if request.method == 'POST':
		session.delete(itemToDelete)
		session.commit()
		flash("new menu item Deleted!")
		return redirect(url_for('hello', resto_id = resto_id))
	else:
		return render_template('deleteitem.html', item = itemToDelete)


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 8000)
	server.socket.close()
