from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string' #app.config 字典可用来存储框架、扩展和程序本身的配置变量。
#为了增强安全性，密钥不应该直接写入代码，而要保存在环境变量中。
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    #验证函数用来验证用户提交的输入值是否符合要求。
    name = StringField('What is your name?', validators=[DataRequired()])
    #可选参数 validators 指定一个由验证函数组成的列表，在接受
    #用户提交的数据之前验证数据。验证函数 Required() 确保提交的字段不为空。
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])#methods 参数告诉 Flask 在 URL 映射中把这个视图函数注册为GET 和 POST 请求的处理程序。
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
#推荐使用 url_for() 生成 URL，因为这个函数使用 URL 映射生成 URL，从而保证 URL 和定义的路由兼容，而且修改路由名字后依然可用。