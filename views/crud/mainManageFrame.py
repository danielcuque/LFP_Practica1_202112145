import tkinter as tk
import customtkinter as ctk

# Helpers
from model.helpers.positionWindow import PositionWindow

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

        # Custom grid layout (2x1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.frame_left = ctk.CTkFrame(
            master=self, bg="white", width=180, corner_radius=10)
        self.frame_left.grid(row=0, column=0, sticky="nsew")

        self.frame_right = ctk.CTkFrame(
            master=self)
        self.frame_right.grid(row=0, column=1, sticky="nsew", pady=15, padx=15)

        # ======= frame_left =======

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, minsize=10)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        # Side frame components
        self.titleLabel = ctk.CTkLabel(
            master=self.frame_left, text="Acciones", text_font=("Roboto", "14", "bold"))
        self.titleLabel.grid(row=0, column=0, sticky="nsew")
