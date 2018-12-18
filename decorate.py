
def weclome(func1):
    def sub_func(*t,**args):
        print("welcome")
        func1(*t,**args)
    return sub_func

@weclome
def cs(t):
    print("cs",t)

cs(5)

