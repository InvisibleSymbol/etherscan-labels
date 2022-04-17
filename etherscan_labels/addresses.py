import json

import pkg_resources

from .address import Address


class Addresses:
    addresses = json.load(pkg_resources.resource_stream(__name__, 'data/all.json'))

    @staticmethod
    def get(address):
        return Address(address, Addresses.addresses.get(address.lower(), {}))
