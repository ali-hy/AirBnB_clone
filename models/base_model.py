#!/usr/bin/python3
'''Defines BaseModel Class that defines all common attributes/methods shared by
other classes'''
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''BaseModel that defines all common attributes/methods that are shared
    by other classes'''

    def __init__(self, *args, **kwargs) -> None:
        '''BaseModdel constructor'''
        if len(kwargs) > 0:
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        '''save model to a file. Not yet implemented'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''create a dictionary that represents the object'''
        res = dict(self.__dict__)
        res['__class__'] = self.__class__.__name__
        res['created_at'] = self.created_at.isoformat()
        res['updated_at'] = self.updated_at.isoformat()
        return res

    def __str__(self) -> str:
        '''convert object to string'''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def __repr__(self) -> str:
        return f"BaseModel(id='{self.id}'," + \
            "created_at={repr(self.created_at)}," + \
            "updated_at={repr(self.updated_at)})"


if __name__ == '__main__':
    models = [BaseModel() for _ in range(10)]
    for m in models:
        print(m)
    print('\n')
    print([m.to_dict() for m in models])
