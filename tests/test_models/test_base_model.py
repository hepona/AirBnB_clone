#!/usr/bin/python3
""" unittest for class BaseModel """

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from console import HBNBCommand
class TestBaseModel(unittest.TestCase):
    def test_Inequality_Of_Two_Id(self):
        """ test inequality of two id's """
        f = FileStorage()
        b1 = BaseModel()
        b2  = BaseModel()

        f.new(b1)
        f.new(b2)

        self.assertNotEqual(b1.id, b2.id)
    
    def test_inequality_of_two_instance(self):
        "Inequality of two instances of BaseModel"
        b1=BaseModel()
        b2=BaseModel()
        self.assertNotEqual(b1, b2)

    def test_if_id_is_str(self):
        "test id the id is a string"
        b1=BaseModel()
        
        self.addTypeEqualityFunc(b1.id , str)
    
    def test_printing_formatt(self):
        "test if printing the instance of BaseModel\
equals [<class name>] (<self.id>) <self.__dict__>"
        b = BaseModel()
        exceptation = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(exceptation, str(b))

    def test_if_basmodel_originatFrom_obj_class(self):
        "check if basemodel originate from objct class"
        b = BaseModel()
        self.assertIsInstance(b, object)

    def test_inequality_of_updateAt_createdAt(self):
        "check if update_at is difference from created_at after saving"
        f = FileStorage()
        b = BaseModel()
        # c = HBNBCommand()
        f.new(b)

        b.id =  "00000"
        self.assertNotEqual(b.created_at, b.updated_at)

        # c.do_update("BaseModel", b.id, id, "00000")



if __name__ == '__main__':
    unittest.main()