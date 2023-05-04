from json_utils import Json
##import MySerializer.xml_utils as Xml
from utils import check

class MySerializer:
    @staticmethod
    def createSerializer(format):
        if format == ".json":
            return Json()

        elif format == ".xml":
            return Xml

        else:
            raise Exception("Wrong format")    