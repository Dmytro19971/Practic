import unittest

from module_12_1 import Runner
from unittest import TestCase


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner("Dima")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
        print('Test OK')

    def test_run(self):
        runner = Runner('Andrey')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
        print('Test OK')

    def test_challenge(self):
        runner_1 = Runner('Valentina')
        runner_2 = Runner('Anastasia')
        for i in range(10):
            if i % 2 == 0:
                runner_1.run()
            else:
                runner_2.walk()
            self.assertNotEqual(runner_1.distance, runner_2.distance)
            print('Test OK')


if __name__ == '__main__':
    unittest.main()
