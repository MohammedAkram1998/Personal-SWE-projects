	.text 

# student number 22203536
# expression is 2*0/5/6=0
	li t0, 2
	li t1, 0
	li t2, 5
	li s1, 6
	mul s0,t0,t1
	div s2,s0,t2
	div s3,s2,s1
	mv a0, s3
	li a7, 1
	ecall
