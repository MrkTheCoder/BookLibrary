import unittest
from .book import Book
from .user import User
from .unitofworks import UnitOfWorks


class UnitOfWorksTests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__("initialize")

    def initialize(self):
        self.database = UnitOfWorks()
        self.database.books = "c:/entity_book_file.txt"
        self.database.users = "c:/entity_user_file.txt"
        self.database.remove_database_files()

    # integration Test
    def test_Add_BookEntity_ShouldEntityAddedToDb(self):
        # Assign
        book = Book("Abc")

        # Action
        self.database.books.add(book)

        # Assert
        self.assertTrue(self.file_lines_verify(
            self.database.books_file_path, [book.title]))

    # integration Test
    def test_AddUserEntity_ShouldEntityAddedToDb(self):
        user = User("Abcd", "Efgh")

        self.database.users.add(user)

        self.assertTrue(self.file_lines_verify(
            self.database.users_file_path, [user]))

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
