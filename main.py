import tkinter as tk
import customtkinter as ctk

# Views
from views.credits import CreditsWindow

# # Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")

# # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    # Size of the window
    APP_WIDTH = 500
    APP_HEIGHT = 300

    def __init__(self):
        super().__init__()

        # Set minimum size of window
        self.minsize(self.APP_WIDTH, self.APP_HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # Size of the app
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        # Coordinates of the center of the screen
        x = (screenWidth - self.APP_WIDTH) / 2
        y = (screenHeight - self.APP_HEIGHT) / 2

        # Position of the app
        self.geometry(
            f'{self.APP_WIDTH}x{self.APP_HEIGHT}+{int(x)}+{int(y)}')
        self.title("App FIUSAC")

        # Custom grid layout (2x2)
        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Title of the app
        self.textbox = ctk.CTkLabel(
            master=self, text="Administrador de Pensum FIUSAC",
            text_font=("Roboto Medium", -16), text_color="white")
        self.textbox.grid(row=0, column=0, columnspan=2,
                          padx=20, pady=(20, 0), sticky="nsew")

        # Close the current frame and open the CRUD frame
        self.startButton = ctk.CTkButton(
            master=self, text="Iniciar", command=self.new_window)
        self.startButton.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        # Show credits
        self.creditsButton = ctk.CTkButton(
            master=self, command=self.show_credits, text="Créditos")
        self.creditsButton.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    # Principal functions
    def show_credits(self):
        CreditsWindow(self)

        # # Course label
        # courseLabel = ctk.CTkLabel(
        #     window, text="Lenguajes formales y de programación")
        # courseLabel.pack(side="top", fill="both",
        #                  expand=True, pady=10, padx=10)
        # # Students label
        # studentsLabel = ctk.CTkLabel(
        #     window, text="Desarrollado por Daniel Estuardo Cuque Ruíz",
        #     text_font=("Roboto Medium", -14),
        #     text_color="white")
        # studentsLabel.pack(side="top", fill="both",
        #                    expand=True, pady=10, padx=10)

        # # ID student label
        # idStudentLabel = ctk.CTkLabel(
        #     window, text="Carné: 202112145", text_font=("Roboto Medium", -14),
        # )
        # idStudentLabel.pack(side="top", fill="both",
        #                     expand=True, pady=10, padx=10)

        # # Close button
        # closeButton = ctk.CTkButton(
        #     window, text="Cerrar", command=window.destroy)
        # closeButton.pack(side="top", fill="both",
        #                  expand=True, pady=10, padx=10)

    def new_window(self):
        print("start")


if __name__ == "__main__":
    app = App()
    app.mainloop()