from flask import Flask,render_template,request
from flask_script import Manager
app = Flask(__name__)

'''Flask 用这个参数决定程序的根目录，以便稍后能够找到相对于程
序根目录的资源文件位置。Python 的 __name__ 变量就是所需的值。'''

from flask_bootstrap import Bootstrap
manager = Manager(app)
bootstrap = Bootstrap(app)
'''客户端（例如 Web 浏览器）把请求发送给 Web 服务器，
Web 服务器再把请求发送给 Flask,
程序实例需要知道对每个 URL 请求运行哪些代码，
所以保存了一个 URL 到Python 函数的映射关系。
处理 URL 和函数之间关系的程序称为路由。
'''
@app.route('/')
def index(): #像 index() 这样的函数称为视图函数（ view function）。
	#把 index() 函数注册为程序根地址的处理程序。	
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' % user_agent
	#函数的返回值称为响应，是客户端接收到的内容。
	#如果客户端是 Web 浏览器，响应就是显示给用户查看的文档。
	##Flask 使用上下文临时把某些对象变为全局可访问。request(伪全局变量)
'''使用修饰器把函数注册为事件的处理程序。
Flask 从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。 
	请求对象封装了客户端发送的 HTTP 请求。'''
@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)
	
'''Flask 支持在路由中使用 int、 float 和 path 类型。
path 类型也是字符串，但不把斜线视作分隔符，而将其当作动态片段的一部分。'''
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404
	
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500
		
#from flask_script import Manager 		#flask.ext.script is deprecated, use flask_script instead.
#manager = Manager(app)
# ...

if __name__ == '__main__':
	manager.run()	
	#app.run(debug=True)	#debug=True=启用调试模式
	#如果这个脚本由其他脚本引入，程序假定父级脚本会启动不同的服务器，
	#因此不会执行 app.run()。
	#manager.run()
	
