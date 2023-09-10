import logging
import logging.config
import json
class FileReader:
    logging.config.fileConfig("processor/resources/configs/logging.conf")
    logger=logging.getLogger("Ingest")
    def __init__(self,fileType):
        self.logger.debug("init of filereader")
        self.file_Type=fileType
    def read_file(self):
        self.logger.debug(f"Reading a file: {self.file_Type}")
        with open('course.json') as f:
            data=json.load(f)
        print(f"new course is {data}")
        return data

