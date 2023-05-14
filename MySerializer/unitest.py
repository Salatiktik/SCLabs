import unittest
from MySerializer import MySerializer 
import math

class JsonTests(unittest.TestCase):
    def test_json_primitive(self):
        ser = MySerializer.createSerializer(".json")
        obj = 1
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = True
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = "a"
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = 1.1
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = None
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))

    def test_xml_primitive(self):
        ser = MySerializer.createSerializer(".xml")
        obj = 1
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = True
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = "a"
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = 1.1
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = None
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))

    def test_json_collections(self):
        ser = MySerializer.createSerializer(".json")
        obj = [1,2,3,4,5]
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = (1,2,3,4,5)
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = {1,2,3,4,5}
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = {1:1,2:2,3:3,4:4,5:5}
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
    
    
    def test_xml_collections(self):
        ser = MySerializer.createSerializer(".xml")
        obj = [1,2,3,4,5]
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = (1,2,3,4,5)
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = {1,2,3,4,5}
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))
        obj = {1:1,2:2,3:3,4:4,5:5}
        self.assertEqual(obj,ser.loads(ser.dumps(obj)))

    def test_json_func(self):
        def Rprint(a):
            return a*a
        
        ser = MySerializer.createSerializer(".json")
        self.assertEqual(Rprint(2),ser.loads(ser.dumps(Rprint))(2))
            

    def test_xml_func(self):
        def Rprint(a):
            return math.sin(a)
        
        ser = MySerializer.createSerializer(".xml")
        self.assertEqual(Rprint(2),ser.loads(ser.dumps(Rprint))(2))
        
unittest.main()