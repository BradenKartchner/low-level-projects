# parsing the provided JSON
import json

with open("./gb_emu_py/opcodes/opcodes.json", "r") as file:
    data = json.load(file)
print(data['unprefixed']['0x00'])

unprefixedMnem = [instr['mnemonic'] for instr in data['unprefixed'].values()]
print(unprefixedMnem)

## TODO: make classes for Instruction and Operand


# random experimentation
'''
someValues = data['unprefixed'].values()
print(someValues)
'''

