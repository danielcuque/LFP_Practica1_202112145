from typing_extensions import Self
import customtkinter as ctk

# Helpers
from docs.helpers.positionWindow import PositionWindow


class CountCredits(ctk.CTkFrame):
    def __init__(self):
        super().__init__()

    # Set position of the window

        self.geometry(
            PositionWindow().positionWindow(self.winfo_screenwidth(), self.winfo_screenheight(), self.APP_WIDTH, self.APP_HEIGHT))

        self.title("Conteo de créditos")
