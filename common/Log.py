import os
import logging
from logging.handlers import TimedRotatingFileHandler
import getpathInfo



path = getpathInfo.get_Path()
log_path = os.path.join(path,'result')

class Logger(object):
    def __init__(self,logger_name = 'log...'):
        sefl.logger = logging.getLogger(logger_name)
        logging.rot.setLevel(logging.NOTSET)
        self.log_file_name ='logs'
        self.backup_count =5

        slef.console_output_level ='WARNING
        slef.file_output_level ='DEBUG'

        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):

        if not self.logger.handlers:
            console_hander = logging.StreamHandler()
            console_hander.setFormatter(self.formatter)
            console_hander.setLevel(self.console_output_level)

            self.logger.addHandler(console_hander)

            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, self.log_file_name), when='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()