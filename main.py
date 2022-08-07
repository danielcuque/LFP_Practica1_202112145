import tkinter as tk
import customtkinter as ctk

# # Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")

# # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    APP_WIDTH = 500
    APP_HEIGHT = 500

    def __init__(self):
        super().__init__()

        # Set minimum size of window
        self.minsize(self.APP_WIDTH, self.APP_HEIGHT)

        # Custom grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = ctk.CTkFrame(master=self,
                                       width=180,
                                       corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = ctk.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

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
        self.label = ctk.CTkLabel(self, text="Reporte de Pensum FIUSAC")


if __name__ == "__main__":
    app = App()
    app.mainloop()
