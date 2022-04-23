import compress_json

import pkg_resources

from .label import Label


class Labels:
    labels = compress_json.load(pkg_resources.resource_filename(__name__, "data/labels.json.bz"))

    @staticmethod
    def from_list(labels):
        return [
            Label(label_id=label['label_id'],
                  data=Labels.labels[label['label_id']],
                  sub_category=label.get('sub_category'))
            for label in labels]
