#!/usr/bin/env python
import os
from app import create_app, db#为什么这里要导入db，这个db应该还没有初始化把
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate,MigrateCommand
''', Mig'''

app = create_app(os.getenv('FLASK_CONFIG') or 'default')#默认为开发环境
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():#回调函数，避免繁琐导入
	return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command#测试，具体函数还未理解
def test():#函数名为命令名，这里是test
	"""Run the unit tests."""
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
	manager.run()