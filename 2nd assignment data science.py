#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##1. Explain what inheritance is in object-oriented programming and why it is used.


# In[5]:


'''inheritance in Python's object-oriented programming is a mechanism where a class can inherit attributes and 
methods from another class, known as the base or parent class. It is used to promote code reuse and establish 
a hierarchical relationship between classes. By inheriting from a base class, a derived or child class can 
access and extend the functionalities defined in the base class, reducing code duplication and enhancing 
modularity.'''


# In[ ]:


##2. Discuss the concept of single inheritance and multiple inheritance, highlighting their
differences and advantages.


# In[6]:


'''Single inheritance in Python involves a class inheriting from a single base class. This means that a derived
class can inherit attributes and methods from only one parent class. On the other hand, multiple inheritance 
allows a class to inherit from multiple base classes. This means that a derived class can inherit attributes 
and methods from multiple parent classes. Single inheritance provides a simpler and more straightforward 
relationship between classes, while multiple inheritance offers more flexibility and the ability to combine 
features from different sources. However, multiple inheritance can also introduce increased complexity and 
potential conflicts if not managed carefully.'''


# In[ ]:


##3. Explain the terms "base class" and "derived class" in the context of inheritance.


# In[7]:


'''In the context of inheritance, the "base class" refers to the class being inherited from, and it is also 
called the superclass. The "derived class" refers to the class that inherits from the base class or extends 
its functionality, and it is also known as the subclass. The derived class inherits the attributes and 
methods of the base class and can add its own unique attributes and methods.'''


# In[ ]:


##4. What is the significance of the "protected" access modifier in inheritance? How does
get_ipython().run_line_magic('pinfo', 'modifiers')


# In[8]:


''''the "protected" access modifier has significance in inheritance. When a member variable or method is marked 
as "protected" in the base class, it can be accessed by the derived class and other classes within the same 
module or package. It is more accessible than the "private" modifier, which restricts access to only the 
defining class, but less accessible than the "public" modifier, which allows unrestricted access from any 
class.'''


# In[ ]:


##5. What is the purpose of the "super" keyword in inheritance? Provide an example.


# In[12]:


'''The "super" keyword in Python is used to refer to the parent class or base class within the context of 
inheritance. It is primarily used to invoke the parent class's methods or access its attributes. By using the 
"super" keyword, you can explicitly call the parent class's methods and initialize inherited members or 
extend their functionality. Here's an example:'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print("Employee ID:", self.employee_id)


person = Person("srinivas", 27)
person.display_info()
print()
employee = Employee("aditya", 2, 5634)
employee.display_info()


# In[ ]:


##6. Create a base class called "Vehicle" with attributes like "make", "model", and "year".
Then, create a derived class called "Car" that inherits from "Vehicle" and adds an
attribute called "fuel_type". Implement appropriate methods in both classes.


# In[13]:


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year) 
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()  
        print("Fuel Type:", self.fuel_type)


my_car = Car("hyundai", "creta", 2024, "Petrol")
my_car.display_info()


# In[ ]:


##7. Create a base class called "Employee" with attributes like "name" and "salary."
Derive two classes, "Manager" and "Developer," from "Employee." Add an additional
attribute called "department" for the "Manager" class and "programming_language"
for the "Developer" class.


# In[14]:


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  
        self.department = department

    def display_info(self):
        super().display_info()  
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary) 
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print("Programming Language:", self.programming_language)


manager = Manager("prateek", 50000, "IT")
manager.display_info()

print()

developer = Developer("adil", 40000, "Python")
developer.display_info()


# In[ ]:


##8. Design a base class called "Shape" with attributes like "colour" and "border_width."
Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add
specific attributes like "length" and "width" for the "Rectangle" class and "radius" for
the "Circle" class.


# In[15]:


class Shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width

    def display_info(self):
        print("Colour:", self.colour)
        print("Border Width:", self.border_width)


class Rectangle(Shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width)  
        self.length = length
        self.width = width

    def display_info(self):
        super().display_info()  
        print("Length:", self.length)
        print("Width:", self.width)


class Circle(Shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width)  
        self.radius = radius

    def display_info(self):
        super().display_info()  
        print("Radius:", self.radius)


rectangle = Rectangle("green", 9, 10, 5)
rectangle.display_info()
print()
circle = Circle("red", 1, 7)
circle.display_info()


# In[ ]:


##9. Create a base class called "Device" with attributes like "brand" and "model." Derive
two classes, "Phone" and "Tablet," from "Device." Add specific attributes like
"screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.


# In[16]:


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)  
        self.screen_size = screen_size

    def display_info(self):
        super().display_info() 
        print("Screen Size:", self.screen_size)


class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info() 
        print("Battery Capacity:", self.battery_capacity)


phone = Phone("Apple", "iPhone 12", "6.1 inches")
phone.display_info()

print()

tablet = Tablet("Samsung", "Galaxy Tab S7", "8000 mAh")
tablet.display_info()


# In[ ]:


##10. Create a base class called "BankAccount" with attributes like "account_number" and
"balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from
"BankAccount." Add specific methods like "calculate_interest" for the
"SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.


# In[17]:


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)  

    def calculate_interest(self, interest_rate):
        interest = self.balance * interest_rate
        self.balance += interest
        print("Interest calculated:", interest)


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)  

    def deduct_fees(self, fee_amount):
        self.balance -= fee_amount
        print("Fees deducted:", fee_amount)


savings_account = SavingsAccount("5465444515", 5000)
savings_account.display_info()
print()
savings_account.calculate_interest(6)
savings_account.display_info()
print()
checking_account = CheckingAccount("8654523444", 10000)
checking_account.display_info()
print()
checking_account.deduct_fees(100)
checking_account.display_info()


# In[ ]:




