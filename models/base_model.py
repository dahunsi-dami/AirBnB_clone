#!/usr/bin/python3
"""The base class `BaseModel`."""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Defines common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """
        Initializes public instance attributes.

        Args:
            id: assigns uuid on instance creation.
            created_at: current datetime when instance's created.
            updated_at: also datetime & updated on obj change.
        """
        if len(kwargs) != 0:
            if "__clas__" in kwargs:
                del kwargs["__class__"]

            for k, v in kwargs.items():
                if k in ["updated_at", "created_at"]:
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Modifies custom string representation an object."""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates `updated_at` w/ current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dict w/ key val of instance attribute."""
        cp_dict = self.__dict__.copy()
        cp_dict["__class__"] = self.__class__.__name__
        cp_dict["created_at"] = self.created_at.isoformat()
        cp_dict["updated_at"] = self.updated_at.isoformat()
        return cp_dict
