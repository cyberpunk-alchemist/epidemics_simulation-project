import customtkinter as ctk
from simulator import Simulator

class Interface(ctk.CTk):
    def __init__(self):
        """initialization of the basic layout"""
        super().__init__()
        self.simulator= Simulator()
        #####
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")
        self.title("Simulator Epidemie")
        self.geometry("800x500")

        self.label = ctk.CTkLabel(self, text="Simulator epidemie v1.0",font=("Helvetica",18,"bold"))
        self.label.grid(row=0, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        
        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, padx=(10,10), pady=10, sticky="nsew",columnspan=3)

        button_frame = ctk.CTkFrame(self,width=750,height=50)
        button_frame.grid(row=100, column=0, columnspan=3, padx=10,pady=10, sticky="nsew")

        run_button = ctk.CTkButton(button_frame, text="Spustit", command=self.run_button_callback)
        run_button.place(relx=0.5, rely=0.5, anchor="center")
        self.error_lable = ctk.CTkLabel(button_frame, text="", text_color="red")
        self.error_lable.place(in_=run_button, relx=1.0, x=10, rely=0.5, anchor="w")

    def run_button_callback(self):
        """callback function for running the simulation"""
        try:
            if float(self.scrollable_frame.entry_1.get()) < 0 or float(self.scrollable_frame.entry_2.get()) < 0 or float(self.scrollable_frame.entry_3.get()) < 0 or float(self.scrollable_frame.entry_4.get()) < 0 or float(self.scrollable_frame.entry_7.get()) < 0 or float(self.scrollable_frame.entry_8.get()) < 0:
                self.error_lable.configure(text="Error: Negative values!",text_color="red")
                return
            if float(self.scrollable_frame.entry_5.get()) < 0 or float(self.scrollable_frame.entry_5.get()) > 1 or float(self.scrollable_frame.entry_6.get()) < 0 or float(self.scrollable_frame.entry_6.get()) > 1:
                self.error_lable.configure(text="Error: Probability not in [0,1] range!",text_color="red")
                return

            self.simulator.set_params(
                n_cities = int(self.scrollable_frame.entry_1.get()),
                city_pop = int(self.scrollable_frame.entry_2.get()),
                in_city_int = int(self.scrollable_frame.entry_3.get()),
                out_city_int = int(self.scrollable_frame.entry_4.get()),
                imunity_fade = float(self.scrollable_frame.entry_5.get()),
                cure= float(self.scrollable_frame.entry_6.get()),
                simulation_steps= int(self.scrollable_frame.entry_7.get()),
                init_ill=int(self.scrollable_frame.entry_8.get())
            )

        except:
            self.error_lable.configure(text="Error: Wrong type of entry!",text_color="red")
            return
        try:
            self.simulator.run()
        except:
            self.error_lable.configure(text="Error: Simulation failed!",text_color="red")
            return
        self.error_lable.configure(text="",text_color="red")


class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self,master):
        super().__init__(master,width=750, height=350)
        self.master = master

        self.label = ctk.CTkLabel(self, text="Parametry:", font=("Helvetica",14,"bold"))
        self.label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        
        self.entry_label_1 = ctk.CTkLabel(self, text="Počet měst [N]:")
        self.entry_label_1.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_1 = ctk.CTkEntry(self, width=200, placeholder_text="n_cities")
        self.entry_1.insert(0,str(self.master.simulator.n_cities)) #type: ignore
        self.entry_1.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.entry_label_2 = ctk.CTkLabel(self, text="Populace měst [N]")
        self.entry_label_2.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_2 = ctk.CTkEntry(self, width=200, placeholder_text="city_pop ")
        self.entry_2.insert(0,str(self.master.simulator.city_pop )) #type: ignore
        self.entry_2.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.entry_label_3 = ctk.CTkLabel(self, text="Počet interakcí ve městě [N]:")
        self.entry_label_3.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_3 = ctk.CTkEntry(self, width=200, placeholder_text="in_city_int")
        self.entry_3.insert(0,str(self.master.simulator.in_city_int))#type: ignore
        self.entry_3.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.entry_label_4 = ctk.CTkLabel(self, text="Počet interakcí mezi každými městy [N]:")
        self.entry_label_4.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.entry_4 = ctk.CTkEntry(self, width=200, placeholder_text="out_city_int")
        self.entry_4.insert(0,str(self.master.simulator.out_city_int)) #type: ignore
        self.entry_4.grid(row=6, column=1, padx=10, pady=5, sticky="w") 

        self.entry_label_5 = ctk.CTkLabel(self, text="Pravděpodobnost ztráty imunity [0-1]:")
        self.entry_label_5.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.entry_5 = ctk.CTkEntry(self, width=200, placeholder_text="imunity_fade")
        self.entry_5.insert(0,str(self.master.simulator.imunity_fade))#type: ignore
        self.entry_5.grid(row=7, column=1, padx=10, pady=5, sticky="w") 

        self.entry_label_6 = ctk.CTkLabel(self, text="Pravděpodobnost uzdravení [0-1]:")
        self.entry_label_6.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.entry_6 = ctk.CTkEntry(self, width=200, placeholder_text="cure")
        self.entry_6.insert(0,str(self.master.simulator.cure)) #type: ignore
        self.entry_6.grid(row=9, column=1, padx=10, pady=5, sticky="w") 

        self.entry_label_7 = ctk.CTkLabel(self, text="Počet kroků simulace [N]:")
        self.entry_label_7.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.entry_7 = ctk.CTkEntry(self, width=200, placeholder_text="simulation_steps")
        self.entry_7.insert(0,str(self.master.simulator.simulation_steps)) #type: ignore
        self.entry_7.grid(row=9, column=1, padx=10, pady=5, sticky="w") 

        self.entry_label_8 = ctk.CTkLabel(self, text="Počáteční počet nemocných (město 1) [N]:")
        self.entry_label_8.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.entry_8 = ctk.CTkEntry(self, width=200, placeholder_text="init_ill")
        self.entry_8.insert(0,str(self.master.simulator.init_ill)) #type: ignore
        self.entry_8.grid(row=9, column=1, padx=10, pady=5, sticky="w") 

        