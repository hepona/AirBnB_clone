#!/usr/bin/python3
""" console of hBnB"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models import storage
from models.city import City
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """Encompasses console functionality."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_show(self, line):
        """Show the string representation of an instance
        Args: line ->  id Class In that order
        """
        class_object = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif class_object[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        elif len(class_object) == 1:
            print("** instance id missing **")
        else:
            key = class_object[0] + "." + class_object[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key]
                print(str(obj))

    def do_create(self, line):
        """new object Created"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.__class__.classes[line]()
            obj.save()
            print(obj.id)

    def do_update(self, line):
        """attributes of an object Updated"""
        updates = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif updates[0] not in __class__.classes.keys():
            print("** class doesn't exist **")
        elif len(updates) == 1:
            print("** instance id missing **")
        elif len(updates) == 2:
            print("** attribute name missing **")
        elif len(updates) == 3:
            print("** value missing **")
        else:
            key = updates[0] + "." + updates[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** instance id missing **")
            else:
                obj = all_instances[key]
                setattr(obj, updates[2], updates[3])
                storage.save()

    def do_destroy(self, args):
        """Name Class and ID based object destruction."""

        target_list = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        elif target_list[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(target_list) == 1:
            print("** instance id missing **")
            return
        else:
            key = target_list[0] + "." + target_list[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                del all_instances[key]
                storage.save()

    def do_all(self, line):
        """show string representation of all instances"""
        obj_list = []
        objs = storage.all()
        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        line.strip()
        for key, val in objs.items():
            if len(line) != 0:
                if type(val) is eval(line):
                    val = str(objs[key])
                    obj_list.append(val)
            else:
                val = str(objs[key])
                obj_list.append(val)
        print(obj_list)

    def emptyline(self):
        """Override default for last command repeat"""
        pass

    def do_operations(self, args):
        """Perform actions on objects"""

    def do_EOF(self, args):
        """Manages program exit on EOF"""
        print()
        return True

    def do_count(self, arg):
        """Count class instances"""
        to_count = arg.split(" ")
        instances = 0
        for obj_ in storage.all().values():
            if to_count[0] == type(obj_).__name__:
                instances += 1
        print(instances)

    def default(self, arg):
        """Commands"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        match_car = re.search(r"\.", arg)
        if match_car is not None:
            argl = [arg[: match_car.span()[0]], arg[match_car.span()[1]:]]
            match_car = re.search(r"\((.*?)\)", argl[1])
            if match_car is not None:
                command = [argl[1][: match_car.span()[0]],
                           match_car.group()[1:-1]]
                if command[0] in argdict.keys():
                    call_result = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call_result)
        print("*** Unknown syntax : {}".format(arg))
        return False

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
