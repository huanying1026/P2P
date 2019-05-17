from driver import create__browser_driver
url = 'localhost/m.php'

class Page():
    def __init__(self, driver=''):
        wd = driver
        if wd == '':
            self.wd = create__browser_driver()
        else:
            self.wd = wd
        self.wd.maximize_window()
        self.wd.implicitly_wait(10)

    def open_url(self, pathUrl=url):
        self.wd.get(pathUrl)

    def close_bs(self):
        self.wd.quit()
