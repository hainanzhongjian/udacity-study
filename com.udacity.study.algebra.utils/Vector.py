# -*- coding: UTF-8 -*-
from math import sqrt , acos ,pi
from decimal import Decimal ,getcontext

class Vector(object):

    # 构造方法
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            times_scalar = coordinates
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError("The coordinates must be nonempty")
        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    ###
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    # 向量的大小
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    # 单位向量
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1,dot(u2))

v1 = Vector([-0.221, 7.437])
print v1.magnitude()

v2 = Vector([-8.813, -1.331, -6.247])
print v2.magnitude()

v3 = Vector([5.581, -2.136])
print v3.normalized()

v4 = Vector([1.996, 3.108, -4.554])
print v4.normalized()