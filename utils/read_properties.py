import configparser

config = configparser.RawConfigParser()
config.read('C:\\Users\\Dana Scully\\Selenium\\hybrid_framework\\configs\\config.ini')

class ReadConfig:

    #staticmethod so can use methods without instantiating class
    @staticmethod
    def get_app_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_username():
        un = config.get('common info', 'un')
        return un

    @staticmethod
    def get_password():
        pw = config.get('common info', 'pw')
        return pw

