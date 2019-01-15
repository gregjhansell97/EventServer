class Event:
    def __init__(
            self,
            name="",
            time=None,
            location=(0,0),
            tags=[],
            description=""):
        self.name = name
        self.time = time
        self.description = description
        self.tags = tags
        self.location = location
