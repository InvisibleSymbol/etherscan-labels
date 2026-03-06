import os
import compress_json

from .address import Address


class Addresses:
    addresses = compress_json.load(os.path.join(os.path.dirname(__file__), "data/all.json.bz"))

    @staticmethod
    def get(address):
        return Address(address, Addresses.addresses.get(address.lower(), {}))
