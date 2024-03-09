#!/usr/bin/python3
'''This module defines the Place class'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''This class represents a Place'''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if len(kwargs) > 0:
            self.city_id = kwargs['city_id']
            self.user_id = kwargs['user_id']
            self.name = kwargs['name']
            self.description = kwargs['description']
            self.number_rooms = kwargs['number_rooms']
            self.number_bathrooms = kwargs['number_bathrooms']
            self.max_guest = kwargs['max_guest']
            self.price_by_night = kwargs['price_by_night']
            self.latitude = kwargs['latitude']
            self.longitude = kwargs['longitude']
            self.amenity_ids = kwargs['amenity_ids']
        else:
            self.city_id = ''
            self.user_id = ''
            self.name = ''
            self.description = ''
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
