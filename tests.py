import unittest
from parameterized import parameterized
from main import course_longer, top_name, same_names

class UnitTestMain(unittest.TestCase):

    @parameterized.expand ([
        [("Python-разработчик с нуля", 12),
          ("Fullstack-разработчик на Python, Frontend-разработчик с нуля", 20)]
    ])
    def test_top_name(self, course, lenth):
        self.assertEqual(course_longer(), (course, lenth))

    @parameterized.expand([
        [['Александр: 10', 'Евгений: 5', 'Максим: 4']]
    ])
    def test_top_name(self, name_repeat):
        self.assertEqual(top_name(), (name_repeat))

    @parameterized.expand([
        [['Иван Бочаров', 'Иван Маркитан', 'Максим Батырев', 'Максим Воронцов', 'Сергей Индюков', 'Сергей Сердюк']]
    ])
    def test_same_names(self, same_name):
        self.assertIn(same_name, same_names())
