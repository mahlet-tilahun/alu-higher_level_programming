#!/usr/bin/python3
"""
This module defines a Base class that serves as the foundation
for other classes in the project.

"""
import json
import csv


class Base:
    """
    Base class for managing id attribute in all future
    classes and to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        """

        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string
        representation.
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        with open("{}.json".format(cls.__name__), "w") as file:
            if list_objs:
                obList = [i.to_dictionary() for i in list_objs]
                file.write(cls.to_json_string(obList))
            else:
                file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a Python object.
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class with the provided
        dictionary.
        """
        if cls.__name__ == "Rectangle":
            newIns = cls(1, 1)
        elif cls.__name__ == "Square":
            newIns = cls(1)

        newIns.update(**dictionary)
        return newIns

    @classmethod
    def load_from_file(cls):
        """
        Reads a JSON file and returns a list of instances of the class.
        """
        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                jsonData = file.read()
                dictList = cls.from_json_string(jsonData)
                insList = [cls.create(**i) for i in dictList]
                return insList
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV string representation of list_objs to a file.
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline='') as csvfile:
            if list_objs:
                writer = csv.writer(csvfile)
                if cls.__name__ == "Rectangle":
                    writer.writerow(["id", "width", "height", "x", "y"])
                    for obj in list_objs:
                        writer.writerow([
                            obj.id,
                            obj.width,
                            obj.height,
                            obj.x,
                            obj.y
                        ])
                elif cls.__name__ == "Square":
                    writer.writerow(["id", "size", "x", "y"])
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])
            else:
                csvfile.write("")

    @classmethod
    def load_from_file_csv(cls):
        """
        Reads a CSV file and returns a list of instances of the class.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                dict_list = [dict(row) for row in reader]
                for d in dict_list:
                    for key in d:
                        d[key] = int(d[key])
                return [cls.create(**d) for d in dict_list]
        except Exception:
            return []
