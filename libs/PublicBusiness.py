from po.LoginPage import LoginPage


def Login_info(name='admin', pwd='admin'):
    obj = LoginPage()
    obj.get_url()
    obj.set_username(name)
    obj.set_password(pwd)
    obj.login_submit()
    return obj.wd


if __name__ == '__main__':
    Login_info('admin', 'admin')
