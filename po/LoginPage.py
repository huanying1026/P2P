from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from po.Page import Page

class LoginPage(Page):
    ipt_username_loc = (By.CLASS_NAME, 'adm_name')
    ipt_password_loc = (By.CLASS_NAME, 'adm_password')
    ipt_checkcode_loc = (By.NAME, 'adm_verify')
    btn_login_loc = (By.ID, 'login_btn')
    msg_login_success_loc = (By.ID, 'tips')
    msg_usernameorpassword_empty_loc = (By.XPATH, '//*[@id="login_msg"]')

    def set_username(self, name):
        self.wd.find_element(*self.ipt_username_loc).send_keys(name)

    def set_password(self, pwd):
        self.wd.find_element(*self.ipt_password_loc).send_keys(pwd)

    def set_checkcode(self, checkcode):
        self.wd.find_element(*self.ipt_checkcode_loc).send_keys(checkcode)

    def login_submit(self):
        self.wd.find_element(*self.btn_login_loc).click()

    def login_success_msg(self):
        ret = username_password_exception('登录成功')
        return ret

    def username_password_exception(self,warningword):
        WebDriverWait(self.wd, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.msg_usernameorpassword_empty_loc,warningword))
        r = self.wd.find_element(*self.msg_usernameorpassword_empty_loc).text
        return r

if __name__ == '__main__':
    p = LoginPage()
    p.set_username('admin')
    p.set_password('admin')
    p.set_checkcode('1234')
    p.login_submit()
    ret =p.username_password_exception('登录成功')
    print(ret)
    if ret=='登录成功':
        print('PASS')
    else:
        print('FAIL')
    p.wd.quit()