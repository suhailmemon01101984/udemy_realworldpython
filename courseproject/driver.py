from processor import ingest, persist
import logging
import logging.config
from flask import Flask, request

myapp=Flask(__name__)
@myapp.route('/getcourses',methods=['GET'])
def get_courses():
    pd=persist.PersistData("postgres")
    allrecords=pd.read_from_pg("futurexschema.futurex_course_catalog")
    return f"courses are - {allrecords}"



class DriverProgram:
    logging.config.fileConfig("processor/resources/configs/logging.conf")
    def __init__(self,fileType):
        self.file_Type=fileType
        logging.debug('init of driverprogram')
    def my_function(self):
        logging.debug("you are in driver my_function")
        logging.debug(f"Processing filetype:{self.file_Type}")
        reader = ingest.FileReader(self.file_Type)
        read_json=reader.read_file()
        print(f"read the json: {read_json}")
        writer = persist.PersistData("postgres")
        writer.store_data(read_json)


#driver=DriverProgram("json")
#driver.my_function()

myapp.run(port=8005, debug=True)