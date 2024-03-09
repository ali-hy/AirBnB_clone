#!/usr/bin/python3
'''This file starts and manages the console for hbnb
it's the entrypoint to the application'''
import cmd
import sys
import shlex
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models import storage


Classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Reviw': Review
}


class HBNBCommand(cmd.Cmd):
    '''Class for a command interpreter for the hbnb app'''

    def __init__(self,
                 completekey="tab",
                 stdin=None,
                 stdout=None) -> None:
        '''Constructor of the commandline interpreter'''
        super().__init__(completekey, stdin, stdout)
        if sys.stdin.isatty():
            self.prompt = '(hbnb) '
        else:
            self.prompt = ''

    def do_quit(self, s):
        '''function to run on `quit` command
        exits command interpreter'''
        return 1

    def help_quit(self):
        '''provide user with details about the quit command'''
        print('Quit command to exit the program\n')

    def do_EOF(self, s):
        '''function to run on `EOF` command
        exits command interpreter'''
        return 1

    def help_EOF(self, s):
        '''provide user with details about the EOF command'''
        print('Quit command to exit the program\n')

    def do_create(self, s):
        '''function to run on 'create' command'''
        args = s.split()
        if args == 0:
            print('** class name missing **')
            return
        classname = args[0]
        if classname not in Classes:
            print("** class doesn't exist **")
            return
        newobj = Classes[classname]()
        print(newobj.id)
        newobj.save()

    def help_create(self):
        '''provide user with details about the create command'''
        print('takes a classname and creates an object of that class')

    def do_show(self, s):
        '''function to run on 'show' command'''
        args = s.split()
        if len(s) == 0:
            print('** class name missing **')
            return
        classname = args[0]
        if classname not in Classes:
            print("** class doesn't exist **")
            return
        if len(s) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj = storage.get(classname, instance_id)
        if obj:
            print(obj)
        else:
            print('** no instance found **')

    def help_show(self):
        '''provide user with details about the help command'''
        print('show <classname> <instance_id>: show details of object with ' +
              'specified classname and id')

    def do_destroy(self, s):
        '''function to run on 'destroy' command'''
        args = s.split()
        if len(s) == 0:
            print('** class name missing **')
            return
        classname = args[0]
        if classname not in Classes:
            print("** class doesn't exist **")
            return
        if len(s) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        success = storage.delete(classname, instance_id)
        if success:
            storage.save()
        else:
            print('** no instance found **')

    def help_destroy(self):
        '''provide user with details about the destroy command'''
        print('destroy <classname> <instance_id>: delete object with ' +
              'specified classname and id')

    def do_all(self, s):
        '''function to call on 'all' command'''
        args = s.split()
        if len(args) == 0:
            classname = None
        else:
            classname = args[0]
            if classname not in Classes:
                print("** class doesn't exist **")
                return
        res = []
        if classname:
            for obj in storage.all().values():
                if obj.__class__.__name__ == classname:
                    res.append(str(obj))
        else:
            for obj in storage.all().values():
                res.append(str(obj))
        print(res)

    def help_all(self):
        '''provide user with details about the all command'''
        print('show all stored objects. If a classname is specified, only' +
              ' objects with that classname will be displayed')

    def do_update(self, s: str):
        '''function to call on 'update' command'''
        args = shlex.split(s)
        if len(args) == 0:
            print('** class name missing **')
            return
        if args[0] not in Classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj = storage.get(args[0], args[1])
        if not obj:
            print('** no instance found **')
            return
        if len(args) == 2:
            print('** attribute name missing **')
            return
        if len(args) == 3:
            print('** value missing **')
            return
        attr = args[2]
        val = args[3]
        curr_type = type(getattr(obj, attr))
        if curr_type == list:
            new_val = eval(val)
        else:
            new_val = curr_type(val)
        setattr(obj, attr, new_val)
        obj.save()

    def emptyline(self) -> bool:
        '''do nothing when an empty line is entered'''
        pass

    def precmd(self, line: str) -> str:
        '''process input before command runs'''
        tmp = line.split('.')
        if len(tmp) < 1 or tmp[0] not in Classes:
            return line

        # handle: Class.cmd(<arg1>, <arg2>, ..., <argn>)
        classname = tmp[0]

        argstart, argend = tmp[1].find('('), tmp[1].find(')')
        if argstart == -1 or argend == -1 or argend < argstart:
            return line
        command = tmp[1][0:argstart]

        arglist = list()
        args = tmp[1][argstart+1:argend]

        if len(args) > 0:
            start = 0
            end = 0
            while True:
                if start >= len(args):
                    return line
                end = args.find(',', start)
                if end == -1:
                    arg = args[start:].strip()
                    if len(arg) == 0:
                        return line
                    arglist.append(arg)
                    break

                arglist.append(args[start: end].strip())
                start = end + 1

        return f"{command} {classname} {' '.join(arglist)}"


if __name__ == '__main__':
    HBNBCommand().cmdloop()
