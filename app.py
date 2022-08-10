import customtkinter as ctk

# Views
from views.author import CreditsWindow
from views.home.mainMenu import MainMenu

# Helpers
from model.helpers.positionWindow import PositionWindow

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

        # Position of the app
        self.geometry(PositionWindow().positionWindow(self.winfo_screenwidth(
        ), self.winfo_screenheight(), self.APP_WIDTH, self.APP_HEIGHT))

        self.title("App FIUSAC")

        # Custom grid layout (2x2)
        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Title of the app
        self.textbox = ctk.CTkLabel(
            master=self, text="Administrador de Pensum FIUSAC",
            text_font=("Roboto Medium", -25), text_color="white")
        self.textbox.grid(row=0, column=0, columnspan=2,
                          padx=20, pady=(20, 0), sticky="nsew")

        # Close the current frame and open the CRUD frame
        self.startButton = ctk.CTkButton(
            master=self, text="Iniciar", command=self.main_menu)
        self.startButton.grid(row=1, column=0,
                              padx=20, pady=20, sticky="ew")

        # Show credits
        self.creditsButton = ctk.CTkButton(
            master=self, command=self.show_credits, text="Créditos")
        self.creditsButton.grid(row=1, column=1,
                                padx=20, pady=20, sticky="ew")

    # Principal functions
    def show_credits(self):
        CreditsWindow(self)

    def main_menu(self):
        self.destroy()
        app = MainMenu(self)
        app.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()
