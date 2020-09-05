import json
import requests

address = "3FkenCiXpSLqD8L79intRNXUgjRoH9sjXa"
res = requests.get("https://blockchain.info/unspent?active=" + address)
utxo_list = json.loads(res.text)["unspent_outputs"]

print(str(len(utxo_list))+"個のUTXOが見つかりました")