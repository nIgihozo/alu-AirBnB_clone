#!/usr/bin/python3
"""Entry point of the AirBnB command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""

    # Custom prompt
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program (Ctrl+D)"""
        print()  # ensures a clean newline when exiting
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

