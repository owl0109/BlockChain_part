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
