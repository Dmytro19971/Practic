from module_12_2 import Runner
from module_12_2 import Tournament
import unittest
from unittest import TestCase


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = [
            Runner("Dima", 10),
            Runner("Andrey", 9),
            Runner("Nick", 3),
        ]

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print("{}:".format(key))
            for k, v in value.items():
                print("{}: {}".format(k, v))

    def test_dima_and_nick(self):
        turn_1 = Tournament(90, self.runners[0], self.runners[2])
        result = turn_1.start()
        self.assertTrue(list(result.values())[-1].name == "Nick")
        self.all_results["Result Dima and Nick"] = result

    def test_andrey_and_nick(self):
        turn_2 = Tournament(90, self.runners[1], self.runners[2])
        result = turn_2.start()
        self.assertTrue(list(result.values())[-1].name == "Nick")
        self.all_results["Result Andrey and Nick"] = result

    def test_dima_andrey_nick(self):
        turn_3 = Tournament(90, *self.runners)
        result = turn_3.start()
        self.assertTrue(list(result.values())[-1].name == "Nick")
        self.all_results["Result of the overall race"] = result



if __name__ == "__main__":
    unittest.main()