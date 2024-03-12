#!/usr/bin/python3
"""Subclass of BaseModel, User"""

from models.base_model import BaseModel


class User(BaseModel):
    """Model for users of the AirBnB website"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
