#1 task
# class Money():
#     def __init__(self, dolars, cent):
#         self.dolars = dolars
#         self.cent = cent
#
#     def getSum(self, other):
#         sum = self + other
#         print(sum.dolars, sum.cent)
#
#     def __add__(self, other):
#         return Money(self.dolars + other.dolars, self.cent + other.cent)
#
#     def setDolars(self, dolars):
#         self.dolars = dolars
#
#     def setCent(self, cent):
#         self.cent = cent
#
#
# class Product(Money):
#     def __init__(self, dolars, cent):
#         super().__init__(dolars, cent)
#
#     def decreaseDolars(self, minus):
#         self.dolars -= minus
#
# m1 = Money(1, 30)
# m2 = Money(2, 30)
# m1.getSum(m2)
# p1 = Product(m2.dolars, m2.cent)
# p1.decreaseDolars(1)
# print(p1.dolars)

#2 task
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def __add__(self, add):
#         return Circle(self.radius + add)
#
#     def __sub__(self, sub):
#         return Circle(self.radius - sub)
#
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     def __le__(self, other):
#         return self.radius <= other.radius
#
# c11 = Circle(2)
# c12 = Circle(3)
# print(c11 > c12)
# print(c11 < c12)
# print(c12 == c11)

#3 task
# class Airplane:
#     def __init__(self, type, passengers, maxAmountOfPassengers):
#         self.type = type
#         self.passengers = passengers
#         self.maxAmountOfPassengers = maxAmountOfPassengers
#
#     def __eq__(self, other):
#         return self.type == other.type
#
#     def __add__(self, pas):
#         self.passengers += pas
#     def __sub__(self, pas):
#         self.passengers -= pas
#
#     def __lt__(self, other):
#         return self.maxAmountOfPassengers < other.maxAmountOfPassengers
#     def __gt__(self, other):
#         return self.maxAmountOfPassengers > other.maxAmountOfPassengers
#     def __le__(self, other):
#         return self.maxAmountOfPassengers <= other.maxAmountOfPassengers
#     def __ge__(self, other):
#         return self.maxAmountOfPassengers >= other.maxAmountOfPassengers
#
# p1 = Airplane("Airbus", 120, 150)
# p2 = Airplane("Boeing", 0, 320)
#
# print(p1 == p2)
# print(p1 > p2)
# print(p1 < p2)

#4 task
# class Flat:
#     def __init__(self, cost, square):
#         self.cost = cost
#         self.square = square
#
#     def __eq__(self, other):
#         return self.square == other.square
#
#     def __ne__(self, other):
#         return self.square != other.square
#
#     def __lt__(self, other):
#         return self.cost < other.cost
#     def __gt__(self, other):
#         return self.cost > other.cost
#
# f1 = Flat(100, 100)
# f2 = Flat(200, 200)
# print(f1 == f2)
# print(f1 != f2)
# print(f1 > f2)