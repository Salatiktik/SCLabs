import unittest
from MySerializer import MySerializer 

class JsonTests(unittest.TestCase):
    def test_json_primitive(self):
        ser = MySerializer.createSerializer(".json")
        obj = 1
        self.assertEqual(obj,ser.dumps(obj))
        obj = True
        self.assertEqual(obj,ser.dumps(obj))
        obj = "a"
        self.assertEqual(obj,ser.dumps(obj))
        obj = 1.1
        self.assertEqual(obj,ser.dumps(obj))
        obj = None
        self.assertEqual(obj,ser.dumps(obj))

    

unittest.main()