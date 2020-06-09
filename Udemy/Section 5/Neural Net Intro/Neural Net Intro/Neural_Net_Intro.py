
"""
z = wx + b where w are the weights, x are the inputs and b is the bias term.
    z is the sum of all the inputs multiplied by the weights plus the bias term.

sigmoid function
    f(z) = 1/[1 + e^(-z)]

ReLU    rectified linear unit
    max(0,z)
        makes answer positive

Quadratic cost function
    C = sumOf(y-a)^2 / n
        larger errors are  more prominent due to the squaring

cross entropy
    c = (-1/n) * sumOf(y ln(a) + 1-y) ln(1-a)

backpropagation
    A way to actually learn and fix the error which is predicted
    Calculates error at the output and then distributes back through the network layers
    Requires a known desired output for each input value


gradient descent
    1st order minimizer


"""

# executes upon creation
class SimpleClass():

        def __init__(self, name): 
            print("hello")

        def yell(self):
            print("YELLING")


s = "world"

type(s)

# will print hello
x = SimpleClass()

#shows you what it is and where in the memory it is stored
print(x)


x.yell()

class ExtendedClass(SimpleClass):

    def __init__(self):

        # run the init method in the simple class
        super().__init__()
        print("EXTEND!")

y = ExtendedClass()
y.yell()

