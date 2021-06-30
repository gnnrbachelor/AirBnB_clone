#!/usr/bin/python3
"""console module"""

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for prompt"""

    __classes = ['BaseModel', 'User', 'State',
                 'City', 'Amenity', 'Place', 'Review']
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
            print("** class doesn't exist **")
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
            print("** class name missing **")
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

    def do_all(self, arg):
        """String rep of all"""
        cmds = shlex.split(arg)
        objs = []
        if len(cmds) == 0:
            for value in models.storage.all().values():
                objs.append(str(value))
            print("[", end="")
            print(", ".join(objs), end="")
            print("]")
        elif cmds[0] in self.__classes:
            for key in models.storage.all():
                if cmds[0] in key:
                    objs.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(objs), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates instance"""
        if not arg:
            print("** class name missing **")
        else:
            cmd = arg.split()
            if (cmd[0] in self.__classes):
                if (len(cmd) < 2):
                    print("** instance id missing **")
                    return
                key_ch = str(cmd[0] + "." + str(cmd[1]))
                if key_ch not in storage.all().keys():
                    print("** no instance found **")
                    return
                elif (len(cmd) < 3):
                    print("** attribute name missing **")
                    return
                elif (len(cmd) < 4):
                    print("** value missing **")
                    return
                else:
                    objs = storage.all()
                    for key in objs.keys():
                        if (key_ch == key):
                            temp = objs[key]
                            try:
                                cmd[3] = cmd[3].strip('"')
                                cmd[3] = int(cmd[3])
                            except:
                                pass
                            setattr(temp, cmd[2], cmd[3])
                            storage.save()
                            flag = 1
                    if (flag == 0):
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
