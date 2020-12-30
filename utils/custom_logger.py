import logging


class LogGen:
    @staticmethod
    def log_gen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename='C:\\Users\\Dana Scully\\Selenium\\hybrid_framework\\logs\\automation.log', format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y%m%d %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger