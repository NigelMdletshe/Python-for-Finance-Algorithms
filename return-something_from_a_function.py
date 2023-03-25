#How to return something from a function

def example():
    fun  = 'I am having fun!'
    sky  = 7
    blue = 'orange'
    return fun,sky,blue

example()    

fun  = example()
print(fun)
#('I am having fun!', 7, 'orange')

fun = example()[0]
print(fun)
#I am having fun!

sky = example()[1]
blue = example()[2]

print(f'fun = {fun} sky = {sky} blue  = {blue}')
#fun= I am having fun! sky = 7 blue  = orange