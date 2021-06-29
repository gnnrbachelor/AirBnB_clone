#!/usr/bin/python3
"""console module"""

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for prompt"""

    __classes = [
    'BaseModel'
    ]
    prompt = '(hbnb) '

    def emptyline(self):
        """Deal with empty line"""
        pass

    def do_EOF(self, arg):
        """Exit the console"""
        return True

    def do_quit(self, arg):
        """Quit command"""
        return True

    def do_create(self, arg):
        """Create instance of BaseModel"""
        cmd = self.parseline(arg)[0]
        if cmd is None:
            print("** class name missing **")
        elif cmd not in self.__classes:
            print("** Class doesn't exist **")
        else:
            new_inst = eval(cmd)()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """Prints string rep"""
        arguments = shlex.split(arg)
        dictionary = storage.all()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in dictionary:
            print("** no instance found **")
        else:
            print(dictionary["{}.{}".format(arguments[0], arguments[1])])

    def do_destroy(self, arg):
        """Destroys instance"""
        cmd = self.parseline(arg)[0]
        argument = self.parseline(arg)[1]
        if cmd is None:
            print("** Class name missing **")
        elif cmd not in self.__classes:
            print("** class doesn't exist **")
        elif argument == '':
            print("** instance id missing **")
        else:
            index = cmd + '.' + argument
            instance = models.storage.all().get(index)
            if instance is None:
                print("** no instance found **")
            else:
                del models.storage.all()[index]
                models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
