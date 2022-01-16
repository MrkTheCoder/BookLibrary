class repository:
    def __init__(self, db_context):
        self.db_context = db_context

    def add(self, entity):
        self.db_context.add(entity)
