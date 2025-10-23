class Std:
    
    def __init__(self,name):
        self.name = name
    def show(self):
            print("My name:",self.name)
    def __del__(self):
      print("object destroyed")

s1-std("iot")
s2=std("iotab")

s2.show()
del s1
s1.show()

