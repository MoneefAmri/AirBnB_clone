#!/usr/bin/python3
"""This is the Console module."""
import cmd

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB project.
    """

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
        "User": User,
    }

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a class, save it to the JSON file, and print the id.

        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance based on the class name and id.

        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id (save the change into the JSON file).

        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key in objects:
            del objects[key]
            BaseModel().save()
        else:
            print("** noinstance found **")

    def do_all(self, arg):
        """
        Print all string representations of instances based on the class name.

        Usage: all <class name> or all
        """
        args = arg.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objects.values() if type(obj).__name__ == class_name])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or updating an attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key in objects:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attr_value = args[3]
            setattr(objects[key], attr_name, attr_value)
            objects[key].save()
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
