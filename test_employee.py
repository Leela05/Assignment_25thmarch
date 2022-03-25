import unittest
import sqlite3 as sql

class employee_details(unittest.TestCase):
    def setUp(self):
        self.empname = "Tom"
        self.empcode = "1101"
        self.connection = sql.connect("employee.db")

    def tearDown(self):
        self.empname = ""
        self.empcode = ""
        self.connection.close()

    def test_case1(self):
        result = self.connection.execute("select empname from employee  where empcode="+self.empcode)

        for i in result:
            fetchedemployeename=i[0]

        self.assertEqual(self.empname, fetchedemployeename)

if __name__ == "__main__":
    unittest.main()