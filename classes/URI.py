class URI:

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.uri = data["uri"]
        self.selector = data["selector"]
        self.value = data["value"]
        self.trash = data["trash"]

