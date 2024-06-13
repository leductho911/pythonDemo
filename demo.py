import MyModule
from mypackage import module1, module2
from mypackage.module1 import function1
from mypackage.module2 import function2

MyModule.hello_world()
MyModule.cal_emi()

print(module1.function1())
print(module2.function2())

print(function1())
print(function2())
