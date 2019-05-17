
import unittest
from po.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.obj = LoginPage()

    def tearDown(self):
        self.obj.quit()

    def verify_login(self,name,pwd,checkcode):
        self.obj.open_url()
        self.obj.set_username(name)
        self.obj.set_password(pwd)
        self.obj.set_checkcode(checkcode)
        self.obj.login_submit()

    def test_username_empty(self):
        '''账号为空验证'''
        self.verify_login('','admin','1234')
        r = self.obj.login_success_msg()
        self.assertEqual(r,'管理员帐号不能为空')

    def test_pwd_empty(self):
        '''密码为空验证'''
        self.verify_login('admin','','1234')
        r = self.obj.login_success_msg()
        self.assertEqual(r,'管理员密码不能为空')

    def test_checkcode_empty(self):
        '''验证码为空验证'''
        self.verify_login('admin', 'admin', '')
        r = self.obj.login_success_msg()
        self.assertEqual(r, '验证码不能为空')

    def test_name_error(self):
        '''账号错误验证'''
        self.verify_login('add', 'admin', '1234')
        r = self.obj.login_success_msg()
        self.assertEqual(r, '管理员账号错误')

    def test_pwd_error(self):
        '''密码错误验证'''
        self.verify_login('admin', '1234', '1234')
        r = self.obj.login_success_msg()
        self.assertEqual(r, '管理员密码错误')

    def test_login_success(self):
        '''登录成功验证'''
        self.verify_login('admin', 'admin', '1234')
        r = self.obj.login_success_msg()
        self.assertEqual(r, '登录成功')

if __name__ == '__main__':
    unittest.main(verbosity=2)