import customtkinter as ctk
from tkinter import LEFT


from model.credits.coursesByStudent import CoursesByStudent


class CreateCourse(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()

        self.master = master

        data = CoursesByStudent()
        self.courses = data.coursesData
        #  configure grid layout (2x1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.titleLabel = ctk.CTkLabel(master=self,
                                       text="Crear curso",
                                       height=50,
                                       corner_radius=6,
                                       text_font=("Roboto Medium", -25), text_color="white",
                                       fg_color=("white", "gray38"),
                                       justify=LEFT)
        self.titleLabel.grid(
            column=0, row=0, sticky="nwe", padx=15, pady=15)

        if (len(self.courses) > 0):
            self.frame_info = ctk.CTkFrame(self)

            # configure grid layout (7x2)
            self.frame_info.grid_columnconfigure((0, 1), weight=1)
            self.frame_info.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
            self.frame_info.grid(column=0, row=1, sticky="nswe")

        else:
            self.label_info_2 = ctk.CTkLabel(master=self,
                                             text="No hay cursos registrados",
                                             corner_radius=6,
                                             fg_color=("white", "gray38"),
                                             justify=LEFT)
            self.label_info_2.grid(
                column=0, row=1, sticky="nswe", padx=15, pady=5)
