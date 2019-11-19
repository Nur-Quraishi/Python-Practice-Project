def transmit_to_space(message):
    # "This is the enclosing function"
    def data_transmitter():
        # "The nested function"
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))


def print_msg(number):
    def printer():
        # "Here we are using the nonlocal keyword"
        nonlocal number
        number = 3
        print(number)

    printer()
    print(number)


print_msg(9)


def transmit_to_space(message):
    # "This is the enclosing function"
    def data_transmitter():
        # "The nested function"
        print(message)

    return data_transmitter


fun2 = transmit_to_space("Burn the Sun!")
fun2()


# ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.(Eg. When there are
# few methods in a class, use closures instead).

# your code goes here

def multiplier_of(number):
    def multiply_with(param):
        return param * number

    return multiply_with


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
