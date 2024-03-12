#!/usr/bin/python3
"""Subclass for City model"""
from models.base_model import BaseModel


class City(BaseModel):
    """Model for Cities on AirBnB web app."""
    state_id = ""
    name = ""
