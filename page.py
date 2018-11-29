import locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def function_1(self):
        '''Verb.

        Next line.
        '''
        pass
