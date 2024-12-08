# class Myclass:
#     x = 20
#     y = 30
#     z = 40

#     sum = x+y+z

# obj1 = Myclass()
# print(obj1.x)

# obj2 = Myclass()
# print(obj2.y)

# obj3 = Myclass()
# print(obj3.x)
# print(obj3.y)
# print(obj3.z)
# print(obj3.sum)


# class Myclass:
#     x = 20
#     y = 30
#     z = 40

#     def addtwo(self,a,b):
#         sum = self.x + self.y + self.z + a + b
#         print(sum)
    
#     def addnew(self):
#         self.addtwo(9,10)


# Myclass().addtwo(10,10)
# Myclass().addnew()


# class profile:
#     x = 10
#     y = 20

#     @staticmethod
#     def addtwo():
#         sum = profile.x + profile.y
#         print(sum)

# profile.addtwo()


# class profile:
#     x = 10
#     y = 20

#     def __init__(self):
#         print(self.x - self.y)

#     def addtwo(self):
#         sum = self.x + self.y
#         print(sum)   

# profile().addtwo()


# class father:
#     x = 20
#     y = 30

#     def __init__(self):
#         print(self.x - self.y)

#     def addtwo(self):
#         print(self.x + self.y )

#     @staticmethod
#     def multi():
#         print(father.x * father.y)


# class son(father):
#     pass

# son().multi()
# father().addtwo()


# class father:
#     x = 20
#     y = 30

#     def __init__(self):
#         print(self.x - self.y)

#     def addtwo(self):
#         print(self.x + self.y )

#     @staticmethod
#     def multi():
#         print(father.x * father.y)


# class son(father):
#     x = 10
#     y = 5

#     def addtwo(self):
#         print(self.x + self.y )

# objson = son()
# objson.addtwo()

# from abc import ABC,abstractclassmethod

# class father:
#     x = 20
#     y = 30

#     @abstractclassmethod
#     def addtwo(self):
#         pass

# class son(father):
#     def addtwo(self):
#         print(self.x + self.y )


# # fatherobj = father()
# # fatherobj.addtwo()

# sonobj = son()
# sonobj.addtwo()


# class father:
#     def addtwo(self, num1, num2):
#         print(num1+num2)

# class mother:
#     def multi(self, num1, num2):
#         print(num1*num2)

# class son(father,mother):
#     pass

# objson = son()
# objson.addtwo(2,3)
# objson.multi(2,3)

# class grandfather:
#     x = 10
#     y = 20

#     def addtwo(self):
#         print(self.x+self.y)

# class father(grandfather):
#     pass

# class son(father):
#     pass

# class grandson(son):
#     pass


# objgrandson = grandson()
# objgrandson.addtwo()

# public mode:
# class grandfather:
#     x = 10
#     y = 20

#     def addtwo(self):
#         print(self.x+self.y)

# class father(grandfather):
#     pass

# class son(father):
#     pass

# class grandson(son):
#     pass


# objgrandson = grandson()
# print(objgrandson.x)


# private mode: 
# class grandfather:
#     __x = 10
#     __y = 20

#     def addtwo(self):
#         print(self.__x+self.__y)


# objgrandfather = grandfather()
# objgrandfather.addtwo()


# protected mode:
# class grandfather:
#     _x = 10
#     __y = 20
#     _z = 100


# objgrandfather = grandfather()
# print(objgrandfather._z)

# class Myclass:
#     x = 10
#     y = 20

#     def __init__(self,a,b):
#         print("I am Constractor")
#         print(self.x+self.y)
#         print(a+b)

# Myclass(5,10)

# class Myclass:
#     x = 10
#     y = 20

#     def __init__(self,a):
#         self.a = a

#     def addtwo(self):
#         print(self.x + self.a)

# obj = Myclass(100)
# print(obj.a)
# obj.addtwo()

# class Myclass:
#     x = 10
#     y = 20

#     @staticmethod
#     def addtwo():
#         print(Myclass.x+Myclass.y)

# Myclass.addtwo()

# obj = Myclass()
# obj.addtwo()

# class Myclass:
#     x = 10
#     y = 20

#     @staticmethod
#     def addtwo():
#         print(Myclass.x+Myclass.y)
# print("Without Creating Object : ")
# print(Myclass.x)
# print(Myclass.y)

# print("After Creating Object : ")
# obj = Myclass()
# print(obj.x)
# print(obj.y)

