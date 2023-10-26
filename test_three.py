def my_function():
    print('My function has run')

def call_it_twice(function):
    function()
    function()

call_it_twice(my_function)