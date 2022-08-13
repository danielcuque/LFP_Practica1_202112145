import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
import re

from model.credits.coursesByStudent import CoursesByStudent


class DeleteCourse(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()

        self.master = master

        #  configure grid layout (2x1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.titleLabel = ctk.CTkLabel(master=self,
                                       text="Eliminar curso",
                                       height=50,
                                       corner_radius=6,
                                       text_font=("Roboto Medium", -25), text_color="white",
                                       fg_color=("white", "gray38"),
                                       justify=LEFT)
        self.titleLabel.grid(
            column=0, row=0, columnspan=2, sticky="nwe", padx=15, pady=15)

        # Create a frame to store the fields
        self.frame_info = ctk.CTkFrame(master=self)
        self.frame_info.grid(column=0, row=1, sticky="nswe", padx=15, pady=15)

        '''Configure the grid layout'''
        # Create a grid of (7x3) to store the fields
        self.frame_info.grid_columnconfigure((0, 1), weight=1)
        self.frame_info.grid_columnconfigure(2, weight=0)
        self.frame_info.grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        lenghtOfData = CoursesByStudent().getLengthCoursesData()
        if lenghtOfData == 0:
            self.labelInformation = ctk.CTkLabel(master=self, text="No hay cursos registrados", width=10, height=1, corner_radius=6,
                                                 text_font=("Roboto Medium", -15), text_color="white",
                                                 fg_color=("white", "gray38"),
                                                 justify=LEFT)
            self.labelInformation.grid(
                column=0, row=1, columnspan=2, sticky="nswe", padx=15, pady=5)
        else:
            self.create_components()

    def create_components(self):

        self.courseIdLabel = ctk.CTkLabel(master=self.frame_info,
                                          text="ID del curso:",
                                          text_font=("Roboto", -15), text_color="white",
                                          justify=LEFT)
        self.courseIdLabel.grid(
            column=0, row=1, sticky="nwe", padx=15, pady=15)

        self.courseIdEntry = ctk.CTkEntry(master=self.frame_info,
                                          text_font=("Roboto", -15), text_color="white",
                                          justify=LEFT)
        self.courseIdEntry.grid(
            column=1, row=1, sticky="nwe", padx=15, pady=15)

        self.delete_button = ctk.CTkButton(master=self.frame_info,
                                           text="Eliminar",
                                           command=self.delete_course,
                                           text_font=("Roboto", -15), text_color="white")
        self.delete_button.grid(
            column=0, row=2, sticky="nwe", columnspan=3, padx=55, pady=15)

    def delete_course(self):
        data = CoursesByStudent()
        id_course = self.courseIdEntry.get()
        if id_course is None or not re.fullmatch(data.allowValuesForId, id_course.strip()):
            messagebox.showerror("Error", "El valor de ID no es válido")
        else:
            resp = data.deleteCourse(id_course)
            if resp:
                messagebox.showinfo("Éxito", "El curso ha sido eliminado")
                self.courseIdEntry.delete(0, END)
            else:
                messagebox.showerror(
                    "Error", "El curso no ha sido eliminado. Intente con otro código")
