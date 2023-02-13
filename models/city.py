#!/usr/bin/python3
"""
module city that inherits BaseModel
"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """class city inherits BaseModel"""

    state_id = ""
    name = ""
