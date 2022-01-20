from .repositorybase import RepositoryBase


class BookRepository(RepositoryBase):
    def add(self, entity):
        self.db_context.add(entity)
