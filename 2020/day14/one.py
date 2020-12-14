mask = ""
operations = []


def int2bin(num):
    result = []
    while num:
        result.append(str(num & 1))
        num >>= 1
    return ''.join(result[::-1])


with open("input.txt") as file_handler:
    for line in file_handler:
        if line.strip().startswith("mask"):
            mask = line.strip().split(" = ")[1]
        elif line.strip().startswith("mem"):
            addr = line.strip().split("[")[1]
            addr = int(addr.split("]")[0])

            val_dec = int(line.strip().split(" = ")[1])

            val_bit = int2bin(val_dec)
            while len(val_bit) < 36:
                val_bit = "0" + val_bit

            res_bit = [i for i in val_bit]
            for n, char in enumerate(mask):
                if char == "X":
                    continue
                if char == "1":
                    res_bit[n] = "1"
                elif char == "0":
                    res_bit[n] = "0"

            operations.append([addr, val_dec, val_bit, "".join(res_bit)])


memory = dict()
for op in operations:
    memory[op[0]] = op[3]

result = 0
for k, v in memory.items():
    result += int(v, 2)

print(result)
