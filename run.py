import time

def how_long(fxn):
    def inner(*arg):
        start = time.time()
        fxn(*arg)
        end = time.time()
        final = end - start
        return "execute time: " + str(final)
    return inner

def show_function(fxn):
    def inner(*arg): 
        fxn(*arg)
        return fxn.func_name + ': ' + str(arg)
    return inner
    
@show_function

def fib2(n):
    if n<=1:
        return 1
    else:
        return fib2(n-1)+fib2(n-2)


@how_long
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print fib(4)
print fib2(3)

