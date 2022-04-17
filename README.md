Small python library to give easy access to etherscan address labels & names. Obviously only as up-to-date as the extension is, as the data is stored locally. Though that does mean it works offline and without any requests. Bit chonky, the data is about 19.2 MB, could prob be reduced by quite a bit if wanted. 

If you use this, don't attribute me/this repo. **Attribute etherscan.io instead!**

You can install this packaged after cloning using pip:

```
pip install .
```

Then you can use it like this:

```pycon
>>> from etherscan_labels import Addresses
>>> Addresses.get("0x0000000000000000000000000000000000000000")
<Address 0x0000000000000000000000000000000000000000 (Null Address: 0x000…000) [<Label Blocked>, <Label Burn (Main)>, <Label Genesis (Main)>]>
```
