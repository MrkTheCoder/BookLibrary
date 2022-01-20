from .bookrepository import BookRepository
from .userrepository import UserRepository
from .textfiledbcontext import TextFileDbContext
import os


class UnitOfWorks:
    def __init__(self):
        self.__books_file_path = "books.txt"
        self.__users_file_path = "users.txt"
        self.__books = None
        self.__users = None

    @property
    def books(self):
        if self.__books == None:
            self.books = BookRepository(
                TextFileDbContext(self.__books_file_path))
        return self.__books

    @books.setter
    def books(self, value):
        self.__books_file_path = value
        self.__books = BookRepository(
            TextFileDbContext(value))

    @property
    def users(self):
        if self.__users == None:
            self.users = UserRepository(
                TextFileDbContext(self.__users_file_path))
        return self.__users

    @users.setter
    def users(self, value):
        self.__users_file_path = value
        self.__users = UserRepository(
            TextFileDbContext(value))

    def remove_database_files(self):
        if os.path.exists(self.__users_file_path):
            os.remove(self.__users_file_path)
        if os.path.exists(self.__books_file_path):
            os.remove(self.__books_file_path)
