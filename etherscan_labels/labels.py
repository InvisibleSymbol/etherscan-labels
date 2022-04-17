import json

import pkg_resources

from .label import Label


class Labels:
    labels = json.load(pkg_resources.resource_stream(__name__, 'data/labels.json'))

    @staticmethod
    def from_list(labels):
        return [
            Label(label_id=label['label_id'],
                  data=Labels.labels[label['label_id']],
                  sub_category=label.get('sub_category'))
            for label in labels]
