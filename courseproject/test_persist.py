import unittest
from processor import persist

class PersistDataTest(unittest.TestCase):
    def test_persist_read_from_pg(self):
        pd=persist.PersistData("postgres")
        courses=pd.read_from_pg("futurexschema.futurex_course_catalog")
        first_element=courses[0]
        self.assertEqual(first_element[1],'Hadoop Spark')
        self.assertEqual(len(courses[0]),9)

if __name__=="__main__":
    unittest.main()