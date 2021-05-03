from random import randint

class Die():
    """Uma class que representa um unico dado"""

    def __init__(self, num_sides=6):
        """Supoe que seja um dado de seis lados"""
        self.num_sides = num_sides


    def roll(self):
        """Devolve um valor aleatorio entre 1 e o numero de lados"""
        return randint(1, self.num_sides)