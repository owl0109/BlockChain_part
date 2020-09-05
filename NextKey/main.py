import os
import binascii
import hmac
import hashlib
import ecdsa

#シードの作成
seed = os.urandom(32)
#キー
root_key = b"Bitcoin seed"

#512ビットのハッシュ値を作成する処理
def hmac_sha512(data,key_message):
    hash = hmac.new(data,key_message,hashlib.sha512).digest()
    return hash

#秘密鍵から公開鍵を作成する処理
def create_pubkey(private_key):
    publickey = ecdsa.SigningKey.from_string(private_key,curve=ecdsa.SECP256k1).verifying_key.to_string()
    return publickey

#マスター作成。
master = hmac_sha512(seed,root_key)

#前半256ビットでマスター秘密鍵を取得する
master_secretkey = master[:32]

#後半256ビットでマスターチェーンコードを取得する
master_chaincode = master[32:]

#マスター公開鍵作成
master_publickey = create_pubkey(master_secretkey)
master_publickey_integer = int.from_bytes(master_publickey[32:],byteorder="big")

#圧縮公開鍵生成
if master_publickey_integer % 2 ==0:
    master_publickey_x = b"\x02" + master_publickey[:32]
else:
    master_publickey_x = b"\x03" + master_publickey[:32]

print("マスター秘密鍵")
print(binascii.hexlify(master_secretkey))
print("\n")
print("マスターチェーンコード")
print(binascii.hexlify(master_chaincode))
print("\n")
print("マスター公開鍵")
print(binascii.hexlify(master_publickey_x))

index = 0
index_bytes = index.to_bytes(8,"big")

#データ作成
data = master_publickey_x + index_bytes

result_hmac512 = hmac_sha512(data,master_chaincode)

#親秘密鍵とHMAC-SHA512の結果の前半部を足す
sum_integer = int.from_bytes(master_secretkey,"big") + int.from_bytes(result_hmac512[:32],"big")

p = 2 ** 256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
#子秘密鍵の作成(マスターの一つ下の階層)
child_secretkey = (sum_integer % p).to_bytes(32,"big")

print("\n")
print("子秘密鍵")
print(binascii.hexlify(child_secretkey))
