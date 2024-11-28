import unittest
from unittest import TestCase
from rt_with_exceptions import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        first = Runner('Вася')
        [first.walk() for _ in range(10)]
        self.assertEqual(first.distance, 50)

    def test_run(self):
        first = Runner('Вася')
        [first.run() for _ in range(10)]
        self.assertEqual(first.distance, 100)

    def test_challenge(self):
        first = Runner('Вася')
        second = Runner('Илья')
        [first.walk() for _ in range(10)]
        [second.run() for _ in range(10)]
        self.assertNotEqual(first.distance, second.distance)

if __name__ == '__main__':
    unittest.main()