# This is example of tail recursion as recursion fn call is placed at the end
counter = 0

def tail_func():
    global counter
    if counter == 4:
        return
    
    print(f'{counter} -> Rishabh')
    counter += 1
    tail_func()

tail_func()

# This is example of head recursion as recursion fn call is placed before the action
counter2 = 0
def head_func():
    global counter2
    if counter2 == 4:
        return
    
    counter2 += 1
    head_func()
    print(f'{counter2} -> Rishabh')

head_func()
