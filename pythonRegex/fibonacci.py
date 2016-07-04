def fib(max):
    a,b=0,1;
    while a<max :
        yield a
        a,b=b,a+b

for i in fib(1000):
    print(i,end="  ")
print("")
filbs=list(fib(1000))
print(filbs)