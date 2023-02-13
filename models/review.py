#!/usr/bin/python3
"""
module review inherits BaseModel
"""

import models
from models.base_model import BaseModel


class Review(BaseModel):
    """class review that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
