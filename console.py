#!/usr/bin/python3
"""
the console module
"""

import cmd
import shlex
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place",
               "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """method for close and exit from the console"""

        return True

    def do_EOF(self, arg):
        """method for exit from the console"""
        print()
        exit()

    def do_create(self, arg):
        """method for create a new object
        """

        if len(arg) < 1:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Method for show a specific object wiht the id option
        """

        data = arg.split()
        my_list = []
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                my_list.append("[{}] ({}) {}".format(data[0],
                               data[1], storage.all()[key]))
                print(my_list)

    def do_destroy(self, arg):
        """Method for delete a object
        """

        data = arg.split()
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
                storage.save()

    def do_all(self, arg):
        """Method for listed all abjects in a list
        """

        data = shlex.split(arg)
        my_list = []
        if len(arg) < 1:
            for key, value in storage.all().items():
                c_name, c_id = key.split(".")
                my_list.append("{}".format(value))
            print(my_list)
        else:
            if not data[0] in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    c_name, c_id = key.split(".")
                    if c_name == data[0]:
                        my_list.append("{}".format(value))
                print(my_list)

    def do_update(self, arg):
        """Updates and instance"""

        data = shlex.split(arg)
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(data) < 3:
                print("** attribute name missing **")
            elif len(data) < 4:
                print("** value missing **")
            else:
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all().get(key)
                    setattr(obj, data[2], data[3])
                    storage.save()

    def emptyline(self):
        """empty line"""

        pass

    def default(self, arg):
        """Takes the default input and process it"""
        my_methods = {"all": self.do_all, "destroy": self.do_destroy,
                      "update": self.do_update, "show": self.do_show}
        data = arg.split(".")
        if len(data) < 2:
            print("** missing arguments **")
        else:
            key = data[1]
            if data[1] == "count()" and data[0] in HBNBCommand.classes:
                count = 0
                for key in storage.all().keys():
                    clas = key.split('.')
                    if clas[0] == data[0]:
                        count += 1
                print(count)
            else:
                if key[-2:] != "()":
                    print("** invalid command **")
                elif key[:-2] not in my_methods:
                    print("** method does not exist **")
                elif key[:-2] in my_methods:
                    my_methods[key[:-2]](data[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
