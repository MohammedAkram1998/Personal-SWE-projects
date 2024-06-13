.globl adder
.text
adder:            
add a0,a0, a1  # add the values in x10 and x11 and store the result in x10  
li a2, 22203536    #load the student number 22203536 in x12
add a0, a0, a2    #the addition of the values in x10 and x12 is stored to x10.
jr  ra

