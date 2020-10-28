import logging
import logging.config

class InvestmentLogger:
    __instance = None

    @staticmethod
    def getInstance(cfg):
        if InvestmentLogger.__instance == None:
            InvestmentLogger(cfg)
        return InvestmentLogger.__instance
    
    def __init__(self, cfg):
        if InvestmentLogger.__instance != None:
            raise Exception("This class is a singleton, call instance()")
        else:
            InvestmentLogger.__instance = self
            self.cfg = cfg
            self.__configure()

    def __configure(self):
        try:
            logging.config.dictConfig(self.cfg)
        except Exception as e:
            print(e)
            print("Error in logger configuration.  Defaulting to console logging")
            logging.basicConfig()
    
    def getLogger(self,logger):
       return logging.getLogger(logger)
