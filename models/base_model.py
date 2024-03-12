#!/usr/bin/python3
"""The base class `BaseModel`."""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """Defines common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes public instance attributes."""

        if len(kwargs) != 0:
            if "__class__" in kwargs:
                del kwargs["__class__"]

            for k, v in kwargs.items():
                if k in ["updated_at", "created_at"]:
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Add new instance to __object

    def __str__(self):
        """Modifies custom string representation an object."""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates `updated_at` with current datetime."""

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns dict with keys and values of instance attribute."""

        cp_dict = self.__dict__.copy()
        cp_dict["__class__"] = self.__class__.__name__
        cp_dict["created_at"] = self.created_at.isoformat()
        cp_dict["updated_at"] = self.updated_at.isoformat()
        return cp_dict
