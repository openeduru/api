
import json, os


class Schema:

    def __init__(self, name: str):

        self.filename = os.path.normpath(
            os.path.dirname(__file__) + '/../schema/' + name + '.json'
        )
        fh = open(self.filename, 'r', -1, 'utf-8')
        self.schema = json.load(fh)

    def get(self):
        return self.schema

    def check(self, expected):
        self.expected = expected
        return self.result

    def _check(self, block):
        pass

