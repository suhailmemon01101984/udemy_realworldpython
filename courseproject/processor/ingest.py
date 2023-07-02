import logging
import logging.config
class FileReader:
    logging.config.fileConfig("../resources/configs/logging.conf")
    logger=logging.getLogger("Ingest")
    def __init__(self,fileType):
        self.logger.debug("init of filereader")
        self.file_Type=fileType
    def read_file(self):
        self.logger.debug(f"Reading a file: {self.file_Type}")
