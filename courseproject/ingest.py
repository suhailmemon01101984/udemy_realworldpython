import logging
import logging.config
class FileReader:
    logging.config.fileConfig("resources/configs/logging.conf")
    def __init__(self,fileType):
        logging.info("init of filereader")
        self.file_Type=fileType
    def read_file(self):
        logging.debug(f"Reading a file: {self.file_Type}")
