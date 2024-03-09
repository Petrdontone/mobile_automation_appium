from appium import webdriver


class Singleton(type):
    _instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        print('_instances', cls._instances)
        return cls._instances[cls]


class AppiumDriver(metaclass=Singleton):

    def create_driver(self, url, capabilities):
        self.driver = webdriver.Remote(command_executor=url, options=capabilities)
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()

