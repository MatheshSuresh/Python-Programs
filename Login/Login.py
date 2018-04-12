from flask import Flask, redirect, url_for,request
app = Flask(__name__)
		
@app.route('/login/<name>')
def name(name):
	return ('Happy Birthday %s' %name)
	
@app.route('/login',methods = ['POST','GET'])
def login():
	if (request.method == 'POST'):
		user = request.form['nm']
		return redirect(url_for('name',name=user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('name',name=user))
		
if __name__ == '__main__':
	app.run(debug = True)
