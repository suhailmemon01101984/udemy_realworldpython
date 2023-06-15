import logging
class PersistData:
    logging.basicConfig(level="DEBUG")
    def __init__(self,dbType):
        logging.debug("init of persistdata")
        self.db_Type=dbType
    def store_date(self):
        logging.debug(f"storing data in db: {self.db_Type}")