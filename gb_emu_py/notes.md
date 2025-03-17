## Resources

https://gbdev.io/gb-opcodes/optables/

## Opcodes

An "opcode" is the action the CPU carries out against the opcode's operands  
The Nintendo Gameboy's processor is a modified Intel 8080-style Sharp CPU called the LR35902
It is similar to the Z80, and uses a lot of the same assembly instructions

Structure of disassembled/assembly instructions:

<address> <opcode> <mnemonic> [<operand> ...] [; commentary]
Note that some opcodes don't have any operands and some have more than one

There are two distinct types of opcodes: prefixed and unprefixed

Hex vs. binary:
One byte (8 bits) represents 0-255 in decimal, which is the same as 0x0 - 0xFF in hexadecimal
Bytes are commonly divided into 2 "nibbles" of 4 bits each
The two nibbles are usually called "high" and "low"
High and low nibbles can be swapped based on CPU architecture --> Endianness
Since the Z80 is an 8-bit CPU (with some limited 16-bit support), we will deal with nibbles, bits, and up to 2 bytes at a time
