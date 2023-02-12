#!/usr/bin/python3
"""
the console module
"""
import cmd
from models.base_model import BaseModel
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    """A class for the command interprator"""

    prompt = "(hbnb) "

    __class = ["BaseModel"]

    def do_quit(self, line):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, line):
        """
        End Of File: EOF command used to exit the program
        """
        return True

    def emptyline(self):
        """
        A method empty line to don't excute anything
        """
        return

    def do_create(self, args):
        """create: Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """

        if len(args) == 0:
            print("** class name missing **")
            return

        elif args not in HBNBCommand.__class:
            print("** class doesn't exist **")
            return
        else:
            b_model = eval(args)()
            b_model.save()
            print(b_model.id)

    def do_show(self, args):
        """ Prints the string representation
        of an instance based on the class name and id
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        else:
            args = args.split()
            if len(args) == 1:
                print("** instance id missing **")

            class_name, object_id = args
            if class_name not in HBNBCommand.__class:
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, object_id)
                if key in HBNBCommand.__class:
                    print(key)
                else:
                    print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
