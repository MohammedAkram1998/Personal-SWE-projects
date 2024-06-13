
import multiprocessing


import time


from multiprocessing import Pool

def check_prime(num):
    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                res = False
                break
        else:
            res = True
    elapsed_time = time.time() - t1
    print(f"Number {num}: {'prime' if res else 'not prime'}, Time taken: {elapsed_time:.6f} seconds")
    return res, elapsed_time

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
    

def read_prime_numbers(filename,  n):
    # open the file in order to start reading 
    with open(filename, 'r') as  f:
        
    
        lines = f.readlines()
        
        # make an empty list of prime numbers called pr
        pr = []
        for line in lines:
            line = line.strip()
            
            # check for empty lines and validity
            if line and all(c.isdigit() for c in line.split()):
                pr.extend(int(num) for num in line.split())
                
                
            if len(pr) >= n:  # stop reading from the file.
                break
                
       # return the values.         
    return pr[:n]




if __name__ == '__main__':
    pnums   = read_prime_numbers('primes1.txt', 1000)
# run the process for 2 cores 
    print("run check_prime with 2 cores")
    pool_process(check_prime, pnums   , 2)
# run the proces for 1 core in order to compare the time 
    print("run check_prime with 1 core ")
    pool_process(check_prime, pnums  , 1)

