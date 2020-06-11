
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

#import OOPRefresher


"""
Placeholder
    and empty node that needs a value to be provided to compute output.

variables
    changeable parameter of graph

graph
    global variables connecting variables and placeholders to operations

"""

import numpy as np

class Operation():

    def __init__(self, input_nodes=[]):

        self.input_nodes = input_nodes
        self.output_nodes = []

        for node in input_nodes:
            node.output_nodes.append(self)

        _default_graph.operations.append(self)

    def compute(self):
        pass


class add(Operation):

    def __init__(self,x,y):
        super().__init__([x,y])

    # overwrites other method
    def compute(self,x_var,y_var):
        self.input = [x_var, y_var]

        return x_var + y_var


class multiply(Operation):

    def __init__(self,x,y):
        super().__init__([x,y])

    # overwrites other method
    def compute(self,x_var,y_var):
        self.input = [x_var, y_var]

        return x_var * y_var

class matmul(Operation):

    def __init__(self,x,y):
        super().__init__([x,y])

    # overwrites other method
    def compute(self,x_var,y_var):
        self.input = [x_var, y_var]

        return x_var.dot(y_var)

class Placeholder():

    def __init__(self):

        self.output_nodes = []

        _default_graph.placeholders.append(self)

class Variable():
    
    def __init__(self,initial_value = None):

        self.value = initial_value
        self.output_nodes = []

        _default_graph.variables.append(self)

class Graph():
    
    def __init__(self):

        self.operations = []
        self.placeholders = []
        self.variables = []

    def set_as_default(self):

        global _default_graph
        _default_graph = self


# Post order traversal 

def traverse_postorder(operation):

    nodes_postorder = []

    def recurse(node):
        if isinstance(node, Operation):
            for input_node in node.input_nodes:
                recurse(input_node)

        nodes_postorder.append(node)

    recurse(operation)
    return nodes_postorder

g = Graph()
g.set_as_default()

A = Variable(10)
b = Variable(1)

x = Placeholder()

y = multiply(A,x)

z = add(y,b)

class Session():

    def run(self, operation, feed_dict={}):

        nodes_postorder = traverse_postorder(operation)

        for node in nodes_postorder:

            if type(node) == Placeholder:

                node.output = feed_dict[node]

            elif type(node) == Variable:

                node.output = node.value

            else:

                # operation
                node.inputs = [input_node.output for input_node in node.input_nodes]

                # asterisk is because we don't known how many arguments were going to pass in
                node.output = node.compute(*node.inputs)

            if type(node.output) == list:

                node.output = np.array(node.output)

        return operation.output

sess = Session()

result = sess.run(operation=z, feed_dict={x:10})

print("result: ",  result)


# new matrix multiplication example
g = Graph()
g.set_as_default()

A = Variable([[10,20], [30,40]])
b = Variable([1,2,])

x = Placeholder()

y =matmul(A,x)

z = add(y,b)

sess = Session()

result = sess.run(operation=z, feed_dict={x:10})

print("result2: ",  result)


