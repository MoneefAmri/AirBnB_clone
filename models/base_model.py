#!/usr/bin/python3
""" This is the Base Model module."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for other models, defines common attributes and methods.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Datetime when the instance is created.
        updated_at (datetime): Datetime when the instance is last updated.

    Methods:
        __str__(): Returns a string representation of the object.
        save(): Updates the updated_at attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the object.
    """
    D_F = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the current class.

        Args:
            *args: Unused.
            **kwargs: (optional) dictionary of attribute values to
                      initialize the instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k in ("created_at", "updated_at"):
                    self.__dict__[k] = datetime.strptime(v, self.D_F)
                elif k != "__class__":
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the object.
        It prints the class name, id,
        and the dictionary representation of the object's attributes.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary with all keys and values of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
