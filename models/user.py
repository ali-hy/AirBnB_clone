#!/usr/bin/python3
'''This module defines the User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''This class represents a user of hbnb'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if len(kwargs) > 0:
            self.email = kwargs['email']
            self.password = kwargs['password']
            self.first_name = kwargs['first_name']
            self.last_name = kwargs['last_name']
        else:
            self.email = ''
            self.password = ''
            self.first_name = ''
            self.last_name = ''
