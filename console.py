#!/usr/bin/python3
"""
Class that defines HBNBCommand
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine import file_storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        Class that defines HBNBCommand, defines the prompt and the methods
        to create, update, show and delete instances.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Exits the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program
        """
        return True

    def emptyline(self):
        """
        Executes nothing
        """
        pass

    def check_for_class(self, args):
        """
            Evaluate if the given arguments are valid
            and the class exists
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        else:
            try:
                check = eval("{}()".format(args[0]))
                dict = storage.all()
                del dict[args[0] + "." + check.id]
                return True
            except:
                print("** class doesn't exist **")
                return False

    def check_for_id(self, args):
        """
            Evaluate if the given arguments are valid and instance id
            is present to set or update.
        """
        if len(args) < 2:
            print("** instance id missing **")
            return False

        key = args[0] + "." + args[1]
        if key in storage.all():
            return True
        else:
            print("** no instance found **")
            return False

    def check_for_attribute(self, args):
        """
            Evaluate if the given arguments are valid and
            attribute name and value are present to set or update.
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        elif len(args) < 4:
            print("** value missing **")
            return False
        elif args[3] in ['id', 'updated_at', 'created_at']:
            return False
        else:
            return True

    def do_create(self, args):
        """
            If arguments are valid create a new instance according to
            given values.
        """
        className = args.split()
        if self.check_for_class(className):
            new_instance = eval("{}()".format(className[0]))
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
            If arguments are valid prints an specific instance according to
            given values.
        """
        class_id = arg.split()
        if self.check_for_class(class_id) and self.check_for_id(class_id):
            dict = storage.all()
            print("{}".format(dict[class_id[0] + "." + class_id[1]]))

    def do_destroy(self, args):
        """
            If arguments are valid delete an specific instance according to
            given values and update the json file
        """
        class_id = args.split()
        if self.check_for_class(class_id) and self.check_for_id(class_id):
            dict = storage.all()
            del dict[class_id[0] + "." + class_id[1]]
            storage.save()

    def do_all(self, args):
        """
            If arguments are valid prints an specific class or all classes
            according to given values.
        """
        newlist = []
        args_sp = args.split()
        for key, value in storage.all().items():
            className = key.split(".")
            if len(args) == 0:
                newlist.append(value.__str__())
            elif className[0] == args_sp[0]:
                newlist.append(value.__str__())
        if bool(newlist) is False:
            print("** class doesn't exist **")
        else:
            print(newlist)

    def do_update(self, args):
        """
            If arguments are valid create or update an attribute value
            in a specific instance according to given values.
        """
        args_sp = args.split()
        if (self.check_for_class(args_sp) and self.check_for_id(args_sp) and
                self.check_for_attribute(args_sp)):
            for i in range(len(args_sp)):
                args_sp[i] = args_sp[i].strip('"')
            class_id = args_sp[0] + "." + args_sp[1]
            attribute = args_sp[2]
            upd_instance = storage.all().get(class_id)
            try:
                upd_attr = getattr(upd_instance, attribute)
            except:
                upd_attr = ""
            type_attr = type(upd_attr)
            setattr(upd_instance, attribute, type_attr(args_sp[3]))
            upd_instance.save()

    def do_count(self, arg):
        """
            If arguments are valid counts the number of instances for a
            given class
        """
        counter = 0
        args_sp = arg.split()
        for key, value in storage.all().items():
            className = key.split(".")
            if len(arg) == 0:
                return
            elif className[0] == args_sp[0]:
                counter = counter + 1
        print(counter)

    def default(self, args):
        """
            If arguments are valid executes one of the commands built
            for the console
        """

        dict_methods = {
            'create': self.do_create,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'all': self.do_all,
            'update': self.do_update,
            'count': self.do_count
        }

        parameters = (args.replace("(", ".").replace(
            ")", ".").replace('"', "").replace(",", ""))
        parameters = parameters.split(".")
        if parameters[1] in dict_methods.keys():
            if len(parameters) > 2:
                method_exec = dict_methods[parameters[1]]
                class_id = parameters[0] + " " + parameters[2]
                method_exec(class_id)
            else:
                print("*** Unknown syntax:", args[0])
        else:
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    