class Tag:
    tags = {}
    def __init__(name=""):
        self.name = name
        Tag.tags[name] = self

    def create_tag(self, name=""):
        if name in tags:
            return Tag.tags[name]
        else:
            return Tag(name=name)

    @staticmethod
    def get_tag(self, name=""):
        if name in tags:
            return Tag.tags[name]
        else:
            return None
    @staticmethod
    def get_tags(self, names=[]):
        tags = []
        for n in names:
            t = Tag.getTag(n)
            if t != None:
                tags.append(t)
        return tags
