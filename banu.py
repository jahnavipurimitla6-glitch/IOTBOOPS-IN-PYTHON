#Parent
class Person:

      def__init__(self,name,age):
         self.Name = name
         self.Age = age


  Class Student(Person):

        def__init__(self,name,age,rollno = 278):
             super()__init__(name,age)
             self.roll_no = rollno


    def introduce(self):
          print("f My name is {self.Name},age{self.Age},roll number{self.roll_no} ")



     obj = Stident("Janu",18)
     obj.introduce
