from processor import ingest, persist
import logging
import logging.config
from flask import Flask, request

myapp=Flask(__name__)
@myapp.route('/getcourses',methods=['GET'])
def get_courses():
    pd1=persist.PersistData("postgres")
    allrecords=pd1.read_from_pg("futurexschema.futurex_course_catalog")
    return f"courses are - {allrecords}"

@myapp.route('/insertcourse',methods=['POST'])
def insert_course():
    input_json=request.get_json(force=True)
    print(f"input json is: {input_json}")
    pd2=persist.PersistData("postgres")
    pd2.write_to_pg_from_json("futurexschema.futurex_course_catalog",input_json)
    return "success"


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