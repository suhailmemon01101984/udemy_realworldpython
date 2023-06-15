import ingest
import persist
class DriverProgram:
    def __init__(self):
        print('init of driver class')
    def my_function(self):
        print("you are in driver function")


driver=DriverProgram()
driver.my_function()
reader=ingest.FileReader()
reader.read_file()
writer=persist.PersistData()
writer.store_date()