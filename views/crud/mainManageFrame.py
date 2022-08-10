import customtkinter as ctk
from tkinter import LEFT

# Helpers
from model.helpers.positionWindow import PositionWindow

# Frames
from views.crud.listCourse import ListCourse
from views.crud.createCourse import CreateCourse
from views.crud.updateCourse import UpdateCourse
from views.crud.deleteCourse import DeleteCourse


class mainManageFrame(ctk.CTk):

    # Size of the window
    APP_WIDTH = 780
    APP_HEIGHT = 520

    def __init__(self, *args, **kwargs):
        super().__init__()

        # Set principal properties of the window
        self.title("Gestionar cursos")
        self.minsize(self.APP_WIDTH, self.APP_HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # Position of the app
        self.geometry(
            PositionWindow().positionWindow(self.winfo_screenwidth(
            ), self.winfo_screenheight(), self.APP_WIDTH, self.APP_HEIGHT))

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = ctk.CTkFrame(master=self,
                                       width=180,
                                       corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = ListCourse(self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(6, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.titleLabel = ctk.CTkLabel(master=self.frame_left,
                                       text="Acciones",
                                       text_font=("Roboto", "14", "bold"))
        self.titleLabel.grid(row=1, column=0, pady=10, padx=10)

        # List courses button
        self.listCourseButton = ctk.CTkButton(master=self.frame_left,
                                              text="Listar cursos",
                                              command=lambda: self.changeFrame(ListCourse(self)))
        self.listCourseButton.grid(row=2, column=0, pady=10, padx=20)

        # Create course button
        self.createCourseButton = ctk.CTkButton(master=self.frame_left,
                                                text="Crear curso",
                                                command=lambda: self.changeFrame(CreateCourse(self)))
        self.createCourseButton.grid(row=3, column=0, pady=10, padx=20)

        # Update course button
        self.updateCourseButton = ctk.CTkButton(master=self.frame_left,
                                                text="Actualizar curso",
                                                command=lambda: self.changeFrame(UpdateCourse(self)))
        self.updateCourseButton.grid(row=4, column=0, pady=10, padx=20)

        # Delete course button
        self.deleteCourseButton = ctk.CTkButton(master=self.frame_left,
                                                text="Eliminar curso",
                                                command=lambda: self.changeFrame(DeleteCourse(self)))
        self.deleteCourseButton.grid(row=5, column=0, pady=10, padx=20)

        # Apparence mode button
        self.appearanceLabel = ctk.CTkLabel(
            master=self.frame_left, text="Mode de apariencia:")
        self.appearanceLabel.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = ctk.CTkOptionMenu(master=self.frame_left,
                                              values=[
                                                  "Oscuro", "Claro", "Sistema"],
                                              command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # Setting components
        self.optionmenu_1.set("Oscuro")

    def change_appearance_mode(self, new_appearance_mode):
        if new_appearance_mode == "Oscuro":
            ctk.set_appearance_mode("dark")
        elif new_appearance_mode == "Claro":
            ctk.set_appearance_mode("light")
        elif new_appearance_mode == "Sistema":
            ctk.set_appearance_mode("System")

    def changeFrame(self, frame):
        self.frame_right.destroy()
        self.frame_right = frame
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
