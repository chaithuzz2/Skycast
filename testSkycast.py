""" Author: Krishna Chaitanya Chavati
    Date  : 10.06.14
    Description: This is the test suite for Skycast
    problem. Contains four testcases obtained from
    text files in the folder """

import unittest
from Skycast import Skycast

class TestSkycast(unittest.TestCase):

    def setUp(self):
        pass

    def testcase_1(self):
        File = "testcases/t1.txt"
        self.assertEqual( Skycast(File), 7)

    def testcase_2(self):
        File = "testcases/t2.txt"
        self.assertEqual( Skycast(File), 8)

    def testcase_3(self):
        File = "testcases/t3.txt"
        self.assertEqual( Skycast(File), 12)

    def testcase_4(self):
        File = "testcases/t4.txt"
        self.assertEqual( Skycast(File), 7)


if __name__ == '__main__':
    unittest.main()
