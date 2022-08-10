import customtkinter as ctk
import tkinter as tk


class CreditsWindow(ctk.CTkToplevel):
    WINDOW_WIDTH = 370
    WINDOW_HEIGHT = 200

    def __init__(self, master):
        super().__init__(master)
        self.title("Créditos")
        self.minsize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.geometry(
            f'{self.WINDOW_WIDTH-100}x{self.WINDOW_HEIGHT-100}+{int(self.WINDOW_WIDTH/2)}+{int(self.WINDOW_HEIGHT/2)}')
        # Course label
        courseLabel = ctk.CTkLabel(
            self, text="Lenguajes formales y de programación")
        courseLabel.pack(side="top", fill="both",
                         expand=True, pady=10, padx=10)
        # Students label
        studentsLabel = ctk.CTkLabel(
            self, text="Desarrollado por Daniel Estuardo Cuque Ruíz",
            text_font=("Roboto Medium", -14),
            text_color="white")
        studentsLabel.pack(side="top", fill="both",
                           expand=True, pady=10, padx=10)

        # ID student label
        idStudentLabel = ctk.CTkLabel(
            self, text="Carné: 202112145", text_font=("Roboto Medium", -14),
        )
        idStudentLabel.pack(side="top", fill="both",
                            expand=True, pady=10, padx=10)

        # Close button
        closeButton = ctk.CTkButton(
            self, text="Cerrar", command=self.destroy)
        closeButton.pack(side="top", fill="both",
                         expand=True, pady=10, padx=10)
