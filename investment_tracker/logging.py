import logging

class InvestmentLogger:
    __instance = None

    @staticmethod
    def instance():
        if InvestmentLogger.__instance == None:
            InvestmentLogger()
        return InvestmentLogger.__instance
    
    def __init__(self):
        if InvestmentLogger.__instance != None:
            raise Exception("This class is a singleton, call instance()")
        else:
            InvestmentLogger.__instance = self

with open('conf/logger.yaml', 'r') as f:
    log_cfg = yaml.safe_load(f.read())

logging.config.dictConfig(log_cfg)

logger = logging.getLogger('dev')

# Create logger
logging.basicConfig(format='%s(levelname)s:%(message)s, ')
logging.basicConfig(format='%s(levelname)s:%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')
logging.basicConfig()
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %I:%M:%S,uuu')
handler.setFormatter(formatter)
logger.addHandler(handler)
