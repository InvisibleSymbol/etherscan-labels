from .labels import Labels


class Address:
    def __init__(self, address, data):
        self.address = address
        self.name = data.get('name')
        self.labels = Labels.from_list(data.get('labels', []))
        self.info = data.get('info')

    def __str__(self):
        name = f'Address {self.address}'
        if self.name:
            name += f' ({self.name})'
        if self.labels:
            name += f' {self.labels}'
        return name

    def __repr__(self):
        return f'<{self.__str__()}>'
