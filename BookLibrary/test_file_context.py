import unittest
import os
from file_context import file_context


class test_file_context(unittest.TestCase):

    def test_Add_ToNewFile_ItShouldOnlyOneText(self):
        filename = 'c:/1.pytest'
        text = "Hello!"
        os.remove(filename)
        fc = file_context(filename)
        fc.add(text)

        file = open(filename, "r")
        for line in file:
            self.assertEqual(f"{text}\n", line)
        file.close()

    def test_Add_ToExistingFile_ItShouldAppend(self):
        filename = 'c:/1.pytest'
        line_one = "Hello!"
        line_two = "World."

        os.remove(filename)
        fc = file_context(filename)
        fc.add(line_one)
        fc.add(line_two)

        file = open(filename, "r")
        count = 1
        for line in file:
            if count == 1:
                self.assertEqual(f"{line_one}\n", line)
            if count == 2:
                self.assertEqual(f"{line_two}\n", line)
            if count == 3:
                self.assertTrue(False)
            count = count + 1
        file.close()


if __name__ == "__main__":
    unittest.main()
