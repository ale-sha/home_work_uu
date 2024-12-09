import unittest
from unittest import TestCase
from rt_with_exceptions import Runner, Tournament


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_one = Runner('Усэйн', 10)
        self.runner_two = Runner('Андрей', 9)
        self.runner_three = Runner('Ник', 3)

    def test_start_1(self):
        self.start = Tournament(90, self.runner_one, self.runner_three)
        result = Tournament.start(self.start)
        self.all_results.update(result)
        last_runner_name = result[max(result)]
        self.assertTrue(last_runner_name == "Ник")

    def test_start_2(self):
        self.start = Tournament(90, self.runner_two, self.runner_three)
        result = Tournament.start(self.start)
        self.all_results.update(result)
        last_runner_name = result[max(result)]
        self.assertTrue(last_runner_name == "Ник")

    def test_start_3(self):
        self.start = Tournament(90, self.runner_one, self.runner_two, self.runner_three)
        result = Tournament.start(self.start)
        self.all_results.update(result)
        last_runner_name = result[max(result)]
        self.assertTrue(last_runner_name == "Ник")

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

if __name__ == '__main__':
    unittest.main()