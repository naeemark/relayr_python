from itertools import permutations


class Finder(object):
    def __init__(self, collection=[]):
        super().__init__()
        self.collection = collection

    def is_empty(self):
        return len(self.collection) == 0

    def find(self, string=None):
        result = []
        if string:
            permutes = [''.join(p) for p in permutations(string)]
            for s in self.collection:
                for t in permutes:
                    if t in s:
                        result.append(s)
        return result
