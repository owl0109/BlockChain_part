import ecdsa
import os
import base58
import hashlib

#秘密鍵生成
private_key = os.urandom(32)

#公開鍵の生成
public_key = ecdsa.SigningKey.from_string(private_key,curve=ecdsa.SECP256k1).verifying_key.to_string()

#非圧縮公開鍵
prefix_and_pubkey = b"\x04"+ public_key

#hash160を作成
intermediate = hashlib.sha256(prefix_and_pubkey).digest()
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(intermediate)
hash160 = ripemd160.digest()

#ハッシュ160 + バージョンプレフィックス
prefix_and_hash160 = b"\x00" + hash160

#hashlib.256を入れる
double_hash = hashlib.sha256(hashlib.sha256(prefix_and_hash160).digest()).digest()

#チェックサム
check_sum = double_hash[:4]

pre_address = prefix_and_hash160 + check_sum
#base58でエンコード
address = base58.b58encode(pre_address)
print(address)