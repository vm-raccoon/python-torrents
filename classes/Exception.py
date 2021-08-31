class Exception:

    def __init__(self, data):
        self.id = data["id"]
        self.value = data["value"]
        self.trash = data["trash"]

