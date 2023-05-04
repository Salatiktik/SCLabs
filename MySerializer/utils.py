from constants import PRIMITIVES, COLLECTIONS
import inspect
import types

def check(obj):
    if(type(obj) in PRIMITIVES or type(obj) in COLLECTIONS):
        return obj
    
    elif (inspect.isfunction(obj) or inspect.ismethod(obj) or type(obj) == types.LambdaType): 
        return pack_func(obj)

    elif(inspect.isclass(obj)):
        return pack_class(obj)
    
    else:
        return pack_obj(obj)
    
def pack_func(obj):
    result = {"type": "function"}

    if inspect.ismethod(obj):
        obj = obj.__func__

    result["name"] = obj.__name__

    arguments = {}

    for (key, value) in inspect.getmembers(obj.__code__):
        if key.startswith("co_"):
            if isinstance(value, bytes):
                value = list(value)

            if getattr(obj, "__iter__", None) is not None and not isinstance(value, str):
                converted_vals = []

                for val in value:
                    if val is not None:
                        converted_vals.append(check(val))
                    else:
                        converted_vals.append(None)

                arguments[key] = converted_vals

                continue

            arguments[key] = value

    result["args"] = arguments

    return result

def pack_class(obj):
    result = {"type": "class", "name": obj.__name__}

    for attr in inspect.getmembers(obj):
        if attr[0] not in (
                "__mro__", "__base__", "__basicsize__",
                "__class__", "__dictoffset__", "__name__",
                "__qualname__", "__text_signature__", "__itemsize__",
                "__flags__", "__weakrefoffset__", "__objclass__"
        ):
            attr_value = getattr(obj, attr[0])
            result[attr[0]] = check(attr_value)

    result["bases"] = [pack_class(base) for base in obj.__bases__ if base != object]

    return result

def pack_object(obj):
    result = {"type": "object", "class": pack_class(obj.__class__), "attr": {}}

    for key, value in inspect.getmembers(obj):
        if not key.startswith("__") and not (inspect.isfunction(value) or inspect.ismethod(value) or type(value) == types.LambdaType):
            result["attr"][key] =check(value)

    return result
