import os
import binascii

#32バイトの乱数の生成
private_key = os.urandom(32)

print(private_key)
#バイナリデータを16進数に変換する(これはわかりやすくするためにやっている)
print(binascii.hexlify(private_key))
