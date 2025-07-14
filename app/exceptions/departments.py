class Departments404Exception(Exception):
    def __init__(self, message: str):
        self.message = message
