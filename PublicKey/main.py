import ecdsa
import os
import binascii
import base58

#秘密鍵生成
private_key = os.urandom(32)

#公開鍵の生成
public_key = ecdsa.SigningKey.from_string(private_key,curve=ecdsa.SECP256k1).verifying_key.to_string()

#Y座標を取得(32から取得。)
public_key_y = int.from_bytes(public_key[32:],"big")

#圧縮公開鍵を生成(32まで取得)
if public_key_y %2 == 0:
    public_key_compressed = b"\x02"+public_key[:32]
else:
    public_key_compressed = b"\x03"+public_key[:32]

#実行するたび値が変わる
print(binascii.hexlify(public_key))
print(binascii.hexlify(public_key_compressed))