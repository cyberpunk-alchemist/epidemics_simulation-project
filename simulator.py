from human import Human
import numpy as np

class Simulator():
    def __init__(self):
        self.n_cities = 2 #pocet mest
        self.city_pop = 100 #pocet lidi ve meste
        self.in_city_int = 30 #interakce v kazdem meste P
        self.out_city_int = 30 # interakce mezi mesty X
        self.imunity_fade = 0.1 #pravdepodobnost ztraty imunity
        self.cure = 0.3 #pravdepodobnost uzdraveni
        self.simulation_steps = 100

        self.city_dict = {}

    def set_params(self,**kwargs):
        self.n_cities = kwargs.get("n_cities",self.n_cities)
        self.city_pop = kwargs.get("city_pop",self.city_pop)
        self.in_city_int = kwargs.get("in_city_int",self.in_city_int)
        self.out_city_int = kwargs.get("out_city_int",self.out_city_int)
        self.imunity_fade = kwargs.get("imunity_fade",self.imunity_fade)
        self.cure = kwargs.get("cure",self.cure)
        self.simulation_steps = kwargs.get("sim_steps",self.simulation_steps)

    def generate_system(self):
        self.city_dict = {}
        for i in range(self.n_cities):
            l = []
            for j in range(self.city_pop):
                l.append(Human(i))

