.data 
list: .word 10,3,2,4,6,10,6,5,-5,10
.text
main: la t0, list  #t0 points to start of above list
      lw t1, 0(t0) #load first number and guess its maximum
      li t2, 9   # 9 items remain in list 

loop: addi t0,t0,4 #advancing to the next number in list 
      lw t3,0(t0)  # load next listed number 
      bgt t1,t3,skip #if number in T1 is still maximum continue
      mv t1,t3 #guess that t3 is the max number 
skip: addi t2,t2,-1 #reduce numbers in list by 1 
      bne t2,zero,loop #keep looping while numbers remain 
      
      li a7,1  #print last chosen maximum number 
      mv a0,t1
      ecall
      
      li a7,10 # terminate program
      ecall
      