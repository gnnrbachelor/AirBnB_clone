#!/usr/bin/python3
"""
Module for BaseModel class
"""


from datetime import datetime
import models
import uuid


class BaseModel:
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """
        Init method setting default values
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date_obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, date_obj)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """String representation"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """updates current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary"""
        new_dictionary = self.__dict__.copy()
        new_dictionary['created_at'] = datetime.isoformat(new_dictionary[
                                       'created_at'])
        new_dictionary['updated_at'] = datetime.isoformat(new_dictionary[
                                       'updated_at'])
        new_dictionary["__class__"] = self.__class__.__name__
        return new_dictionary
