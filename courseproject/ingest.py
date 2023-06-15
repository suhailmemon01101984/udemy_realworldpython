import logging
class FileReader:
    logging.basicConfig(level="DEBUG")
    def __init__(self,fileType):
        logging.debug("init of filereader")
        self.file_Type=fileType
    def read_file(self):
        logging.debug(f"Reading a file: {self.file_Type}")
