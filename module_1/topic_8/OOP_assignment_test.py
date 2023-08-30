import unittest
from OOP_assignment import *


class UserAccountTest(unittest.TestCase):

    def setUp(self):  # set up class
        self.acct = UserAccount("Kyle", "001", "5000")

    def tearDown(self):  # tear down class
        del self.acct

    def test_object_created_required_attributes(self):  # test required attributes for class
        self.assertEqual(self.acct.account_owner, "Kyle")
        self.assertEqual(self.acct.account_num, "001")
        self.assertEqual(self.acct.account_balance, 5000)


if __name__ == '__main__':
    unittest.main()
