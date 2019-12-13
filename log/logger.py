import logging
import os
class logger:
    def __init__(self,loggername):
        self.logger=logging.getLogger(loggername)
        self.logger.setLevel(logging.INFO)
        log_path=os.path.dirname(os.path.dirname(__file__))
        logname=log_path+'/logs/log.log'
        fh=logging.FileHandler(logname,encoding='utf-8')
        fh.setLevel(logging.INFO)
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlogger(self):
        return self.logger