#!/usr/bin/python3
"""Console module for HolbertonBnB command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel 
from models.user import User 
from models.place import Place 
from models.state import State 
from models.city import City 
from models.amenity import Amenity 
from models.review import Review

classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""
    prompt = '(hbnb) '


    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def help_quit(self):
        """Print help message for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Print help message for EOF command."""
        print("EOF signal to exit the program")
        
    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it (to the JSON file) and prints the id."""

        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return

        new_instance = classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0: 
            print("** class name missing **") 
            return 
        if args[0] not in classes: 
            print("** class doesn't exist **") 
            return 
        if len(args) == 1: 
            print("** instance id missing **") 
            return 
        key = f"{args[0]}.{args[1]}" 
        all_objects = storage.all() 
        if key not in all_objects: 
            print("** no instance found **") 
            return 
        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split() 
        if len(args) == 0: 
            print("** class name missing **") 
            return 
        if args[0] not in classes: 
            print("** class doesn't exist **") 
            return 
        if len(args) == 1: 
            print("** instance id missing **") 
            return 
        key = f"{args[0]}.{args[1]}" 
        all_objects = storage.all() 
        if key not in all_objects: 
            print("** no instance found **") 
            return 
        del all_objects[key] 
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = arg.split()
        all_objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objects.values()])
        else:
            class_name = args[0]
            filtered_objects = [str(obj) for key, obj in all_objects.items() if key.startswith(class_name + ".")]
            print(filtered_objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) == 0: 
            print("** class name missing **") 
            return 
        if args[0] not in classes: 
            print("** class doesn't exist **") 
            return 
        if len(args) == 1: 
            print("** instance id missing **") 
            return 
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        class_name, instance_id, attr_name, attr_value = args[0], args[1], args[2], args[3]
        all_objects = storage.all()
        key = f"{class_name}.{instance_id}"
        if key in all_objects:
            instance = all_objects[key]
            try:
                attr_value = eval(attr_value)
            except:
                pass
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** no instance found **")

                                            
            

    
if __name__ == "__main__":
    HBNBCommand().cmdloop()

