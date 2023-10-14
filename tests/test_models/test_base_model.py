#!/usr/bin/python3
""" unittest for class BaseModel """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from console import HBNBCommand
import re


class TestBaseModel(unittest.TestCase):
    """unitest for basemodel"""

    def test_Inequality_Of_Two_Id(self):
        """test inequality of two id's"""
        f = FileStorage()
        b1 = BaseModel()
        b2 = BaseModel()

        f.new(b1)
        f.new(b2)

        self.assertNotEqual(b1.id, b2.id)

    def test_id_is_uuid_string(self):
        """test Ensure id is a uuid4 string (len == 36)"""
        f = FileStorage()
        b = BaseModel()
        f.new(b)

        self.addTypeEqualityFunc(b.id, str)
        self.assertAlmostEqual(len(b.id), 36)

    def test_inequality_of_two_instance(self):
        "Inequality of two instances of BaseModel"
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1, b2)

    def test_if_id_is_str(self):
        "test id the id is a string"
        b1 = BaseModel()

        self.addTypeEqualityFunc(b1.id, str)

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
        "check if update_at is difference\
        from created_at before and after saving"

        f = FileStorage()
        b = BaseModel()
        f.new(b)
        self.assertNotEqual(b.created_at, b.updated_at)
        b.id = "00000"
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_if_created_at_always_less_than_update_at(self):
        "check if created_at <= updated_at"
        f = FileStorage()
        b = BaseModel()
        f.new(b)

        b.id = "00000"
        b.save()
        self.assertGreaterEqual(b.updated_at, b.created_at)

    def test_createdat_updatedat_format(self):
        "check if updated_at and created_at respect format"
        b = BaseModel()
        form = "%Y-%m-%dT%H:%M:%S.%f"
        dic = b.to_dict()
        self.assertEqual(datetime.strptime(dic["created_at"], form),
                         b.created_at)
        self.assertEqual(datetime.strptime(dic["updated_at"], form),
                         b.updated_at)

    def test_if_updatenew_greaterThan_updateold(self):
        "check if new update_at is greater than old update_at"
        b = BaseModel()
        f = FileStorage()
        f.new(b)
        old = b.updated_at
        b.id = "00000"
        b.save()
        new = b.updated_at

        self.assertGreater(new, old, "nope")

    def test_if_createdAt_updatedAt_instance_of_datetime(self):
        "Check if created_at, and Updated_at are instances of datetime"
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)

    def test_check_toDict_return_Dictionary(self):
        "Check if to_dict returned a dictionary\
        that has the correct keys and values"
        b = BaseModel()
        dic = b.to_dict()
        for k in dic.keys():
            self.assertTrue(
                k == "id" or k == "created_at" or
                k == "updated_at" or k == "__class__"
            )


if __name__ == "__main__":
    unittest.main()
