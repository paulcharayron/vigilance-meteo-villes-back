class MeteoFrDPVigilance404Exception(Exception):
    def __init__(self, message: str):
        self.message = message


class MeteoFrDPVigilance500Exception(Exception):
    def __init__(self, message: str):
        self.message = message
