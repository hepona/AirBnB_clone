0x00. AirBnB clone - The console
================================
![Alt text](image.png)

Group projectPythonOOP

*   By: Guillaume
*   Weight: 5
*   Project to be done in teams of 2 people (your team: soufiane ruiq, Hiba Rahif)
*   Project will start Aug 7, 2023 4:00 AM, must end by Aug 14, 2023 4:00 AM
*   Checker will be released at Aug 12, 2023 10:00 AM
*   **Manual QA review must be done** (request it when you are done with the project)
*   An auto review will be launched at the deadline

### Concepts

_For this project, we expect you to look at these concepts:_

*   [Python packages](https://intranet.alxswe.com/concepts/66)
*   [AirBnB clone](https://intranet.alxswe.com/concepts/74)

![](./Project_ 0x00. AirBnB clone - The console _ ALX Africa Intranet_files/65f4a1dd9c51265f49d0.png)

Background Context
------------------

### Welcome to the AirBnB clone project!

Before starting, please read the **AirBnB** concept page.

#### First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

*   put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
*   create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
*   create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
*   create the first abstracted storage engine of the project: File storage.
*   create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

*   Create a new object (ex: a new User or a new Place)
*   Retrieve an object from a file, a database etc…
*   Do operations on objects (count, compute stats, etc…)
*   Update attributes of an object
*   Destroy an object

Resources
---------

**Read or watch**:

*   [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A "cmd module")
*   [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg "cmd module in depth")
*   **packages** concept page
*   [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ "uuid module")
*   [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA "datetime")
*   [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA "unittest module")
*   [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng "args/kwargs")
*   [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw "Python test cheatsheet")
*   [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ "cmd module wiki page")
*   [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA "python unittest")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/uV5eZkRZ_XEqYbgPd-0CWw "explain to anyone"), **without the help of Google**:

### General

*   How to create a Python package
*   How to create a command interpreter in Python using the `cmd` module
*   What is Unit testing and how to implement it in a large project
*   How to serialize and deserialize a Class
*   How to write and read a JSON file
*   How to manage `datetime`
*   What is an `UUID`
*   What is `*args` and how to use it
*   What is `**kwargs` and how to use it
*   How to handle named arguments in a function

### Copyright - Plagiarism

*   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
*   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
*   You are not allowed to publish any content of this project.
*   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### Python Scripts

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version `2.8.*`)
*   All your files must be executable
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files should end with a new line
*   All your test files should be inside a folder `tests`
*   You have to use the [unittest module](https://intranet.alxswe.com/rltoken/op1-rQGlw0wwwqNBsn1yaw "unittest module")
*   All your test files should be python files (extension: `.py`)
*   All your test files and folders should start by `test_`
*   Your file organization in the tests folder should be the same as your project
*   e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
*   e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
*   All your tests should be executed by using this command: `python3 -m unittest discover tests`
*   You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### GitHub

**There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.**

More Info
---------

### Execution

Your shell should work like this in interactive mode:

    $ ./console.py
    (hbnb) help
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    
    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $
    

But also in non-interactive mode: (like the Shell project in C)

    $ echo "help" | ./console.py
    (hbnb)
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
    

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

![](./Project_ 0x00. AirBnB clone - The console _ ALX Africa Intranet_files/815046647d23428a14ca.png)

### Video library(8 total)

HBNB project overview

HBNB - the console

Python: Unique Identifier

Python: Unittests

Python: BaseModel and inheritance

Code consistency

Python: Modules and Packages

HBNB - storage abstraction

Tasks
-----

### 0\. README, AUTHORS

mandatory

*   Write a `README.md`:
    *   description of the project
    *   description of the command interpreter:
        *   how to start it
        *   how to use it
        *   examples
*   You should have an `AUTHORS` file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference [Docker’s AUTHORS page](https://intranet.alxswe.com/rltoken/_8n_z3pf5HWi1l7uv1E9iA "Docker's AUTHORS page")
*   You should use branches and pull requests on GitHub - it will help you as team to organize your work

**Repo:**

*   GitHub repository: `AirBnB_clone`
*   File: `README.md, AUTHORS`

Done?! Help

×

#### Learners who are done with "0. README, AUTHORS"

### 1\. Be pycodestyle compliant!
### 2\. Unittests

### 3\. BaseModel
### 4\. Create BaseModel from dictionary

### 5\. Store first object

### 6\. Console 0.0.1

### 7\. Console 0.1

### 8\. First User


### 9\. More classes!

### 10\. Console 1.0