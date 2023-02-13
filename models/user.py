#!/usr/bin/python3
"""
module user inherits BaseModel
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """class user that inherits BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
