import os
import compress_json

from .label import Label


class Labels:
    labels = compress_json.load(os.path.join(os.path.dirname(__file__), "data/labels.json.bz"))

    @staticmethod
    def from_list(labels):
        return [
            Label(label_id=label['label_id'],
                  data=Labels.labels[label['label_id']],
                  sub_category=label.get('sub_category'))
            for label in labels]
