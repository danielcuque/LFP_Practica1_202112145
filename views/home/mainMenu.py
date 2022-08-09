import customtkinter as ctk
from tkinter import filedialog


class mainMenu(ctk.CTk):

    # Sieze of the window
    APP_WIDTH = 400
    APP_HEIGHT = 400

    INITIAL_ROUTE = "/"

    # Padding
    PADY = (5, 0)
    PADX = 20

    def __init__(self, *args, **kwargs):
        super().__init__()

        # Size of the app
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        # Coordinates of the center of the screen
        x = (screenWidth - self.APP_WIDTH) / 2
        y = (screenHeight - self.APP_HEIGHT) / 2

        # Position of the app
        self.geometry(
            f'{self.APP_WIDTH}x{self.APP_HEIGHT}+{int(x)}+{int(y)}')
        self.title("Menú principal")

        # Create a secondary frame
        self.secondaryFrame = ctk.CTkFrame(self)
        self.secondaryFrame.pack(fill="both", expand=True, pady=20, padx=20, )

        # Create a grid system (2x4) for the secondary frame
        self.secondaryFrame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.secondaryFrame.grid_columnconfigure(0, weight=1)

        # Create the components of the secondary frame

        '''
        Buttons
        1. Upload file
        2. Manage courses
        3. Count credits
        4. Exit
        '''
        # Upload file button
        self.uploadFileButton = ctk.CTkButton(
            master=self.secondaryFrame, text="Subir archivo", command=self.uploadFile)
        self.uploadFileButton.grid(
            row=0, column=0,  padx=self.PADX, pady=self.PADY, sticky="ew")

        # Manage courses button
        self.manageCoursesButton = ctk.CTkButton(
            master=self.secondaryFrame, text="Gestionar cursos", command=self.manageCourses)
        self.manageCoursesButton.grid(
            row=1, column=0,  padx=self.PADX, pady=self.PADY, sticky="ew")

        # Count credits button
        self.countCreditsButton = ctk.CTkButton(
            master=self.secondaryFrame, text="Contar créditos", command=self.countCredits)
        self.countCreditsButton.grid(
            row=2, column=0,  padx=self.PADX, pady=self.PADY, sticky="ew")

        # Exit button
        self.exitButton = ctk.CTkButton(
            master=self.secondaryFrame, text="Salir", command=self.exit)
        self.exitButton.grid(
            row=3, column=0,  padx=self.PADX, pady=self.PADY, sticky="ew")

    def uploadFile(self):
        fileName = filedialog.askopenfilename(
            initialdir="/", title="Seleccionar archivo",
            filetypes=(("Archivos de texto", "*.lfp"), ("Todos los archivos", "*.*")))

    def manageCourses(self):
        pass

    def countCredits(self):
        pass

    def exit(self):
        self.destroy()
