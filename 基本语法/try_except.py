
"""
1/0
Traceback (most recent call last):
  File "E:\PYTHON\PyCharm\venv\lib\site-packages\IPython\core\interactiveshell.py", line 3265, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-3-9e1622b385b6>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero

"""

class  MuffedCalculator():
    muffled = False
    def calc(self,expr):
        print (expr)
        try :
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

def main():
    if __name__ == '__main__':
        aa = MuffedCalculator()
        aa.calc(1+1)



