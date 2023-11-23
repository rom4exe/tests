import unittest
from yandex_api import createfolder, get_folder_info

FOLDERNAME = 'test2'


class TestYandexAPI(unittest.TestCase):
    def test_createfolder(self):
        result = createfolder(FOLDERNAME)
        self.assertEqual(result, 201, {result})

    def test_get_folder_info(self):
        self.assertTrue(get_folder_info(FOLDERNAME) == 'dir')
