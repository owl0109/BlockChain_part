target = 0x777777 * 2 **(8*(0x1e - 0x03))
print(target)

#10進数 => 16進数
target_hex = hex(target)[2:].zfill(64)
print(target_hex)