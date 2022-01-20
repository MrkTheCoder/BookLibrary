from abc import ABC, abstractmethod


class RepositoryBase:
    def __init__(self, db_context):
        self.db_context = db_context

    @abstractmethod
    def add(self, entity):
        raise NotImplementedError
