import matplotlib.pyplot as plt
from typing import List
import matplotlib.image as mpimg

class Visualizer():
    def __init__(self):
        self.x = []
        self.N = []
        self.I = []
        self.V = []
        self.N_per_city = []
        self.I_per_city = []
        self.V_per_city = []
        self.ncities = 0
        self.name = ""

    def load_data(self, filename_tot, filename_per_city):
        """insert full filenames"""
        self.x = []
        self.N = []
        self.I = []
        self.V = []
        self.N_per_city = []
        self.I_per_city = []
        self.V_per_city = []
        self.name = filename_per_city.split(".")[0]
        with open(filename_tot,"r") as f:
            lines = f.readlines()
            for line in lines:
                ll = line.split()
                self.V.append(int(ll[0]))
                self.N.append(int(ll[1]))
                self.I.append(int(ll[2]))
        with open(filename_per_city,"r") as f:
            lines = f.readlines()
            for i,line in enumerate(lines):
                self.x.append(i)
                ll = line.split()
                if i == 0: 
                    self.ncities = int(len(ll)/3)
                    for i in range(self.ncities):
                        self.N_per_city.append([])
                        self.I_per_city.append([])
                        self.V_per_city.append([])
                for j in range(self.ncities):
                    self.V_per_city[j].append(int(ll[0+j*3]))
                    self.N_per_city[j].append(int(ll[1+j*3]))
                    self.I_per_city[j].append(int(ll[2+j*3]))

    def plot_data(self,save):
        if self.ncities == 0:
            raise ValueError("No data vere loaded!")
        
        for i in range(self.ncities):
            fig, ax = plt.subplots()
            ax.set_xlabel("Časové kroky [N]")
            ax.set_ylabel("Počet lidí [N]")
            ax.set_title(f"Vývoj nemoci ve městě {i+1}")
            ax.plot(self.x, self.V_per_city[i], label="Vnímaví",color="#437C90")
            ax.plot(self.x, self.N_per_city[i], label="Nemocní",color="#DD614A")
            ax.plot(self.x, self.I_per_city[i], label="Imunní",color="#A69658")
            ax.legend()
            fig.savefig(f"plots/{self.name}-city_{i+1}", dpi=300, bbox_inches="tight")
            plt.close(fig)
        
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel("Časové kroky [N]")
        self.ax.set_ylabel("Počet lidí [N]")
        self.ax.set_title("Vývoj nemoci v celkové populaci")
        self.ax.plot(self.x, self.V, label="Vnímaví",color="#437C90")
        self.ax.plot(self.x, self.N, label="Nemocní",color="#DD614A")
        self.ax.plot(self.x, self.I, label="Imunní",color="#A69658")
        self.ax.legend()
        fig.savefig(f"plots/{self.name}-total", dpi=300, bbox_inches="tight")
        plt.show()


