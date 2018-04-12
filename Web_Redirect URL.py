from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def admin():
	return('Hello Admin')
	
@app.route('/guest/<guest>')
def hello_user(guest):
	return('Hello %s' %guest)
	
@app.route('/user/<name>')
def hello(name):
	if(name==admin):
		return redirect(url_for('admin'))
	else:
		return redirect(url_for('hello_user',guest=name))
		
if __name__ == '__main__':
	app.run(debug = True)
