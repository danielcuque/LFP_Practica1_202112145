from re import S
from tkinter import messagebox
import customtkinter as ctk
from tkinter import *


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

        # Create the variables to store the data
        self.id_course = ctk.StringVar()
        self.name_course = ctk.StringVar()
        self.pre_course = ctk.StringVar()
        self.semester = ctk.StringVar()
        self.optionality = ctk.StringVar()
        self.credits = ctk.StringVar()
        self.current_state = ctk.StringVar()

        # Create a frame to store the fields
        self.frame_info = ctk.CTkFrame(self)

        # configure grid layout (8x2)
        self.frame_info.grid_columnconfigure((0, 1), weight=1)
        self.frame_info.grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.frame_info.grid(column=0, row=1, sticky="nswe")

        '''Creating form to create a course'''

        # Create a label and Entry for the ID course
        self.idLabel = ctk.CTkLabel(master=self.frame_info, text="Código:", width=10, height=1, corner_radius=6,
                                    text_font=("Roboto Medium", -15), text_color="white",
                                    fg_color=("white", "gray38"), justify=LEFT)
        self.idLabel.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.idText = ctk.CTkEntry(master=self.frame_info, width=10, height=1, corner_radius=6,
                                   textvariable=self.id_course,
                                   text_font=("Roboto Medium", -15), text_color="white",
                                   fg_color=("white", "gray38"), justify=LEFT)
        self.idText.grid(column=1, row=0, sticky="nwe", padx=15, pady=15)

        # Create a label and Entry for the name course
        self.nameLabel = ctk.CTkLabel(master=self.frame_info, text="Nombre:", width=10, height=1, corner_radius=6,
                                      text_font=("Roboto Medium", -15), text_color="white",
                                      fg_color=("white", "gray38"), justify=LEFT)
        self.nameLabel.grid(
            column=0, row=1, sticky="nwe", padx=15, pady=15)

        self.nameText = ctk.CTkEntry(master=self.frame_info, width=10, height=1, corner_radius=6,
                                     textvariable=self.name_course,
                                     text_font=("Roboto Medium", -15), text_color="white",
                                     fg_color=("white", "gray38"), justify=LEFT)
        self.nameText.grid(column=1, row=1, sticky="nwe", padx=15, pady=15)

        # Create a label and Entry for the precourse field
        self.preCourseLabel = ctk.CTkLabel(master=self.frame_info, text="Pre-curso:", width=10, height=1, corner_radius=6,
                                           text_font=("Roboto Medium", -15), text_color="white",
                                           fg_color=("white", "gray38"), justify=LEFT)
        self.preCourseLabel.grid(
            column=0, row=2, sticky="nwe", padx=15, pady=15)
        self.preCourseText = ctk.CTkEntry(master=self.frame_info, width=10, height=1, corner_radius=6,
                                          textvariable=self.pre_course,
                                          text_font=("Roboto Medium", -15), text_color="white",
                                          fg_color=("white", "gray38"), justify=LEFT)

        self.preCourseText.grid(
            column=1, row=2, sticky="nwe", padx=15, pady=15)

        # Create a label and Entry for the semester field
        self.semesterLabel = ctk.CTkLabel(master=self.frame_info, text="Semestre:", width=10, height=1, corner_radius=6,
                                          text_font=("Roboto Medium", -15), text_color="white",
                                          fg_color=("white", "gray38"), justify=LEFT)
        self.semesterLabel.grid(
            column=0, row=3, sticky="nwe", padx=15, pady=15)

        self.semesterText = ctk.CTkEntry(master=self.frame_info, width=10, height=1, corner_radius=6,
                                         textvariable=self.semester,
                                         text_font=("Roboto Medium", -15), text_color="white",
                                         fg_color=("white", "gray38"), justify=LEFT)
        self.semesterText.grid(
            column=1, row=3, sticky="nwe", padx=15, pady=15)

        # Create a label and Entry for optionality field
        self.optionalityLabel = ctk.CTkLabel(master=self.frame_info, text="Obligatorio:", width=10, height=1, corner_radius=6,
                                             text_font=("Roboto Medium", -15), text_color="white",
                                             fg_color=("white", "gray38"), justify=LEFT)
        self.optionalityLabel.grid(
            column=0, row=4, sticky="nwe", padx=15, pady=15)

        self.optionalityMenu = ctk.CTkOptionMenu(master=self.frame_info,
                                                 values=[
                                                     "Obligatorio", "Opcional"],
                                                 variable=self.optionality,
                                                 width=10, height=1, corner_radius=6,
                                                 text_font=("Roboto Medium", -15), text_color="white",
                                                 fg_color=("white", "gray38"))

        self.optionalityMenu.grid(
            column=1, row=4, sticky="nwe", padx=15, pady=15)

        # Create a label and Entry for the credits field
        self.creditsLabel = ctk.CTkLabel(master=self.frame_info, text="Creditos:", width=10, height=1, corner_radius=6,
                                         text_font=("Roboto Medium", -15), text_color="white",
                                         fg_color=("white", "gray38"), justify=LEFT)
        self.creditsLabel.grid(
            column=0, row=5, sticky="nwe", padx=15, pady=15)
        self.creditsText = ctk.CTkEntry(master=self.frame_info, width=10, height=1, corner_radius=6,
                                        textvariable=self.credits,
                                        text_font=("Roboto Medium", -15), text_color="white",
                                        fg_color=("white", "gray38"), justify=LEFT)
        self.creditsText.grid(
            column=1, row=5, sticky="nwe", padx=15, pady=15)

        # Create a label and Entry for the state field
        self.state = ctk.CTkLabel(master=self.frame_info, text="Estado:", width=10, height=1, corner_radius=6,
                                  text_font=("Roboto Medium", -15), text_color="white",
                                  fg_color=("white", "gray38"), justify=LEFT)
        self.state.grid(
            column=0, row=6, sticky="nwe", padx=15, pady=15)
        self.currentStateMenu = ctk.CTkOptionMenu(master=self.frame_info, width=10, height=1, corner_radius=6,
                                                  variable=self.current_state,
                                                  values=[
                                                      "Aprobado", "Cursando", "Pendiente"], text_font=("Roboto Medium", -15), text_color="white",
                                                  fg_color=("white", "gray38"))
        self.currentStateMenu.grid(
            column=1, row=6, sticky="nwe", padx=15, pady=15)

        # Create a button to add a new course
        self.button_add = ctk.CTkButton(master=self.frame_info, text="Agregar", width=10, height=1, corner_radius=6,
                                        command=self.create_course,
                                        text_font=("Roboto Medium", -15), text_color="white",
                                        fg_color=("white", "gray38"))
        self.button_add.grid(
            columnspan=2,
            column=0, row=7, sticky="nwe", padx=15, pady=15)

        # Set initial values for OptionMenus
        self.currentStateMenu.set("Pendiente")
        self.optionalityMenu.set("Obligatorio")

    def create_course(self):
        data = CoursesByStudent()
        id_course_info = self.id_course.get()
        name_course_info = self.name_course.get()
        pre_course_info = self.pre_course.get()
        semester_info = self.semester.get()
        optionality_info = self.optionality.get()
        credits_info = self.credits.get()
        state_info = self.current_state.get()
        isCreated = data.createCourseByForm(id_course_info, name_course_info, pre_course_info,
                                            semester_info, optionality_info, credits_info, state_info)
        if len(isCreated) == 0:
            messagebox.showinfo(
                "Agregar curso", "Curso agregado correctamente")
            self.clear_fields()
        else:
            messagebox.showerror("Agregar curso", "Error al agregar curso")

    def clear_fields(self):
        self.id_course.set("")
        self.name_course.set("")
        self.pre_course.set("")
        self.semester.set("")
        self.optionality.set("")
        self.credits.set("")
        self.current_state.set("")
