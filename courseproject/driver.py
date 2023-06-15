import ingest
import persist
import logging
import logging.config
class DriverProgram:
    logging.config.fileConfig("resources/configs/logging.conf")
    def __init__(self,fileType):
        self.file_Type=fileType
        logging.debug('init of driverprogram')
    def my_function(self):
        logging.debug("you are in driver my_function")
        logging.debug(f"Processing filetype:{self.file_Type}")
        reader = ingest.FileReader(self.file_Type)
        reader.read_file()
        writer = persist.PersistData("postgres")
        writer.store_date()


driver=DriverProgram("csv")
driver.my_function()

