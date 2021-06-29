#!/usr/bin/python3
"""console module"""

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
import shlex

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for prompt"""
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
