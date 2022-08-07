import customtkinter

# # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("dark")

# # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

appWidth = 500
appHeight = 500


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.minsize(appWidth, appHeight)

        # Size of the app
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        # Coordinates of the center of the screen
        x = (screenWidth - appWidth) / 2
        y = (screenHeight - appHeight) / 2

        # Position of the app
        self.geometry(
            f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

        self.title("App FIUSAC")


if __name__ == "__main__":
    app = App()
    app.mainloop()
