# AirBnB Clone – The Console
## Project Overview
The AirBnB Clone Project is the foundation of a larger full‑stack application that replicates the core functionality of the Airbnb platform.
This first milestone focuses on building a command interpreter in Python, which acts as the entry point to manage the backend objects of the system.

The interpreter is built using Python’s cmd module and provides a shell‑like interface where developers can create, update, retrieve, and delete objects. All data is persisted in a JSON file, ensuring that objects remain available across sessions.

###  Command Interpreter Description
The console behaves similarly to a Unix shell but is limited to commands defined specifically for the AirBnB project.
It serves as the frontend for developers, allowing interaction with the backend models and storage engine.

#### Core Capabilities
- Create new objects (e.g., User, Place, City, Review)

- Show details of an object using its class name and ID

- Update attributes of existing objects

- Destroy objects and persist changes

- Count the number of instances of a given class

- List all objects or filter by class

### Installation
Clone this repository:

bash
git clone https://github.com/nIgihozo/alu-AirBnB_clone.git
cd alu-AirBnB_clone
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.
#### Key files and directories:

- console.py → Main executable, the command interpreter

- models/base_model.py → Base class with common attributes and methods

- models/engine/file_storage.py → Handles JSON serialization and deserialization

- models/user.py → User class inheriting from BaseModel

- models/state.py, models/city.py, models/place.py, models/amenity.py, models/review.py → Domain models for the application
- tests/ → Unit tests for all modules

### How to Use
It will work in two differentmodes which are **Interactive Mode**, and **Non-Interactive Mode**
#### Interactive Mode

In this  mode, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, 
the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

Run the console directly:

bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) quit
$
#### Non‑Interactive Mode

In this mode, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. 
Another thing is there is  no prompt will appear, and no further input will be expected from the user in this mode.

Pipe commands into the console:

bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

### Commands Reference
Commands and what they do:

| Command     | Description                                      | Usage                                                  |
|-------------|--------------------------------------------------|--------------------------------------------------------|
| `quit` / `EOF` | Exit the program                                | `quit` or `CTRL+D`                                     |
| `help`      | Show available commands or details about one     | `help` or `help <command>`                             |
| `create`    | Create a new instance and save it                | `create <class name>`                                  |
| `show`      | Display an instance by class name and ID         | `show <class name> <id>`                               |
| `destroy`   | Delete an instance by class name and ID          | `destroy <class name> <id>`                            |
| `all`       | List all instances, optionally filtered by class | `all` or `all <class name>`                            |
| `update`    | Update attributes of an instance                 | `update <class name> <id> <attr name> "<value>"`       |
| `count`     | Return the number of instances of a class        | `<class name>.count()`                                 |

### Authors
See the **'AUTHORS'** file for the list of contributors.
