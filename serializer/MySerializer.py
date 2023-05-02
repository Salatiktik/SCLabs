import serializer.json_utils as json_utils
from serializer.utils import check

class MySerializer:
    def __init__(self, format):
        if format != ".json" and format !=".xml":
            raise Exception("Wrong file format")
        
        self.format = format

    def dumps(self, obj):
        if format == ".json":
            return json_utils._serialize_to_str(check(obj)) 

    def dump(self, obj, file):
        file.write(self.dumps(obj))
    
    