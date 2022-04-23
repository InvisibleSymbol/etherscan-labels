import compress_json

import pkg_resources

from .address import Address


class Addresses:
    addresses = compress_json.load(pkg_resources.resource_filename(__name__, "data/all.json.bz"))

    @staticmethod
    def get(address):
        return Address(address, Addresses.addresses.get(address.lower(), {}))
