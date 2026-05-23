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
        self.init_ill = 10 #pocet lidi kteri jsou nemocni na pocatku simulace (v meste 1)

        self.human_list = []

    def set_params(self,**kwargs):
        self.n_cities = kwargs.get("n_cities",self.n_cities)
        self.city_pop = kwargs.get("city_pop",self.city_pop)
        self.in_city_int = kwargs.get("in_city_int",self.in_city_int)
        self.out_city_int = kwargs.get("out_city_int",self.out_city_int)
        self.imunity_fade = kwargs.get("imunity_fade",self.imunity_fade)
        self.cure = kwargs.get("cure",self.cure)
        self.simulation_steps = kwargs.get("sim_steps",self.simulation_steps)
        self.init_ill = kwargs.get("init_ill",self.simulation_steps)

    def generate_system(self):
        self.human_list = []
        for i in range(self.n_cities):
            for j in range(self.city_pop):
                self.human_list.append(Human(i))
        for i in range(5):
            self.human_list[i].infect()

    def run(self):
        #######################################
        print([self.n_cities,
        self.city_pop,
        self.in_city_int,
        self.out_city_int,
        self.imunity_fade,
        self.cure,
        self.simulation_steps,
        self.init_ill])
        ########################################
        for i in range(self.simulation_steps):
            ...
                

