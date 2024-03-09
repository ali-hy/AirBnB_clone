#!/usr/bin/python3
'''This class defines a the Amenity class'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''This class represents an amenity'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if len(kwargs) > 0:
            self.name = kwargs['name']
        else:
            self.name = ''
