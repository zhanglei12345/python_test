import inspect

# **kwargs 关键字参数    *args 位置参数
# 命名关键字参数，限制关键字参数的名字
# 1.命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
#   def person(name, age, *, city, job):
#        print(name, age, city, job)
# 2.如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
#   def person(name, age, *args, city, job):
#        print(name, age, args, city, job)
#   参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


#def a(a, b=0, *c, d, e=1, **f):
def a(a, b=0, *, d, e=1 ):
    pass
aa = inspect.signature(a)
print("inspect.signature(fn)是:%s" % aa)
print("inspect.signature(fn)的类型：%s" % type(aa))
print("\n")

bb = aa.parameters
print("signature.paramerters属性是:%s" % bb)
print("signature.paramerters属性的类型是%s" % type(bb))
print("\n")

for cc, dd in bb.items():
    print("mappingproxy.items()返回的两个值分别是：%s和%s" % (cc, dd))
    print("mappingproxy.items()返回的两个值的类型分别是：%s和%s" % (type(cc), type(dd)))
    print("\n")
    ee = dd.kind
    print("Parameter.kind属性是:%s" % ee)
    print("Parameter.kind属性的类型是:%s" % type(ee))
    print("\n")
    gg = dd.default
    print("Parameter.default的值是: %s" % gg)
    print("Parameter.default的属性是: %s" % type(gg))
    print("\n")

ff = inspect.Parameter.KEYWORD_ONLY
print("inspect.Parameter.KEYWORD_ONLY的值是:%s" % ff)
print("inspect.Parameter.KEYWORD_ONLY的类型是:%s" % type(ff))


#inspect.signature（fn)将返回一个inspect.Signature类型的对象，值为fn这个函数的所有参数
#inspect.Signature对象的paramerters属性是一个mappingproxy（映射）类型的对象，值为一个有序字典（Orderdict)。
    #这个字典里的key是即为参数名，str类型
    #这个字典里的value是一个inspect.Parameter类型的对象
#inspect.Parameter对象的kind属性是一个_ParameterKind枚举类型的对象，值为这个参数的类型（可变参数，关键词参数，etc）
#inspect.Parameter对象的default属性：如果这个参数有默认值，即返回这个默认值，如果没有，返回一个inspect._empty类。
