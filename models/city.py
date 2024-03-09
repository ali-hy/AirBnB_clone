#!/usr/bin/python3
'''This module defines the City class'''
from models.base_model import BaseModel


class City(BaseModel):
    '''This class represents a City'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if len(kwargs) > 0:
            self.state_id = kwargs['state_id']
            self.name = kwargs['name']
        else:
            self.state_id = ''
            self.name = ''
