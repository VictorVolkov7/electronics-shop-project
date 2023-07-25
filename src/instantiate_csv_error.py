class InstantiateCSVError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'InstantiateCSVError: {self.message}'
