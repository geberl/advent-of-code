import copy

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

            addr_bit = int2bin(addr)
            while len(addr_bit) < 36:
                addr_bit = "0" + addr_bit

            addr_res = [i for i in addr_bit]
            for n, char in enumerate(mask):
                if char == "X":
                    addr_res[n] = "X"
                if char == "1":
                    addr_res[n] = "1"
                elif char == "0":
                    continue

            val_dec = int(line.strip().split(" = ")[1])

            operations.append(["".join(addr_res), val_dec])


# print(mask)
# print(operations)





def generate_addrs(mk):
    addr_chars = [i for i in mk]

    addrs = []

    for m, ch in enumerate(mk):
        if ch == "X":
            temp = copy.deepcopy(addr_chars)
            temp[m] = "1"
            addrs.append("".join(temp))
            temp[m] = "0"
            addrs.append("".join(temp))
            break

    return addrs


def generate_multi_addrs(add_list):
    for add in add_list:
        if "X" in add:
            sub_add = generate_addrs(add)
            generate_multi_addrs(sub_add)
        else:
            final_addr.append(add)


memory = dict()
for op in operations:
    final_addr = []
    generate_multi_addrs([op[0]])
    for address in final_addr:
        memory[int(address, 2)] = op[1]

result = 0
for _, v in memory.items():
    result += v

print(result)
