import customtkinter as ctk
from tkinter import LEFT


class CreateCourse(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()

        self.master = master

        #  configure grid layout (1x1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.label_info_1 = ctk.CTkLabel(master=self,
                                         text="Crear cursos",
                                         height=100,
                                         corner_radius=6,  # <- custom corner radius
                                         # <- custom tuple-color
                                         fg_color=("white", "gray38"),
                                         justify=LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
