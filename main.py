import math
# from py_serializer.serializer import Serializer
# from sir_Bychko_serializer.serializer_zavod import zavod
# from serdeserf import Serdeser
# from KluchinskiySerializator import great_serializer as gt
# from DariasSerializer153501.serialiser_fabric import serialiser_JSON as Ser
# from Serializer import serializers_factory
# from serializers import factory
# from kirznerSerializer import json_serializer
# from lab3.serializer.src.factory import Factory
# from lab_serializer.serializers.serializer_factory import SerializerFactory
# from ser_Stovba.factory import ser_factory
# from object_serializer.serializer_factory import SerializerFactory
# from serializers.factory import Factory
# from Artur_serializer.serializer_zavod import zavod
# from Serializer import SerializerFactory
# from makarenko_serializer.serializer import Serializer
from MySerializer.MySerializer import MySerializer


def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


# ser = Serializer.create_serializer('json')
# ser = Serdeser('json')
# ser = Ser()
# ser = serializers_factory.SerializersFactory.create_serializer(serializers_factory.SerializerType.XML)
# ser = factory.SerializersFactory.create_serializer(factory.SerializerType.XML)
# ser = json_serializer.JsonSerializer()
# ser = Factory.create_serializer('.xml')
# ser = SerializerFactory.get_serializer('xml')
# ser = ser_factory.create_ser('xml')
# ser = SerializerFactory.create_serializer('xml')
# ser = SerializersFactory.
# ser = Factory.create_serializer('xml')
# ser = zavod.create_zavod('xml')
# ser = SerializerFactory.SerializerFactory.create_serializer('xml')
# ser = Serializer.create_serializer('xml')
ser = MySerializer.createSerializer('.xml')
#
# var = 15
# var_ser = ser.dumps(var)
# var_des = ser.loads(var_ser)
# print(var_des)
#
C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

c = C(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())


def f(a):
    for i in a:
        yield i


g = f([1, 2, 3])
print(next(g))
g_s = ser.dumps(g)
g_d = ser.loads(g_s)
print(next(g_d))

# f = C(1, 2)
# print(f.my_sin(11))



