Small python library to give easy access to etherscan address labels & names. Obviously only as up-to-date as the extension is, as the data is stored locally. Though that does mean it works offline and without any requests. 
<br>Overall size is 5.5MB, stored in 2 json files (addresses, labels) and compressed using bzip2. 

If you use this, don't attribute me/this repo. **Attribute etherscan.io instead!**

You can install this packaged after cloning using pip:

```
pip install .
```

An example of how to use it:

```pycon
>>> from etherscan_labels import Addresses
>>> a = Addresses.get("0x0000000000000000000000000000000000000000")
>>> a
<Address 0x0000000000000000000000000000000000000000 (Null Address: 0x000…000) [<Label Burn (Main)>, <Label Blocked>, <Label Genesis (Main)>]>
>>> a.name
'Null Address: 0x000…000'
>>> a.labels
[<Label Burn (Main)>, <Label Blocked>, <Label Genesis (Main)>]
>>> a.labels[0].description
'Tokens are commonly considered burned\xa0after sending to an address whose private keys are impossible (or extremely improbable) for anyone to have access to. Another recommended method is to create a contract which immediately self destructs and sends to its own address.'

```
