from math import fabs
import unittest
import os
from file_context import file_context


class test_file_context(unittest.TestCase):

    # Integration Test
    def test_Add_Oneline_ToNewFile_ShouldHaveOneline(self):
        # Arrange
        file_name = 'c:/1.pytest'
        line_one = "Hello!"
        os.remove(file_name)
        f_c = file_context(file_name)

        # Action
        f_c.add(line_one)

        # Assert
        self.assertTrue(self.file_lines_verify(
            file_name, [line_one]))

    # Integration Test
    def test_Add_OneLine_ToExistingFileWithOneLine_ShouldAppend(self):
        # Arrange
        file_name = 'c:/1.pytest'
        line_one = "Hello!"
        line_two = "World."
        os.remove(file_name)
        fc = file_context(file_name)

        # Action
        fc.add(line_one)
        fc.add(line_two)

        # Assert
        self.assertTrue(self.file_lines_verify(
            file_name, [line_one, line_two]))

    # Helper Method
    def file_lines_verify(self, file_name, lines):
        index = 0

        file = open(file_name, "r")

        for line in file:
            if index >= len(lines):
                return False

            if line != f"{lines[index]}\n":
                return False

            index = index + 1

        file.close()

        return True


# this 2 lines, will help to RUN this file as usual but "unit testing" process take control of it!
if __name__ == "__main__":
    unittest.main()
