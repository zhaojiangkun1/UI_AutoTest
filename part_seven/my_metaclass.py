"""
首先有一个类
"""
class Person():
    pass

# 可以打印一个类
print(Person)
p = Person
print(p)
p.name  = "张三"
print(p.name)

# 类可以当作一个参数传递
def func(p):
    print(p.name)

func(p)

# 动态的创建一个类
def get_class(name):
    if name == "Dog":
        class Dog():
            def run(self):
                print("dog run")
        return Dog # 这里返回的是类，而不是类的实例
    else:
        class Cat():
            def run(self):
                print("cat run")
        return Cat

c = get_class("Dog")
print(c)
c.run(c)