# Define the parent class (BaseClass)
class BaseClass:
    """
    This is the parent class. It has a method called 'operation' that can be overridden by child classes.
    """
    def __init__(self, name):
        self.name = name
    def operation(self):
        """
        This is a method that performs a basic operation. It's designed to be overridden.
        """
        print(f"Performing operation in BaseClass for {self.name}")

# Define the first child class (ChildClassA)
class ChildClassA(BaseClass):
    """
    This class inherits from BaseClass and adds its own attributes and overrides the operation method.
    """
    def __init__(self, name, attribute_a, attribute_b):
        """
        Initializes the ChildClassA with name, attribute_a, and attribute_b.
        """
        super().__init__(name) # Calls the constructor of the parent class
        self.attribute_a = attribute_a
        self.attribute_b = attribute_b

    def operation(self):
        """
        Overrides the operation method from BaseClass.  Demonstrates polymorphism.
        """
        print(f"Performing operation in ChildClassA for {self.name} with attributes: {self.attribute_a}, {self.attribute_b}")

# Define the second child class (ChildClassB)
class ChildClassB(BaseClass):
    """
    This class also inherits from BaseClass and adds its own attributes and overrides the operation method.
    """
    def __init__(self, name, attribute_c, attribute_d):
        """
        Initializes the ChildClassB with name, attribute_c, and attribute_d.
        """
        super().__init__(name) # Calls the constructor of the parent class
        self.attribute_c = attribute_c
        self.attribute_d = attribute_d

    def operation(self):
        """
        Overrides the operation method from BaseClass.  Demonstrates polymorphism.
        """
        print(f"Performing operation in ChildClassB for {self.name} with attributes: {self.attribute_c}, {self.attribute_d}")

# Example usage
if __name__ == "__main__":
    # Create instances of the classes
    base_object = BaseClass("Base")
    child_a = ChildClassA("ChildA", "ValueA1", "ValueA2")
    child_b = ChildClassB("ChildB", "ValueB1", "ValueB2")

    # Demonstrate polymorphism
    base_object.operation() # Calls the base class method
    child_a.operation()    # Calls the overridden method in ChildClassA
    child_b.operation()    # Calls the overridden method in ChildClassB
