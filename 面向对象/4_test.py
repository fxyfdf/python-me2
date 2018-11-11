class MyClass(object):
    version = 1.0
    def func(self):
        version=self.version
        print (version)

mc = MyClass()
mc.func()
MyClass_dir = dir (MyClass)
print (MyClass_dir)

MyClass_dt =  MyClass.__dict__
print (MyClass_dt)