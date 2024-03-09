#!/usr/bin/python3
'''This module defines the Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if len(kwargs) > 0:
            self.place_id = kwargs['place_id']
            self.user_id = kwargs['user_id']
            self.text = kwargs['text']
