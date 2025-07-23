# Define the parent class 'Instrument'
class Instrument:
    def __init__(self, name, instrument_type):
        # Initialize the attributes of the instrument
        self.name = name
        self.instrument_type = instrument_type

    def make_sound(self):
        # This is a generic method that will be overridden by child classes
        return f"{self.name} makes a generic instrument sound."

# Define the child class 'Guitar' which inherits from 'Instrument'
class Guitar(Instrument):
    def __init__(self, name, num_strings, is_acoustic):
        # Call the parent class constructor to initialize inherited attributes
        super().__init__(name, "String Instrument")
        # Add specific attributes for a Guitar
        self.num_strings = num_strings
        self.is_acoustic = is_acoustic

    def make_sound(self):
        # Override the parent's make_sound method with a specific sound for Guitar
        return f"{self.name} strums a melodic chord on its {self.num_strings} strings."

# Define the child class 'Piano' which inherits from 'Instrument'
class Piano(Instrument):
    def __init__(self, name, num_keys, has_pedals):
        # Call the parent class constructor to initialize inherited attributes
        super().__init__(name, "Keyboard Instrument")
        # Add specific attributes for a Piano
        self.num_keys = num_keys
        self.has_pedals = has_pedals

    def make_sound(self):
        # Override the parent's make_sound method with a specific sound for Piano
        return f"{self.name} plays a grand tune on its {self.num_keys} keys."

# Function to demonstrate polymorphism
def perform_sound(instrument):
    # This function takes an 'instrument' object and calls its 'make_sound' method.
    # The actual method executed depends on the type of the instrument object.
    print(instrument.make_sound())

# Create instances of the classes
guitar = Guitar("Fender Stratocaster", 6, True)
piano = Piano("Grand Piano", 88, True)
generic_instrument = Instrument("Unknown Instrument", "Percussion")

# Demonstrate polymorphism by calling the 'perform_sound' function with different instrument objects
perform_sound(guitar) # Calls the make_sound method in the Guitar class
perform_sound(piano) # Calls the make_sound method in the Piano class
perform_sound(generic_instrument) # Calls the make_sound method in the Instrument class

