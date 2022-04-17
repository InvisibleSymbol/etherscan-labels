class Label:
    def __init__(self, label_id, data, sub_category=None):
        self.id = label_id
        self.name = data['name']
        self.sub_category = None
        if sub_category:
            self.sub_category = data.get('sub_categories', {}).get(sub_category)
        self.description = data['description'].get('clean')
        self.raw_description = data['description'].get('raw')

    def __str__(self):
        name = f'Label {self.name}'
        if self.sub_category:
            name += f' ({self.sub_category})'
        return name

    def __repr__(self):
        return f'<{self.__str__()}>'
