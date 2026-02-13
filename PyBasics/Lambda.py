fun = lambda : print("LPU")
fun()

fun = lambda x : print(x)
fun("Punjab")

fun = lambda x,y : print("Sum :-",x+y)
fun(2,5)

fun = lambda x,y,z : print("Triple Sum :-",x+y+z)
fun(2,5,6)

fun = lambda x,y : print("Conditional Statement :-",x if x > y else y)
fun(2,5)

fun = lambda x,y : print("Conditional Statement :-",2*x if x > y else y*y)
fun(5,2)

pattern = lambda n : list(map(lambda i : print("*"*i),range(1,n+1)))
pattern(5)

pattern = lambda n : list(map(lambda i : print(str(i)*i),range(1,n+1)))
pattern(5)

pattern = lambda n : list(map(lambda i : print("*"*i),range(n,0,-1)))
pattern(5)