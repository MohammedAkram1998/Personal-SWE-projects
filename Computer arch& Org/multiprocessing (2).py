
import multiprocessing

import time

from multiprocessing   import Pool



def fact(x):
    t  = time.time()
    y =1
    for i in range(1, x+1 , 1):
        y = (i*y)
    time1  = time.time()  - t
    
    
    print(f"factorial of {x}: {y} , time taken is {time1:.6f} seconds")
    
    return y , time1 
      
def pool_process  (f,   d ,   p):
    # define the variables 
    tx =     time.time()
    pool =   Pool(p)
    r = pool.map(f, d)
    
    # use .close() and .join() methods 
    pool.close()
    pool.join()
    
    # print the results finally 
    print("the results are ", r)
    ty =   time.time() - tx
    print(f"the total time is : {ty:.6f} seconds")
    

    

    

def makenums(n):
    #generate a list of numebrs from 1 to the number of numbers specified for the factorials 
    return list(range(1, n + 1))

if __name__ == '__main__':
    #generate a certain number of factorials 
    n =  makenums(5000)
    
    
# running the factorial with 2 cores 
    print("run factorial with 2 cores ")
    pool_process(fact, n, 2)
    
    
    
    
    # running the factorial with 1 core
    print("run the factorial with 1 core")
    pool_process(fact, n, 1)
    
    

    
