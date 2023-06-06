---
marp: true
theme: uncover
_class: invert
---
# OOP Python
Object oriented programming

---
# What's OOP
*  It is a programming paradigm or approach that organizes code around objects, which are instances of classes

---
# Benefits of OOP
* Reusability
* Maintainability
* Inheritance and Code Reusability

---
# Classes

* Classes are blueprints or templates that define the structure and behavior of objects in object-oriented programming. They specify what attributes (data) an object will have and what actions (methods) it can perform

---
```python
class Car:
    brand = "Name"
    model = "Name"
    max_speed = 210
    year = 2023

```

---

# Objects

* Objects are instances of classes in object-oriented programming. They are the actual entities created based on the blueprints provided by classes
``` python
new_car = Car()
print(new_car)
print(new_car.brand)
```

---
# Constructor
* A method (function) in a class that creates the object with given values
---
```python
class Car:
    def __init__(self, brand,name,model,max_speed, year):
        brand = brand
        model = model
        max_speed = max_speed
        year = year

```

```python
new_car = Car("Name", "Name", 210, 2023)
print(new_car)
print(new_car.brand)
```
* self -> keyword that refers to the object

---
# Methods
* Methods are functions within a class. They are used to extend the functionality of a class

* __ init __ is the most basic method

* methods are created the same way as functions
* the __self__ keyword __HAS__ to added in every method

Note: it's good practice to have get and set method for each parameter in the class

---
```python
class Car:
    def __init__(self, brand,name,model,max_speed, year):
        brand = brand
        model = model
        max_speed = max_speed
        year = year
    
    def get_brand_name(self):
        return brand

    def calculate_age(self, current_year)
        age = current_year - self.year
        return age

new_car = Car("Name", "Name", 210, 2010)

#calling methods
brand_name = new_car.get_brand_name()

age_of_car = new_car.calculate_age(2023)

```

