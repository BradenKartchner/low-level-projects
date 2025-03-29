## Resources

https://gbdev.io/gb-opcodes/optables/
https://gbdev.io/pandocs/About.html

## Opcodes

An "opcode" is the action the CPU carries out against the opcode's operands  
The Nintendo Gameboy's processor is a modified Intel 8080-style Sharp CPU called the LR35902
It is similar to the Z80, and uses a lot of the same assembly instructions

Structure of disassembled/assembly instructions:

<address> <opcode> <mnemonic> [<operand> ...] [; commentary]
Note that some opcodes don't have any operands and some have more than one

There are two distinct types of opcodes: prefixed and unprefixed

## Hex, binary, Endianness

Hex vs. binary:
One byte (8 bits) represents 0-255 in decimal, which is the same as 0x0 - 0xFF in hexadecimal
Bytes are commonly divided into 2 "nibbles" of 4 bits each
The two nibbles are usually called "high" and "low"
High and low nibbles can be swapped based on CPU architecture --> Endianness
Since the Z80 is an 8-bit CPU (with some limited 16-bit support), we will deal with nibbles, bits, and up to 2 bytes at a time

How to tell which Endian version your computer natively uses (using Python)
`sys.byteorder` (import sys)

Easy way of converting Hex to decimal:
take the right-most digit and multiply by 1
take the second from right and multiply by 16
take the third from right and multiply by 16 x 16 (16^2)
take the fourth from right and multiply by 16^3
etc
and then add the numbers up

## Cartridges and ROM

Gameboy has 16-bit address bus, so it can only address up to 32 KiB of a ROM (2 ^ 16 bytes / 2 ??)
Anything larger than that has more than 1 ROM chip and other chips to manage switching between them

Each cartridge has a reserved area of memory called the "Cartridge Header"
Header is located at offset 0x100 in the cartridge ROM

## Cartridge Header

Every ROM cartridge contains a similar header at address range `$0100 - $014F` (256 - 335)

$0100 - $0103: Entry point (256 - 259, 4 bytes)
After displaying the Nintendo logo, the built-in boot ROM jumps to the address $0100, which should then jump to the actual main program in the cartridge
Most commercial games fill this 4-byte area with a NOP instruction followed by `jp $0150`

$0104 - $0133: Nintendo logo (260 - 307, 48 bytes)
This area contains a bitmap image that is displayed when the GameBoy is powered on.
It must match the following hexadecimal dump, otherwise the boot ROM won't allow the game to run:
CE ED 66 66 CC 0D 00 0B 03 73 00 83 00 0C 00 0D
00 08 11 1F 88 89 00 0E DC CC 6E E6 DD DD D9 99
BB BB 67 63 6E 0E EC CC DD DC 99 9F BB B9 33 3E
For more info, see: https://gbdev.io/pandocs/The_Cartridge_Header.html
