def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local
def ham():
    print(eggs) # this is global

eggs = 42 #this is also global
spam()
print(eggs)
