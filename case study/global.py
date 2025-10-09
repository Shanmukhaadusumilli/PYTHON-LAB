counter = 10 # global variable

def local_increment():
    counter = 0 # local variable
    counter += 1
    print("Inside function, counter:", counter)

local_increment()
print("Outside function, global counter:", counter)
