from repository_base import RepositoryBase


class UserRepository(RepositoryBase):
    def add(self, entity):
        self.db_context.add(entity)
