
class AttrClass(object):

    def __init__(self,name,age=23,sex='male'):
        self.name=name
        self.age=age
        self.sex=sex
    def show(self):
        print (self.name,self.age,self.sex)

suo = AttrClass('SUO')
suo.show()