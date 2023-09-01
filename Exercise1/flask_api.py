#!/usr/bin/python


"""This program written GET Rest api using Flask frame work
i have written three url's user can can select which url he need /admin,/student,/staff"""
from flask import *      	#import the all flask libraries
#from flask import Flask
app = Flask(__name__)    	#initialize the app here

@app.route('/admin')        	#this is decorator use to route the app
def admin() :
	return ("this is for admin Department")
@app.route('/student')
def student() :
	return ("this is for student union Department")
@app.route('/staff')
def staff() :
	return ("this is staff department")

@app.route('/usr/name')
def usr(name) :
	if name == admin :
		return redirect(url_for('admin'))
	if name == student :
		return redirect(url_for('student'))
	if name == staff :
		return redirect(url_for('staff'))

if __name__ == '__main__' :
	app.run(debug = True)

