import customtkinter as ctk
from tkinter import *
from tkinter import ttk

# Import data
from model.credits.coursesByStudent import CoursesByStudent


class ListCourse(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()

        self.master = master
        data = CoursesByStudent()
        self.courses = data.coursesData

        #  configure grid layout (1x1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        if (len(self.courses) > 0):

            # Create a TreeView Scroll
            # self.scrollTable = ctk.CTkScrollbar(self)
            # self.scrollTable.pack(side=RIGHT)

            # Create a TreeView
            self.dataTable = ttk.Treeview(
                self)
            self.dataTable.grid(row=0, column=0, sticky="nsew")

            # Configure the scrollbar
            # self.scrollTable.config(command=self.dataTable.yview)

            # self.tree["columns"] = (
            #     "ID", "Nombre", "Cursos requeridos", "Opcional", "Semestre", "Créditos", "Estado")

            # self.tree.column("ID", width=50, anchor="center")
            # self.tree.column("Nombre", width=200, anchor="center")
            # self.tree.column("Cursos requeridos", width=200, anchor="center")
            # self.tree.column("Opcional", width=200, anchor="center")
            # self.tree.column("Semestre", width=200, anchor="center")
            # self.tree.column("Créditos", width=200, anchor="center")
            # self.tree.column("Estado", width=200, anchor="center")

            # self.tree.heading("ID", text="ID")
            # self.tree.heading("Nombre", text="Nombre")
            # self.tree.heading("Cursos requeridos", text="Cursos requeridos")
            # self.tree.heading("Opcional", text="Opcional")
            # self.tree.heading("Semestre", text="Semestre")
            # self.tree.heading("Créditos", text="Créditos")
            # self.tree.heading("Estado", text="Estado")

            self.dataTable.tag_configure("odd", background="gray25")
            self.dataTable.tag_configure("even", background="gray45")

            # # Fill the treeview with data
            global count
            count = 0
            for course in self.courses:
                if count % 2 == 0:
                    self.dataTable.insert(parent="", index="end", values=(course.idCourse, course.name, course.idCoursesRequired, course.isRequired,
                                                                          course.semester, course.credits, course.currentState), tags=("even"))
                else:
                    self.dataTable.insert(parent="", index="end", values=(course.idCourse, course.name, course.idCoursesRequired, course.isRequired,
                                                                          course.semester, course.credits, course.currentState), tags=("odd"))
                count += 1

        else:
            self.label_info_2 = ctk.CTkLabel(master=self,
                                             text="No hay cursos registrados",
                                             height=100,
                                             corner_radius=6,  # <- custom corner radius
                                             # <- custom tuple-color
                                             fg_color=("white", "gray38"),
                                             justify=LEFT)
            self.label_info_2.grid(
                column=0, row=0, sticky="nwe", padx=15, pady=15)
