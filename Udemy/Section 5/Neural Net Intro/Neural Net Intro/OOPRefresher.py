
# executes upon creation
class SimpleClass():

        def __init__(self, name): 
            print("hello " + name)

        def yell(self):
            print("YELLING")


s = "world"

type(s)

# will print hello
x = SimpleClass("andy")

#shows you what it is and where in the memory it is stored
print(x)


x.yell()

class ExtendedClass(SimpleClass):

    def __init__(self):

        # run the init method in the simple class
        super().__init__("john")
        print("EXTEND!")

y = ExtendedClass()
y.yell()