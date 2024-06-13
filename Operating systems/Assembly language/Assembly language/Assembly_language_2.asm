		.text
main:
		li t0, 0xffff0010
		li t1, 0x5B        # 2
		sb t1, 0(t0)
		li t1, 0x5B        # 2
		sb t1, 0(t0)
		li t1, 0x5B        # 2 
		sb t1, 0(t0)
		li t1, 0x3F        #0
		sb t1, 0(t0)
		li t1, 0x4F        #3
		sb t1, 0(t0)
		li t1, 0x6D        #5
		sb t1, 0(t0)
		li t1, 0x4F         #3
		sb t1, 0(t0)
		li t1, 0x7D        #6
		sb t1, 0(t0)
		li a7, 10
		ecall

