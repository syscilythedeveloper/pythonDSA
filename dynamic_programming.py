counter = 0
def fib1(n):
    global counter 
    counter +=1
    if n ==0 or n==1:
        return n
    return fib1(n-1) + fib1(n-2)


n = 2 
m = 7 
k = 12



print("Fib of: ", k, "=", fib1(k), "Counter: ", counter)
print("Fib of: ", n, "=", fib1(n), "Counter: ", counter)
print("Fib of: ", m, "=", fib1(m), "Counter: ", counter)


memo = [None] * 100
counter2 = 0
def fib(n):
    global counter2 
    counter2 +=1
    if memo[n] is not None: 
        return memo[n]
    
    
    if n ==0 or n==1:
        return n
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print("Memo Fib of: ", n, "=", fib(n), "Counter: ", counter2)
print("Memo Fib of: ", m, "=", fib(m), "Counter: ", counter2)
print("Memo Fib of: ", k, "=", fib(k), "Counter: ", counter2)



def bottom_up_fib(n):
    fib_list=[0,1]
    for index in range(2, n+1):
        next_fib = fib_list[index-1] + fib_list[index-2]
        fib_list.append(next_fib)
    return fib_list[n]

x=7
print("Bottom up - Fib of ", n, "=", bottom_up_fib(x))