from constants import PRIMITIVES,COLLECTIONS

class Json:
    def __init__(self):
        self.pos = 0
        self.indent = 0

    def dump(self, obj, fp):
        fp.write(self.dumps(obj))

    def dumps(self, obj):
        return self.serialize_to_str(obj)

    def serialize_to_str(self, obj):
        if type(obj) in PRIMITIVES:
            return self.serialize_primitive(obj)

        elif type(obj) is dict:
            return self.serialize_dict(obj)
        
        elif type(obj) in COLLECTIONS:
            return self.serialize_collection(obj)

        else:
            raise Exception("Unknown type to serialize")

    def serialize_collection(self, obj):
        result = '\n' + ' ' * self.indent + '{\n'
        result += ' ' * self.indent + f'"type": "{type(obj).__name__}"\n'
        result += ' ' * self.indent + '"value": ['

        self.indent += 4

        for i in obj:
            result += self.serialize_to_str(i) + ','

        if len(result) > 1 and result[-1] == ',':
            result = result[:-1]

        self.indent -= 4
        result += '\n' + ' ' * self.indent + ']\n' + ' ' * self.indent + '}'

        return result

    def serialize_primitive(self, obj):
        result = '\n' + ' ' * self.indent + '{\n'
        result += ' ' * self.indent + f'"type": "{type(obj).__name__}"\n'
        result += ' ' * self.indent + '"value": '

        if obj is None:
            result += 'null'

        elif isinstance(obj, bool):
            result += 'true' if obj else 'false'

        elif isinstance(obj, (int, float)):
            result += str(obj)

        elif isinstance(obj, str):
            result += f'"{obj}"'

        result += '\n' + ' ' * self.indent + '}'

        return result

    def serialize_dict(self, obj):
        result = '\n' + ' ' * self.indent + '{\n'
        result += ' ' * self.indent + f'"type": "{type(obj).name}"\n'
        result += ' ' * self.indent + '"value": {'

        self.indent += 4

        for key, value in obj.items():
            result += self.serialize_to_str(key) + ': ' + self.serialize_to_str(value) + ', \n'

        if len(result) > 1 and result[-3] == ',':
            result = result[:-3]

        result += '\n' + ' ' * self.indent + '}\n'
        self.indent -= 4
        result += ' ' * self.indent + '}'

        return result