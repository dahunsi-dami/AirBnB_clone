#!/usr/bin/python3
"""Subclass for Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Model for Reviews on AirBnB web app."""
    place_id = ""
    user_id = ""
    text = ""
