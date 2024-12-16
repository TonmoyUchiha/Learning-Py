# Learning Python

Here I am going to discuss some design issues with Py and elaborate on the basics using code and their output.

**Primitive Data Types**

Primitive Data Types are the components that make or break a function. There are different kind of data types:
![image](https://github.com/user-attachments/assets/70837009-4c3b-4b59-863d-302e3a200793)
Output:
![image](https://github.com/user-attachments/assets/4179bfd3-15b8-4a3c-a3ba-30f601f4a45e)

**Character String Types**

Using Py, we can do various operations using String (as there is no char data type in Py). Such as finding out it's length and concatenate.
![image](https://github.com/user-attachments/assets/c3eb2d33-0e8e-40af-ab9e-d2ed6b8a9167)
Output:
![image](https://github.com/user-attachments/assets/bd2f6066-e859-4a5f-b647-dd630994aebe)

**Enumeration**
Enumeration is a module we import in Py to bind unique values to different names/string. Almost like putting dates of calendar on weekdays.
There are some design issues using enum:
>Enum members are immutable once defined
>Enums are classes, which means accessing enum members can be slower compared to using simple constants or integers.
>Python's enums do not support multiple inheritance.
>Enum members are designed to be compared by identity, not by value.

![image](https://github.com/user-attachments/assets/f4745674-eabb-4715-9f64-45080ed1f392)
Output:
![image](https://github.com/user-attachments/assets/d65636ab-352e-4df3-bff3-4868b161f533)

**Array Types**
Array is a data storing module that let's us store multiple values in one variable. **Array is not the same as List** (**We mainly use list in Py**)
But there are some issues:
>Array module provides limited functionality for data manipulation. Simply result=Arr1+Arr2 is not possible.
>Array lacks many useful built-in methods for operations like sorting, reversing, or counting elements.
![image](https://github.com/user-attachments/assets/63570439-4e87-4f20-9e81-33a1e80fbe47)
Output:
![image](https://github.com/user-attachments/assets/c08e3c4b-6cd0-4743-af3d-c9b06421b1c3)

**Record Types**
Record types are data structures used to store fields or attributes in a structured manner.
Issues:
>Some record types (e.g., named tuples) are immutable by design, while others (e.g., data classes) are mutable by default.
>While dataclass and named tuples reduce boilerplate compared to regular classes, they still require some boilerplate to define attributes.
>May require custom serialization logic.
![image](https://github.com/user-attachments/assets/494c5303-ffd4-48e8-b24b-666872ea6e97)
Output:
![image](https://github.com/user-attachments/assets/ded72c13-f54f-4212-8a60-d094176efb89)

**Union Types**
Union types are used to store multiple types of data in one variable.
Issues:
>Allowing multiple types for a single variable can lead to ambiguity and complexity, making it harder to understand or predict how the code behaves.
>Union types can be misused to cover too many types, leading to poor design practices or "catch-all" type hints.
![image](https://github.com/user-attachments/assets/2763b83f-7ffe-4d84-b706-6ae42100a7ed)
Output:
![image](https://github.com/user-attachments/assets/33bcbb8e-3c47-482a-b6ae-b054a94ba086)

**Pointers**
Pointers are variables that store the memory address of another variable. I have used C++ for this example.
Issues:
>A dangling pointer occurs when a pointer still refers to a memory location that has been deallocated or goes out of scope.
>Dereferencing a null pointer (a pointer that doesn’t point to a valid memory location) leads to crashes or undefined behavior.
>Pointers are a common source of security vulnerabilities, such as buffer overflows and memory corruption.
>Double free occurs when memory is freed more than once, which can corrupt the memory management system.
![image](https://github.com/user-attachments/assets/516a9780-3d7c-41f3-ae90-6cf5917bee43)
Output:
![image](https://github.com/user-attachments/assets/2547e896-5c51-4fdf-9d71-3d69c23fbd8d)



