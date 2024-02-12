#!/usr/bin/python3
"""This is the City Model module."""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
