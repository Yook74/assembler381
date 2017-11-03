# Assembler381
Acts as an assembler for the subset of MIPS used in COS 381

## Extra syntax rules
- Pretty much everything should be separated by spaces. For example: sll $0, $0, 0x0 is good but sll $0,$0, 0x0 isn't
- Each instruction must be on a separate line
- I type instructions are written in the form beq $0, $0, 0x0 No weird parentheses 
- You'll also note the absence of a label in the branch instruction. Only j type instructions can use labels
- Labels must start with an uppercase letter and instructions must be lowercase
- Immediate values are hex only and are written in the form -0xf (for negative 15)

## Features to add
- I'd like to make the above list as short as possible

## Things to note
- I actually don't know if this works. It outputs some hex but I haven't checked if it's the correct hex very thoroughly 
