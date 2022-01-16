class file_context:
    def __init__(self, file_path):
        self.file_path = file_path

    def add(self, text):
        file = open(f"{self.file_path}", "a")
        file.write(f"{text}\n")
        file.close()
