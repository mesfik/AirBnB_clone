#!/usr/bin/python3
"""
the console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A class for the command interprator"""

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
