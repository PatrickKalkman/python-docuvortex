import os


class VortexContentIterator():
    def __init__(self, content_path):
        self.content_path = content_path

    def __iter__(self):
        for file in os.listdir(self.content_path):
            if file.endswith(".pdf"):
                yield os.path.join(self.content_path, file)
