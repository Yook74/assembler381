#Takes a digit from the keyboard input, multiplies it by 3, and then outputs it

xor   $3, $0, $0 
ori   $3, $3, 0xFFF8 #$3 contains the address to read from
lw    $1, $3, 0 #$1 contains the last character read from the keyboard
addi  $1, $1, -0x30 #converts from ascii to integer

slt   $4, $1, $0 #$4 is 1 if $1 is negative
beq   $4, $0, 0x3 #if $1 is positive branch to  next check
xor   $0, $0, $0 #nop
j  	  End

Second:
xor   $5, $0, $0
addiu $5, $5, 0xA #load 10 into $5
slt   $4, $1, $5 #4 is 1 if $1 is valid
beq   $4, $0, 0x8

sll   $1, $1, 0x1  #this line and the next preform the actual operation
add   $1, $1, $1

addiu  $3, $3, 0x4 #set 3 to the output addr
sw    $1, $3, 0
addi  $5, $5, -0x2 #sets $5 to 8 FIXME this is wrong
srl   $1, $1, 0x8
sw    $1, $3, 0

End:
halt

