from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)

#from flask_script import Manager 		#flask.ext.script is deprecated, use flask_script instead.
#manager = Manager(app)
# ...
from flask_bootstrap import Bootstrap
# ...
bootstrap = Bootstrap(app)
if __name__ == '__main__':
	bootstrap
#	app.run(debug=True)
#	manager.run()