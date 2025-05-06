from typing import Protocol

class WriterOutputProcessor(Protocol):
    readFromFile:str

    def output(self,writeToFile:str)->None:
        ...