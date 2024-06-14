Day 3: Understanding Inheritance in Python
Overview
Day 3 focused on the concept of inheritance in Python, including its necessity, the concept of single inheritance, and the behavior when a constructor is present only in the base class.
Topics Covered
Concept of Inheritance
Inheritance is a fundamental principle in object-oriented programming that allows a class (derived class) to inherit attributes and methods from another class (base class). This promotes code reusability and hierarchical class organization.
Why We Need Inheritance
Inheritance is essential because it enables the creation of a new class that is a modified or extended version of an existing class. This reduces code duplication and enhances maintainability. By inheriting from a base class, derived classes can leverage existing code and introduce new functionality.
Concept of Single Inheritance
Single inheritance refers to a derived class inheriting from a single base class. This is the simplest form of inheritance and is used to extend the functionality of the base class without affecting other classes.
Constructor in Base Class
When a constructor is present only in the base class, the derived class inherits this constructor. Upon creating an instance of the derived class, the base class's constructor is automatically called, initializing the base class's attributes. This demonstrates how the base class can handle common initialization tasks, ensuring that derived classes start with a well-defined state.
