# Abstract assignment
# Abstract method
from abc import ABC, abstractmethod
class music(ABC):
    def blues(self, instrument):
        print("The blues sounds good on: ",instrument)
        @abstractmethod
        def style(self, guitar):
            pass
# regular method with child class
class guitar(music):
    def accompaniment(self, instrument):
        print("The blues also sounds good on the {} because it's sad".format(instrument))
# object creation utilizing both
obj = guitar()
obj.blues("guitar")
obj.accompaniment("trumpet")
