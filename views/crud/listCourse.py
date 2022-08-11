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

            self.tree = ttk.Treeview(self)

            # Define the columns of the treeview
            self.tree["columns"] = (
                "Id", "Curso", "Prerrequisitos", "Obligatoriedad", "Semestre", "Créditos", "Estado")

            # Define the width of the columns
            self.tree.column("#0", width=0, stretch=NO)
            self.tree.column("Id", width=50, minwidth=50, anchor=CENTER)
            self.tree.column("Curso", width=200, minwidth=200, anchor=CENTER)
            self.tree.column("Prerrequisitos", width=200,
                             minwidth=200, anchor=CENTER)
            self.tree.column("Obligatoriedad", width=100,
                             minwidth=100, anchor=CENTER)
            self.tree.column("Semestre", width=100,
                             minwidth=100, anchor=CENTER)
            self.tree.column("Créditos", width=100,
                             minwidth=100, anchor=CENTER)
            self.tree.column("Estado", width=100, minwidth=100, anchor=CENTER)

            # Define the headings of the columns
            self.tree.heading("#0", text="", anchor=W)
            self.tree.heading("Id", text="Id", anchor=W)
            self.tree.heading("Curso", text="Curso", anchor=W)
            self.tree.heading("Prerrequisitos",
                              text="Prerrequisitos", anchor=W)
            self.tree.heading("Obligatoriedad",
                              text="Obligatoriedad", anchor=W)
            self.tree.heading("Semestre", text="Semestre", anchor=W)
            self.tree.heading("Créditos", text="Créditos", anchor=W)
            self.tree.heading("Estado", text="Estado", anchor=W)

            # Configure tags
            self.tree.tag_configure("odd", background="white")
            self.tree.tag_configure("even", background="lightgray")

            # Insert the data into the treeview
            self.listCourse(self, self.tree, self.courses)

            # Pack the treeview
            self.tree.grid(row=0, column=0, sticky="nsew")
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

    @staticmethod
    def listCourse(self, tree, courses):
        # List of options to elegibility of the course
        elegibilityCourse = {
            0: "Obligatorio",
            1: "Opcional"
        }
        # List of options to state of the course
        stateCourse = {
            0: "Aprobado",
            1: "Cursando",
            - 1: "Pendiente"
        }

        global count
        count = 0
        for course in courses:

            if count % 2 == 0:
                tree.insert("", "end", values=(course.idCourse, course.name, course.idCoursesRequired,
                                               elegibilityCourse[course.isRequired], course.semester, course.credits, stateCourse[course.currentState]), tags=("even"))
            else:
                tree.insert("", "end", values=(course.idCourse, course.name, course.idCoursesRequired,
                                               elegibilityCourse[course.isRequired], course.semester, course.credits, stateCourse[course.currentState]), tags=("odd"))
            count += 1
