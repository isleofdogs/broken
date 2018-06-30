from collections.abc import MutableSequence

class Table(MutableSequence):
    def __init__(self, html):
        self.html = html

    def __getitem__(self, index):
        pass

    def __setitem__(self, index, value):
        pass

    def __delitem__(self, index):
        pass

    def __len__(self):
        pass

    def insert(self, index, value):
        pass
