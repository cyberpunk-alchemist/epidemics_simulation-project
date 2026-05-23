import numpy as np
from enum import Enum

class States(Enum):
    V = "vnimavyy"
    N = "nemocny"
    I = "imunni"



class Human():
    def __init__(self,ID: tuple):
        """stores info about city residence and a state
        ID should be a tuple of (city_ID, person_ID)"""
        self.ID=ID 
        self.state=States.V
    
    def cure(self):
        self.state = States.I

    def infect(self):
        self.state = States.N

    def fade(self):
        self.state = States.V

        
        