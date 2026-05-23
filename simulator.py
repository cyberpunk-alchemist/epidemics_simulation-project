from human import Human, States
import numpy as np
from visualizer import Visualizer

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

        self.save_results = True
        self.filename = "results"

        self.human_matrix = []
        self.infected_index_list = []
        self.imune_index_list = []
        self.results_total = [] # matice počtu lidí, kde řádky představují (V,N,I)
        self.results_per_city = [] # matice počtu lidí, pro jednotlivá města, kde řádky představují (V_0,N_0,I_0,V_1,N_1,I_1, ...)
        

    def set_params(self,**kwargs):
        self.n_cities = kwargs.get("n_cities",self.n_cities)
        self.city_pop = kwargs.get("city_pop",self.city_pop)
        self.in_city_int = kwargs.get("in_city_int",self.in_city_int)
        self.out_city_int = kwargs.get("out_city_int",self.out_city_int)
        self.imunity_fade = kwargs.get("imunity_fade",self.imunity_fade)
        self.cure = kwargs.get("cure",self.cure)
        self.simulation_steps = kwargs.get("sim_steps",self.simulation_steps)
        self.init_ill = kwargs.get("init_ill",self.init_ill)
        self.filename = kwargs.get("filename",self.filename)

    def generate_system(self):
        self.human_matrix = []
        self.infected_index_list = []
        self.imune_index_list = []
        for i in range(self.n_cities):
            matrix_line = []
            for j in range(self.city_pop):
                matrix_line.append(Human((i,j)))
            self.human_matrix.append(matrix_line)
        
        for k in range(self.init_ill):
            self.human_matrix[0][k].infect()
            self.infected_index_list.append((0,k))

    def interaction(self, human1: Human, human2: Human):
        if human1.state == States.N:
            if human2.state == States.V:
                human2.infect()
                self.infected_index_list.append(human2.ID)
        elif human1.state == States.V:
            if human2.state == States.N:
                human1.infect()
                self.infected_index_list.append(human1.ID)

    def city_interaction(self,ncity):
        for i in range(self.in_city_int):
            rnd1 = 1
            rnd2 = 1
            while rnd1 == rnd2:
                rnd1 = np.random.randint(self.city_pop)
                rnd2 = np.random.randint(self.city_pop)
            self.interaction(self.human_matrix[ncity][rnd1],self.human_matrix[ncity][rnd2])

    def city_city_interaction(self,ncity1,ncity2):
        for i in range(self.out_city_int):
            rnd1 = np.random.randint(self.city_pop)
            rnd2 = np.random.randint(self.city_pop)
            self.interaction(self.human_matrix[ncity1][rnd1],self.human_matrix[ncity2][rnd2])
    
    def store_data(self):
        per_city = []
        for i in range(self.n_cities):
            n_N = 0
            for j in self.infected_index_list:
                if j[0] == i:
                    n_N +=1
            n_I = 0
            for j in self.imune_index_list:
                if j[0] == i:
                    n_I +=1
            n_V = self.city_pop-n_N-n_I
            per_city.append(n_V)
            per_city.append(n_N)
            per_city.append(n_I)
        self.results_per_city.append(per_city)
        self.results_total.append([self.city_pop*self.n_cities-len(self.infected_index_list)-len(self.imune_index_list),len(self.infected_index_list),len(self.imune_index_list)])

    def save_data_to_file(self,filename: str):
        str1 = """"""
        str2 = """"""
        for i in range(len(self.results_total)):
            str1 = str1 + str(self.results_total[i]).strip()[1:-1].replace(","," ")+ "\n"
            str2 = str2 + str(self.results_per_city[i]).strip()[1:-1].replace(","," ") + "\n"
        with open(f"{filename}.tot.txt","w") as f:
            f.write(str1)
        with open(f"{filename}.per_city.txt","w") as f:
            f.write(str2)
    
    def run(self):
        self.results_per_city = []
        self.results_total = []
        self.generate_system()
        for i in range(self.simulation_steps):
            for city_index in range(self.n_cities):
                self.city_interaction(city_index)
                for city_index_2 in range(city_index+1,self.n_cities): # for all city_index_2 > city_index
                    self.city_city_interaction(city_index,city_index_2)
            for imune_index in self.imune_index_list[:]:
                if np.random.rand() < self.cure:
                    self.human_matrix[imune_index[0]][imune_index[1]].fade()
                    self.imune_index_list.remove(imune_index)
            for ill_index in self.infected_index_list[:]:
                if np.random.rand() < self.cure:
                    self.human_matrix[ill_index[0]][ill_index[1]].cure()
                    self.infected_index_list.remove(ill_index)
                    self.imune_index_list.append(ill_index)

            self.store_data()
            if (i+1)%10 == 0:
                print(f"{i+1}/{self.simulation_steps} steps calculated")
        if self.save_results:
            self.save_data_to_file(self.filename)
        viz = Visualizer()
        viz.load_data(self.filename+".tot.txt",self.filename+".per_city.txt")
        viz.plot_data(True)
        
