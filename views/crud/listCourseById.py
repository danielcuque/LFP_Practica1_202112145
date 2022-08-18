import re
import customtkinter as ctk
from tkinter import messagebox
from tkinter import *


from model.credits.coursesByStudent import CoursesByStudent


class ListCourseById(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()
        self.master = master

        #  configure grid layout (2x1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Variable to store the id of the course
        self.id_course = StringVar()

        # Creating the title label
        self.titleLabel = ctk.CTkLabel(master=self,
                                       text="Listado de cursos por código",
                                       height=50,
                                       corner_radius=6,
                                       text_font=("Roboto Medium", -25), text_color="white",
                                       fg_color=("white", "gray38"),
                                       justify=LEFT)
        self.titleLabel.grid(
            column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.grid(column=0, row=1, sticky="nwe", padx=15, pady=15)

        # Creating custom grid layout
        self.frame_info.rowconfigure(0, weight=1, minsize=70)
        self.frame_info.rowconfigure((1, 2, 3, 4, 5, 6, 7), weight=1)

        self.frame_info.columnconfigure((0, 1), weight=1)

        # Creating the label for the id
        self.id_entry = ctk.CTkEntry(
            textvariable=self.id_course, master=self.frame_info, width=20)

        self.id_entry.grid(column=0, columnspan=2, row=0,
                           sticky="nwe", padx=15, pady=15)

        self.search_button = ctk.CTkButton(
            master=self.frame_info,
            text="Buscar por código",
            width=20,
            height=2,
            corner_radius=6,
            text_font=("Roboto Medium", -15),
            text_color="white",
            fg_color=("white", "gray38"),
            bg_color=("white", "gray38"),
            command=self.search_by_id
        )

        self.search_button.grid(
            column=2, row=0, sticky="nwe", padx=15, pady=15)

    def search_by_id(self):
        data = CoursesByStudent()
        id_course_info = self.id_course.get()
        if id_course_info == "" or re.fullmatch(data.allowValuesForId, id_course_info) is None:
            messagebox.showerror(
                "Error", "El código no puede estar vacío y debe ser un número entero")
        else:
            course = data.getCourseById(int(id_course_info))
            if course is None:

                messagebox.showerror(
                    "Error", "No se encontró el curso con el código ingresado")
            else:
                self.id_course_label = ctk.CTkLabel(
                    master=self.frame_info, text="Código: " + str(course.getIdCourse()), width=20,
                    height=2,
                    corner_radius=6,
                    text_font=("Roboto Medium", -15), text_color="white",
                    justify=LEFT)
                self.id_course_label.grid(
                    column=0, row=1, sticky="nwe", columnspan=3, padx=15, pady=15)

                self.name_course_label = ctk.CTkLabel(
                    master=self.frame_info, text="Nombre: " + str(course.getName()), width=20,
                    height=2,
                    corner_radius=6,
                    text_font=("Roboto Medium", -15), text_color="white",
                    justify=LEFT)
                self.name_course_label.grid(
                    column=0, row=2, sticky="nwe", columnspan=3, padx=15, pady=15)

                self.id_courses_required_label = ctk.CTkLabel(
                    master=self.frame_info, text="Cursos requeridos: " + str(course.getIdCoursesRequired()), width=20,
                    height=2,
                    corner_radius=6,
                    text_font=("Roboto Medium", -15), text_color="white",
                    justify=LEFT)
                self.id_courses_required_label.grid(
                    column=0, row=3, sticky="nwe", columnspan=3, padx=15, pady=15)

                self.is_required_label = ctk.CTkLabel(
                    master=self.frame_info, text="Es requerido: " + data.elegibilityCourse[course.getIsRequired()], width=20,
                    height=2,
                    corner_radius=6,
                    text_font=("Roboto Medium", -15), text_color="white",
                    justify=LEFT)
                self.is_required_label.grid(
                    column=0, row=4, sticky="nwe", columnspan=3, padx=15, pady=15)

                self.semester = ctk.CTkLabel(
                    master=self.frame_info, text="Semestre: " + str(course.getSemester()), width=20,
                    height=2,
                    corner_radius=6,
                    text_font=("Roboto Medium", -15), text_color="white",
                    justify=LEFT)
                self.semester.grid(
                    column=0, row=5, sticky="nwe", columnspan=3, padx=15, pady=15)

                self.credits = ctk.CTkLabel(
                    master=self.frame_info, text="Créditos: " + str(course.getCredits()), width=20,
                    height=2,
                    corner_radius=6,
                    text_font=("Roboto Medium", -15), text_color="white",
                    justify=LEFT)
                self.credits.grid(
                    column=0, row=6, sticky="nwe", columnspan=3, padx=15, pady=15)

                self.current_state = ctk.CTkLabel(
                    master=self.frame_info, text="Estado: " + data.stateCourse[course.getCurrentState()], width=20,
                    height=2,
                    corner_radius=6,
                    text_font=("Roboto Medium", -15), text_color="white",
                    justify=LEFT)
                self.current_state.grid(
                    column=0, row=7, sticky="nwe", columnspan=3, padx=15, pady=15)
