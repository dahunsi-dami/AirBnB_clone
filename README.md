# AirBnB Clone - The console
(https://github.com/eveshogweyore/AirBnB_clone/blob/main/airbnb_clone_pic.png)
## Project Description

This is our first full web application: a clone of the AirBnB website (at https://www.airbnb.com).

It serves as the base for other projects in the ALX-Holberton Software Engineering program: HTML/CSS templating, database storage, API, front-end integration, etc.

We built/performed the following tools/tasks:
- a command interpreter (aka., console)
- a BaseModel
- modules and packages
- file storage abstractions
- unit tests

## Command Interpreter Description

Our command interpreter does the following:
- create a new object (e.g., new User or Place)
- retrive an object from a file/database storage
- do operations on objects (e.g., count, statistics, etc.)
- update instance attributes
- destroy object(s)

### How To Start The Command Interpreter

Console can be started with ```./console.py```

### How To Use The Console

Run command ```help``` to see available commands.

Console can be used interactively or non-interactively.

### Examples

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

```
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
```

## Classes

This project has the following classes:

| Attributes                 | BaseModel                                              |
| ----------------------|---------------------------------------------------------------|
| `public instance`   | id   |
