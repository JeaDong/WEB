from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello,%s!</h1>' % name
if __name__ == '__main__':
	app.run(debug=True)
'''__name__== ' __main__ ' 是 Python 的惯常用法，在这里确保直接执行这个脚本时才启动开发
Web 服务器。如果这个脚本由其他脚本引入，程序假定父级脚本会启动不同的服务器，因
此不会执行 app.run() 。'''
'''有一些选项参数可被 app.run() 函数接受用于设置 Web 服务器的操作模式。在开发过程中
启用调试模式会带来一些便利，比如说激活调试器和重载程序。要想启用调试模式，我们
可以把 debug 参数设为 True 。'''
#2.5.1　程序和请求上下文
'''为了避免大量可有可无的参数把视图函数弄得一团糟，Flask 使用上下文临时把某些对象
变为全局可访问。有了上下文，就可以写出下面的视图函数：'''
#from flask import request
#@app.route('/')
#def index():
#	user_agent = request.headers.get('User-Agent')
#	return '<p>Your browser is %s</p>' % user_agent
'''request虽然不是全局变量，但是在多个线程的单独处理
时就相当于全局变量的作用'''
'''Falsk 使用上下文让特定的变量在一个线程中全局
可访问，与此同时却不会干扰其他线程。'''
'''线程是可单独管理的最小指令集。进程经常使用多个活动线程，有时还会共
享内存或文件句柄等资源。多线程 Web 服务器会创建一个线程池，再从线
程池中选择一个线程用于处理接收到的请求。'''
