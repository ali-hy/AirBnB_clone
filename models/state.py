#!/usr/bin/python3
'''This module defines the State class'''
from models.base_model import BaseModel


class State(BaseModel):
    '''This class represents a State'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if len(kwargs) > 0:
            self.name = kwargs['name']
        else:
            self.name = ''
