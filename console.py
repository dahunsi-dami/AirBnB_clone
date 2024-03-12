#!/usr/bin/python3
"""Entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The command processor's model."""

    prompt = '(hbnb) '
    model_coll = ["BaseModel", "User", "State", "City", "Amenity",
                  "Place", "Review"]

    def do_EOF(self, line):
        """Command to exit interpreter when EOF is encountered."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Override default emptyline() to do nothing."""
        return

    def do_create(self, line):
        """Creates instance of BaseModel, saves to JSON, prints id."""
        if line in self.model_coll:
            cinst = BaseModel()
            scinst = cinst.save()
            print(cinst.id)
        elif line == "":
            print(f"** class name missing **")
        else:
            print(f"** class doesn't exist **")

    def do_show(self, line):
        """prints str rep of instance, <class name> <id>."""
        args = line.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print(f"** class name missing **")
        elif args[0] not in self.model_coll:
            print(f"** class doesn't exist **")
        elif len(args) == 1:
            print(f"** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print(f"** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """deletes instance based on class name and id."""
        args = line.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print(f"** class name missing **")
        elif args[0] not in self.model_coll:
            print(f"** class doesn't exist **")
        elif len(args) == 1:
            print(f"** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print(f"** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, line):
        """prints all str rep of instances w/ class name."""
        list_obj = []
        for v in storage.all().values():
            list_obj.append(str(v))
        if len(line) == 0:
            print("{}".format(list_obj))
        elif line not in self.model_coll:
            print(f"** class doesn't exist **")
        else:
            coll_obj = storage.all()
            list_obj = [str(v) for k, v in coll_obj.items()
                        if "BaseModel" == v.__class__.__name__]
            print(list_obj)

    def do_update(self, line):
        """updates instance based on class name & id."""
        args = line.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print(f"** class name missing **")
        elif args[0] not in self.model_coll:
            print(f"** class doesn't exist **")
        elif len(args) == 1:
            print(f"** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print(f"** no instance found **")
        elif len(args) == 2:
            print(f"** attribute name missing **")
        elif len(args) == 3:
            print(f"** value missing **")
        else:
            attrib = args[2]
            valoo = str(args[3])
            vlen = len(valoo)
            alen = len(attrib)
            if valoo[0] == "\"" or valoo[vlen - 1] == "\'":
                valoo = valoo[1:vlen-1]
            if attrib[0] == "\"" or attrib[alen - 1] == "\'":
                attrib = attrib[1:alen-1]
            obj_mod = storage.all()["{}.{}".format(args[0], args[1])]
            setattr(obj_mod, attrib, valoo)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
