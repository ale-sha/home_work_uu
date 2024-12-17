import unittest
from unittest import TestCase
from rt_with_exceptions import Runner

import logging

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='UTF-8',
    format="%(asctime)s | %(levelname)s | %(message)s"
)
class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            first = Runner('Вася', -5)
            [first.walk() for _ in range(10)]
            self.assertEqual(first.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            first = Runner(15, 10)
            [first.run() for _ in range(10)]
            self.assertEqual(first.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        first = Runner('Вася')
        second = Runner('Илья')
        [first.walk() for _ in range(10)]
        [second.run() for _ in range(10)]
        self.assertNotEqual(first.distance, second.distance)

if __name__ == "__main__":
    unittest.main()



