import unittest
from lr3 import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {
            'name': 'Лера',
            'answer1': 'Красная панда',
            'answer2': 'Она напоминает мне мою лучшую подругу'
        }
        response = self.app.post('/', data=data)
        self.assertIn('Спасибо за ответы!'.encode('utf-8'), response.data)

    def test_empty(self):
        data = {
            'name': '',
            'answer1': 'Кошка',
            'answer2': 'Пушистая'
        }
        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()