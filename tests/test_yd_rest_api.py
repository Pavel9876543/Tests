import unittest

from yandex_rest_api import YandexAPI, get_yd_token


class TestYdRestApi(unittest.TestCase):
    def setUp(self):
        self.yd_token = get_yd_token('yd_token.txt')

    def tearDown(self):
        del self.yd_token

    def test_create_folder(self):
        ya_disk = YandexAPI(self.yd_token)
        status_code = ya_disk.create_folder('new_directory')
        # 201 — Created, 409 — уже существует
        self.assertIn(status_code, (201, 409))

    def test_negative_yd_token(self):
        ya_disk = YandexAPI('invalid_token')
        self.assertRaises(PermissionError, ya_disk.create_folder, 'directory_new')