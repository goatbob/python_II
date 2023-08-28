import unittest
from insurance_quote_assignment import ins_rate_calc


class MyTestCase(unittest.TestCase):
    def setUp(self):  # set up student class
        self.student = St("Bob", "Bob", "Computer Sci", 3.9)

    def tearDown(self):  # tear down student class
        del self.student

    def test_object_created_required_attributes(self):  # test required attributes for class
        self.assertEqual(self.student.last_name, "Bob")
        self.assertEqual(self.student.first_name, "Bob")
        self.assertEqual(self.student.major, "Computer Sci")

    def test_object_created_all_attributes(self):  # test all attributes for class
        student = St("Bob", "Bob", "Computer Sci", 3.9)
        assert student.last_name == "Bob"
        assert student.first_name == "Bob"
        assert student.major == "Computer Sci"
        assert student.gpa == 3.9

    def test_student_str(self):  # test string output of class
        self.assertEqual(str(self.student), "Bob, Bob has major Computer Sci with gpa: 3.9")

    def test_student_str_2(self):  # test string output of class
        st = St("Bob", "Bob", "Computer Sci", 3.9)
        self.assertEqual(str(st), "Bob, Bob has major Computer Sci with gpa: 3.9")

    def test_object_not_created_error_last_name(self):  # test last name validation
        with self.assertRaises(ValueError):
            st = St("123", "Bob", "CompSci")

    def test_object_not_created_error_first_name(self):  # test first name validation
        with self.assertRaises(ValueError):
            st = St("Bob", "123", "CompSci")

    def test_object_not_created_error_major(self):  # test major validation
        with self.assertRaises(ValueError):
            st = St("Bob", "Bob", "123")

    def test_object_not_created_error_gpa(self):  # test gpa validation
        with self.assertRaises(ValueError):
            st = St("Bob", "Bob", "CompSci", "no")

    def test_object_not_created_error_gpa_2(self):  # test gpa validation
        with self.assertRaises(ValueError):
            st = St("Bob", "Bob", "CompSci", 6.0)


if __name__ == '__main__':
    unittest.main()
