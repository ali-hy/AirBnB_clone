#!/usr/bin/python3
'''Manages saving to and loading from files in json format'''
import json
import os
import importlib


class FileStorage:
    '''Manages saving to and loading from files in json format'''

    __classes = dict()
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        '''get all objects currently loaded'''
        return FileStorage.__objects

    def new(self, obj):
        '''add a new object to __objects'''
        FileStorage.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        '''save all currently loaded objects'''
        with open(FileStorage.__file_path, 'w') as f:
            serializable = {k: obj.to_dict() for k, obj in self.all().items()}
            json.dump(serializable, f)

    def reload(self):
        '''load all previously saved objects'''
        if len(FileStorage.__classes) == 0:
            FileStorage.__classes = {
                'BaseModel': importlib.import_module(
                    'models.base_model').BaseModel,
                'User': importlib.import_module('models.user').User,
                'State': importlib.import_module('models.state').State,
                'City': importlib.import_module('models.city').City,
                'Amenity': importlib.import_module('models.amenity').Amenity,
                'Place': importlib.import_module('models.place').Place,
                'Review': importlib.import_module('models.review').Review
            }
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            tmp = json.load(f)
            for key, obj in tmp.items():
                self.all()[key] = FileStorage.__classes[obj['__class__']](
                    **obj)

    def get(self, classname, id):
        '''get an object using classname and id'''
        key = f'{classname}.{id}'
        if key in self.all():
            return self.all()[key]
        return None

    def delete(self, classname, id):
        '''delete an object using classname and id'''
        key = f'{classname}.{id}'
        if key in self.all():
            del FileStorage.__objects[key]
            return True
        return False
