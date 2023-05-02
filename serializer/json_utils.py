from serializer.constants import PRIMITIVES,COLLECTIONS

indent = 0

def _serialize_to_str(obj):
    if type(obj) in PRIMITIVES:
        return _serialize_primitive(obj)

    elif type(obj) is dict:
        return _serialize_dict(obj)
    
    elif type(obj) in COLLECTIONS:
        return _serialize_collection(obj)

    else:
        raise Exception("Unknown type to serialize")

def _serialize_collection(obj):
    result = '\n' + ' ' * indent + '{\n'
    result += ' ' * indent + f'"type": "{type(obj).name}"\n'
    result += ' ' * indent + '"value": ['

    indent += 4

    for i in obj:
        result += _serialize_to_str(i) + ','

    if len(result) > 1 and result[-1] == ',':
        result = result[:-1]

    indent -= 4
    result += '\n' + ' ' * indent + ']\n' + ' ' * indent + '}'

    return result

def _serialize_primitive(obj):
    result = '\n' + ' ' * indent + '{\n'
    result += ' ' * indent + f'"type": "{type(obj).name}"\n'
    result += ' ' * indent + '"value": '

    if obj is None:
        result += 'null'

    elif isinstance(obj, bool):
        result += 'true' if obj else 'false'

    elif isinstance(obj, (int, float)):
        result += str(obj)

    elif isinstance(obj, str):
        result += f'"{obj}"'

    result += '\n' + ' ' * indent + '}'

    return result

def _serialize_dict(obj):
    result = '\n' + ' ' * indent + '{\n'
    result += ' ' * indent + f'"type": "{type(obj).name}"\n'
    result += ' ' * indent + '"value": {'

    indent += 4

    for key, value in obj.items():
        result += _serialize_to_str(key) + ': ' + _serialize_to_str(value) + ', \n'

    if len(result) > 1 and result[-3] == ',':
        result = result[:-3]

    result += '\n' + ' ' * indent + '}\n'
    indent -= 4
    result += ' ' * indent + '}'

    return result