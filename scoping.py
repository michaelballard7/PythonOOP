
# local scoping:
def report():
    # this is local assignement
    x = 'local'
    print(x)

# global scoped variable
x = "This is a global variable"

def enclosing():
    # enclosing scoped variable
    x = "enclosing level of scope"
    def inside_function():
        # local scoped variable
        x = "this is a local variable"
        print(x)
    inside_function()

def global_use():
    # use the global builtin keyword to explicitly use a global variable
    global x 
    print(x)

enclosing()

global_use()