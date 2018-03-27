import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):#创建测试环境，测试之前
        self.app = create_app('testing')
        self.app_context = self.app.app_context()#激活上下文
        self.app_context.push()
        db.create_all()#创建数据库

    def tearDown(self):#测试完毕后
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
