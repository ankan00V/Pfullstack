<!-- ============================================================= -->
<!-- 🐍 PYTHON OOP CONCEPTS – VISUAL + TECHNICAL README TEMPLATE -->
<!-- ============================================================= -->

<div align="center">

# 🧠 Python OOP Engineering Blueprint
### ⚙️ Object-Oriented Programming in Python — Structured Technical Guide

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/OOP-Architecture-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Design-Principles-black?style=for-the-badge" />

---

<img src="https://media.giphy.com/media/QTfX9Ejfra3ZmNxh6B/giphy.gif" width="450"/>

### 🏗 Clean Architecture • ⚡ Runtime Polymorphism • 🔐 Encapsulation • 🛡 Defensive Programming

</div>

---

# 📌 Repository Overview

This repository provides a **production-grade walkthrough of Object-Oriented Programming (OOP) in Python**, designed with implementation clarity and architectural thinking.

It covers:

- 🧬 Inheritance  
- 🔄 Polymorphism  
- 🔐 Encapsulation  
- 🏛 Abstraction  
- 🎯 Property Decorators  
- 🧩 Abstract Base Classes  
- 🛡 Custom Exception Handling  

Ideal for:
- 🎓 University Exams  
- 💼 Technical Interviews  
- 🏗 Backend Engineering  
- 🚀 System Design Foundations  

---

# 🏗 Core OOP Architecture

---

## 1️⃣ Inheritance — Hierarchical Reusability

> Enables structured code reuse through class hierarchies.

```python
class Vehicle:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def display(self):
        print(self.model, self.color)


class Car(Vehicle):
    def __init__(self, model: str, color: str, seats: int):
        super().__init__(model, color)
        self.seats = seats
```

### 🔬 Technical Highlights
- Constructor chaining
- `super()` ensures correct MRO
- Promotes DRY architecture

---

## 2️⃣ Polymorphism — Runtime Dynamic Dispatch

> Same method signature, different runtime behavior.

```python
class Vehicle:
    def display(self):
        print("Vehicle Info")


class Car(Vehicle):
    def display(self):
        super().display()
        print("Car Specific Info")
```

✔ Late binding  
✔ Method overriding  
✔ Interface consistency  

---

## 3️⃣ Constructor Overloading (Pythonic Simulation)

Python achieves flexible initialization via:

- Default parameters  
- `*args` / `**kwargs`  
- Alternative constructors  

```python
class Vehicle:
    def __init__(self, model=None, color=None):
        self.model = model
        self.color = color
```

✔ Flexible object creation  
✔ Clean API design  

---

## 4️⃣ Encapsulation — Controlled State Management

Python uses naming conventions for access control.

| Level      | Syntax     | Behavior |
|------------|------------|----------|
| Public     | `name`     | Global access |
| Protected  | `_name`    | Internal convention |
| Private    | `__name`   | Name mangling applied |

---

### 🔐 Manual Getter & Setter

```python
class Student:
    def __init__(self):
        self.__id = None

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value
```

---

### ⭐ Property Decorators (Production Preferred)

```python
class Student:
    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Invalid marks")
        self.__marks = value
```

✔ Clean syntax  
✔ Inline validation  
✔ Backward compatible API  

---

## 5️⃣ Abstraction — Interface Enforcement

> Forces subclasses to implement required behaviors.

```python
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def greet(self):
        pass
```

### Concrete Implementation

```python
class Technical(Employee):

    def greet(self):
        print("IT Department")
```

✔ Prevents incomplete implementations  
✔ Ensures architectural discipline  

---

# 🛡 Exception Handling — Defensive Programming

---

## Custom Exception

```python
class AgeNotValid(Exception):
    pass
```

---

## Raising Exception

```python
if age < 18:
    raise AgeNotValid("Age must be >= 18")
```

---

## Handling Exception

```python
try:
    obj = Person(17)
except AgeNotValid as error:
    print(error)
```

✔ Domain-level validation  
✔ Controlled execution flow  
✔ Clean debugging  

---

# 🧩 Design Principles Reinforced

- DRY (Don't Repeat Yourself)  
- Liskov Substitution Principle  
- Encapsulation & Data Integrity  
- Runtime Polymorphism  
- Interface Enforcement via ABC  
- Structured Exception Handling  

---

# 🚀 Best Practices Checklist

✔ Use `super()` in inheritance chains  
✔ Prefer `@property` over manual getters  
✔ Keep constructors lightweight  
✔ Raise domain-specific exceptions  
✔ Enforce contracts using abstract base classes  
✔ Maintain consistent naming conventions  

---

# ⚙ Optional: Django Environment Setup

```bash
python -m venv venv
source venv/bin/activate
pip install django
django-admin startproject project
python manage.py runserver
```

---

<div align="center">

<img src="https://media.giphy.com/media/f3iwJFOVOwuy7K6FFw/giphy.gif" width="450"/>

## 🧠 If you understand everything here —
### Your Python OOP foundation is production-ready.

🚀 Keep Building. Keep Architecting. Keep Scaling.

</div>
