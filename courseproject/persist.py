import logging
import logging.config
class PersistData:
    logging.config.fileConfig("resources/configs/logging.conf")
    logger=logging.getLogger("Persist")
    def __init__(self,dbType):
        self.logger.debug("init of persistdata")
        self.db_Type=dbType
    def store_data(self):
        try:
            self.logger.debug(f"storing data in db: {self.db_Type}")
            #var1=100/0
        except Exception as exp:
            self.logger.error(f"An error has occurred: {str(exp)}")