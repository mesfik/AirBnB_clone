#!/usr/bin/python3
"""
the console module
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review

import sys


class HBNBCommand(cmd.Cmd):
    """A class for the command interprator"""

    prompt = "(hbnb) "

    __class = {"BaseModel": BaseModel, "User": User,
               "Amenity": Amenity, "City": City,
               "State": State, "Place": Place, "Review": Review}

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
        args = args.split()

        if args[0] not in HBNBCommand.__class:
            print("** class doesn't exist **")
            return
        
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key in HBNBCommand.__class:

            print(HBNBCommand.__class[key])

        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()

        if args[0] not in HBNBCommand.__class:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key in HBNBCommand.__class:

            del HBNBCommand.__class[key]
            models.save()

        else:
            print("** no instance found **")

    def do_all(self, arg):
        """all: Prints all string representation
        of all instances based or not on the class name.
        """
        objects = []
        if not arg:
            for obj in storage.all().values():
                objects.append(str(obj))
        elif arg in HBNBCommand.__class:
            for obj in storage.all().values():
                if type(obj).__name__ == arg:
                    objects.append(str(obj))
        else:
            print("** class doesn't exist **")
            return

        if objects:
            print("[{}]".format(", ".join(objects)))
        else:
            print("[]")

    def do_update(self, args):
        """update: Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in HBNBCommand.__class:
            print("** class doesn't exist **")
            return

        elif len(args) == 1:
            print("** instance id missing **")
            return

        else:

            key = "{}.{}".format(args[0], args[1])
            
            if key not in storage.all():
                print("** no instance found **")
                return
            elif len(key) < 3:
                print("** attribute name missing **")
                return

            elif len(obj) < 4:
                print("** value missing **")
                return

            else:
                 obj = storage.all().get(key)
                 value = eval(args[3])
                 setattr(obj, args[2], value)
                 odels.save()




if __name__ == '__main__':
    HBNBCommand().cmdloop()
