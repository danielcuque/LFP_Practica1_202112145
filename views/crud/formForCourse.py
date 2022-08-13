from tkinter import messagebox
import customtkinter as ctk
from tkinter import *


from model.credits.coursesByStudent import CoursesByStudent


class FormForCourse(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__()

        self.master = master

        data = CoursesByStudent()
        self.courses = data.coursesData

        #  configure grid layout (2x1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Create the variables to store the data
        self.id_course = ctk.StringVar()
        self.name_course = ctk.StringVar()
        self.pre_course = ctk.StringVar()
        self.semester = ctk.StringVar()
        self.optionality = ctk.StringVar()
        self.credits = ctk.StringVar()
        self.current_state = ctk.StringVar()

        self.titleLabel = ctk.CTkLabel(master=self,
                                       text=title,
                                       height=50,
                                       corner_radius=6,
                                       text_font=("Roboto Medium", -25), text_color="white",
                                       fg_color=("white", "gray38"),
                                       justify=LEFT)
        self.titleLabel.grid(
            column=0, row=0, sticky="nwe", padx=15, pady=15)

        # Create a frame to store the fields
        self.frame_info = ctk.CTkFrame(master=self)

        # self.frame_info = FormForCourse(self)
        self.frame_info.grid(column=0, row=1, sticky="nswe", padx=15, pady=15)
        self.frame_info.grid_columnconfigure((0, 1), weight=1)
        self.frame_info.grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        '''Creating form to create a course'''

        '''Creating Labels'''
        self.idLabel = ctk.CTkLabel(master=self.frame_info, text="Código:", width=10, height=1, corner_radius=6,
                                    text_font=("Roboto Medium", -15), text_color="white",
                                    justify=LEFT)
        self.idLabel.grid(column=0, row=0, padx=15, pady=15)

        # Create a label for the name course
        self.nameLabel = ctk.CTkLabel(master=self.frame_info, text="Nombre:", width=10, height=1, corner_radius=6,
                                      text_font=("Roboto Medium", -15), text_color="white",
                                      justify=LEFT)
        self.nameLabel.grid(
            column=0, row=1,  padx=15, pady=15)

        # Create a label for the precourse field
        self.preCourseLabel = ctk.CTkLabel(master=self.frame_info, text="Pre-curso:", width=10, height=1, corner_radius=6,
                                           text_font=("Roboto Medium", -15), text_color="white",
                                           justify=LEFT)
        self.preCourseLabel.grid(
            column=0, row=2,  padx=15, pady=15)

        # Create a label for the semester field
        self.semesterLabel = ctk.CTkLabel(master=self.frame_info, text="Semestre:", width=10, height=1, corner_radius=6,
                                          text_font=("Roboto Medium", -15), text_color="white", justify=LEFT)
        self.semesterLabel.grid(column=0, row=3,  padx=15, pady=15)

        self.optionalityLabel = ctk.CTkLabel(master=self.frame_info, text="Obligatorio:", width=10, height=1, corner_radius=6,
                                             text_font=("Roboto Medium", -15), text_color="white",
                                             justify=LEFT)
        self.optionalityLabel.grid(
            column=0, row=4, sticky="nwe", padx=15, pady=15)

        # Create a label for the credits field
        self.creditsLabel = ctk.CTkLabel(master=self.frame_info, text="Creditos:", width=10, height=1, corner_radius=6,
                                         text_font=("Roboto Medium", -15), text_color="white",
                                         justify=LEFT)
        self.creditsLabel.grid(
            column=0, row=5, sticky="nwe", padx=15, pady=15)

        # Create a label and Entry for the state field
        self.stateLabel = ctk.CTkLabel(master=self.frame_info, text="Estado:", width=10, height=1, corner_radius=6,
                                       text_font=("Roboto Medium", -15), text_color="white",
                                       justify=LEFT)
        self.stateLabel.grid(
            column=0, row=6, sticky="nwe", padx=15, pady=15)

        '''Creating Entry fields'''
        self.idText = ctk.CTkEntry(master=self.frame_info, width=200, height=25, corner_radius=6,
                                   textvariable=self.id_course,
                                   text_font=("Roboto Medium", -15), text_color="white",
                                   fg_color=("white", "gray38"), justify=LEFT)
        self.idText.grid(column=1, row=0, sticky="nwe",
                         padx=(0, 55), pady=(5, 0))

        self.nameText = ctk.CTkEntry(master=self.frame_info, height=25,  corner_radius=6,
                                     textvariable=self.name_course,
                                     text_font=("Roboto Medium", -15), text_color="white",
                                     fg_color=("white", "gray38"), justify=LEFT)
        self.nameText.grid(column=1, row=1, sticky="nwe",
                           padx=(0, 55), pady=(5, 0))

        self.preCourseText = ctk.CTkEntry(master=self.frame_info, height=25,  corner_radius=6,
                                          textvariable=self.pre_course,
                                          text_font=("Roboto Medium", -15), text_color="white",
                                          fg_color=("white", "gray38"), justify=LEFT)

        self.preCourseText.grid(
            column=1, row=2, sticky="nwe", padx=(0, 55), pady=(5, 0))

        self.semesterText = ctk.CTkEntry(master=self.frame_info, height=25,  corner_radius=6,
                                         textvariable=self.semester,
                                         text_font=("Roboto Medium", -15), text_color="white",
                                         fg_color=("white", "gray38"), justify=LEFT)
        self.semesterText.grid(
            column=1, row=3, sticky="nwe", padx=(0, 55), pady=(5, 0))

        # Create a label and Entry for optionality field
        self.optionalityMenu = ctk.CTkOptionMenu(master=self.frame_info,
                                                 values=[
                                                     "Obligatorio", "Opcional"],
                                                 variable=self.optionality,
                                                 height=25, corner_radius=6,
                                                 text_font=("Roboto Medium", -15), text_color="white",
                                                 fg_color=("white", "gray38"))

        self.optionalityMenu.grid(
            column=1, row=4, sticky="nwe", padx=(0, 55), pady=(5, 0))

        # Create a label and Entry for the credits field
        self.creditsText = ctk.CTkEntry(master=self.frame_info, height=25, corner_radius=6,
                                        textvariable=self.credits,
                                        text_font=("Roboto Medium", -15), text_color="white",
                                        fg_color=("white", "gray38"), justify=LEFT)
        self.creditsText.grid(
            column=1, row=5, sticky="nwe", padx=(0, 55), pady=(5, 0))

        self.currentStateMenu = ctk.CTkOptionMenu(master=self.frame_info, height=25, corner_radius=6,
                                                  variable=self.current_state,
                                                  values=[
                                                      "Aprobado", "Cursando", "Pendiente"], text_font=("Roboto Medium", -15), text_color="white",
                                                  fg_color=("white", "gray38"))
        self.currentStateMenu.grid(
            column=1, row=6, sticky="nwe", padx=(0, 55), pady=(5, 0))

        # Create a button to add a new course
        if title == "Crear curso":
            self.button_add = ctk.CTkButton(master=self.frame_info, text="Agregar", width=10, height=1, corner_radius=6,
                                            command=self.create_course,
                                            text_font=("Roboto Medium", -15), text_color="white",
                                            fg_color=("white", "gray38"))
            self.button_add.grid(
                column=1, row=7, sticky="nwe", padx=(0, 55), pady=(5, 0))
        else:
            if data.getLengthCoursesData() > 0:
                self.enable_fields()
                self.button_update = ctk.CTkButton(master=self.frame_info, text="Actualizar", width=10, height=1, corner_radius=6,
                                                   command=self.update_course,
                                                   text_font=("Roboto Medium", -15), text_color="white",
                                                   fg_color=("white", "gray38"))
                self.button_update.grid(
                    column=1, row=7, sticky="nwe", padx=(0, 55), pady=(5, 0))
            else:
                self.labelInformation = ctk.CTkLabel(master=self.frame_info, text="No hay cursos registrados", width=10, height=1, corner_radius=6,
                                                     text_font=("Roboto Medium", -15), text_color="white",
                                                     justify=LEFT)
                self.labelInformation.grid(
                    column=1, row=7, sticky="nwe", padx=(0, 55), pady=(5, 0))
                self.disable_fields()

        # Set initial values for OptionMenus
        self.currentStateMenu.set("Pendiente")
        self.optionalityMenu.set("Obligatorio")

    def clear_fields(self):
        self.id_course.set("")
        self.name_course.set("")
        self.pre_course.set("")
        self.semester.set("")
        self.credits.set("")
        self.current_state.set("")
        self.optionality.set("")

    def disable_fields(self):
        self.idText.configure(state="disabled")
        self.nameText.configure(state="disabled")
        self.preCourseText.configure(state="disabled")
        self.semesterText.configure(state="disabled")
        self.creditsText.configure(state="disabled")
        self.currentStateMenu.configure(state="disabled")
        self.optionalityMenu.configure(state="disabled")

    def enable_fields(self):
        self.idText.configure(state="normal")
        self.nameText.configure(state="normal")
        self.preCourseText.configure(state="normal")
        self.semesterText.configure(state="normal")
        self.creditsText.configure(state="normal")
        self.currentStateMenu.configure(state="normal")
        self.optionalityMenu.configure(state="normal")

    def create_course(self):
        data = CoursesByStudent()
        isCreated = ""
        isCreated = data.createCourseByForm(self.id_course.get(), self.name_course.get(), self.pre_course.get(),
                                            self.semester.get(), self.optionality.get(), self.credits.get(), self.current_state.get())
        if len(isCreated) == 0:
            messagebox.showinfo(
                "Agregar curso", "Curso agregado correctamente")
            self.clear_fields()

        else:
            messagebox.showerror("Agregar curso", isCreated)

    def update_course(self):
        data = CoursesByStudent()
        if data.getLengthCoursesData() > 0:
            isUpdated = data.updateCourse(self.id_course.get(), self.name_course.get(), self.pre_course.get(),
                                          self.semester.get(), self.optionality.get(), self.credits.get(), self.current_state.get())
            if len(isUpdated) == 0:
                messagebox.showinfo(
                    "Actualizar curso", "Curso actualizado correctamente")
                self.clear_fields()

            else:
                messagebox.showerror("Actualizar curso", isUpdated)
        else:
            messagebox.showerror("Actualizar curso",
                                 "No hay cursos registrados")
