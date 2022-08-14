import customtkinter as ctk
from tkinter import *
from tkinter import messagebox, ttk
# Helpers
from model.helpers.positionWindow import PositionWindow
from model.credits.coursesByStudent import CoursesByStudent


class CountCredits(ctk.CTk):
    # Size of the window
    APP_WIDTH = 750
    APP_HEIGHT = 520

    def __init__(self, *args, **kwargs):
        super().__init__()

        # Set principal properties of the window
        self.title("Conteo de créditos")
        self.minsize(self.APP_WIDTH, self.APP_HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # Position of the app
        self.geometry(
            PositionWindow().positionWindow(self.winfo_screenwidth(
            ), self.winfo_screenheight(), self.APP_WIDTH, self.APP_HEIGHT))
        # Create a custom grid layot (2x1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Create a frame to put the widgets
        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.grid(
            column=0, row=1, sticky="nswe", padx=15, pady=15)
        # Create a grid layout (8x3)
        self.frame_info.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame_info.grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        # Create a obj to get the data
        self.coursesByStudent = CoursesByStudent()

        # Create a label to show the title of the app
        self.titleLabel = ctk.CTkLabel(master=self,
                                       text="Conteo de créditos",
                                       height=50,
                                       corner_radius=6,
                                       text_font=("Roboto Medium", -25), text_color="white",
                                       fg_color=("white", "gray38"),
                                       justify=CENTER)

        self.titleLabel.grid(column=0, row=0, columnspan=2,
                             sticky="nwe", padx=15, pady=15)

        '''Create button to go back'''
        self.backButton = ctk.CTkButton(master=self.frame_info,
                                        text="Volver",
                                        height=30,
                                        corner_radius=6,
                                        text_font=("Roboto Medium", -20), text_color="white",
                                        command=self.back)
        self.backButton.grid(
            column=1, row=7, sticky="nwe", padx=15, pady=15)

        if self.coursesByStudent.getLengthCoursesData() == 0:
            self.labelInformation = ctk.CTkLabel(master=self.frame_info, text="No hay cursos registrados", width=10, height=1, corner_radius=6,
                                                 text_font=("Roboto Medium", -15), text_color="white",
                                                 justify=LEFT)
            self.labelInformation.grid(
                column=1, row=4, sticky="nwe")
        else:

            self.create_componets()

    def create_componets(self):
        # Get the data
        self.creditsApprovalInfo = self.coursesByStudent.countApprovedCredits()
        self.creditsPendingInfo = self.coursesByStudent.countPendingCredits()
        self.creditsStudyingInfo = self.coursesByStudent.countCurrentCredits()
        '''Create the labels of the first column to show the data'''
        self.approvalLabel = ctk.CTkLabel(master=self.frame_info,
                                          text="Créditos aprobados",
                                          height=30,
                                          corner_radius=6,
                                          text_font=("Roboto Medium", -20), text_color="white",
                                          justify=LEFT)
        self.approvalLabel.grid(
            column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.studyingLabel = ctk.CTkLabel(master=self.frame_info,
                                          text="Créditos cursando",
                                          height=30,
                                          corner_radius=6,
                                          text_font=("Roboto Medium", -20), text_color="white",
                                          justify=LEFT)
        self.studyingLabel.grid(
            column=0, row=1, sticky="nwe", padx=15, pady=15)

        self.pendingLabel = ctk.CTkLabel(master=self.frame_info,
                                         text="Créditos pendientes",
                                         height=30,
                                         corner_radius=6,
                                         text_font=("Roboto Medium", -20), text_color="white",
                                         justify=LEFT)
        self.pendingLabel.grid(
            column=0, row=2, sticky="nwe", padx=15, pady=15)

        self.obligatoryCreditsLabel = ctk.CTkLabel(master=self.frame_info,
                                                   text="Créditos obligatorios hasta el semestre: ",
                                                   height=30,
                                                   corner_radius=6,
                                                   text_font=("Roboto Medium", -20), text_color="white",
                                                   justify=LEFT)
        self.obligatoryCreditsLabel.grid(
            column=0, row=3, sticky="nwe", padx=15, pady=15)

        self.selectSemesterLabel1 = ctk.CTkLabel(master=self.frame_info,
                                                 text="Semestre",
                                                 height=30,
                                                 corner_radius=6,
                                                 text_font=("Roboto Medium", -20), text_color="white",
                                                 justify=LEFT)
        self.selectSemesterLabel1.grid(
            column=0, row=4, sticky="nwe", padx=15, pady=15)

        self.creditsOfCurrentSemesterLabel = ctk.CTkLabel(master=self.frame_info,
                                                          text="Créditos del semestre: ",
                                                          height=30,
                                                          corner_radius=6,
                                                          text_font=("Roboto Medium", -20), text_color="white",
                                                          justify=LEFT)
        self.creditsOfCurrentSemesterLabel.grid(
            column=0, row=5, sticky="nwe", padx=15, pady=15)

        self.selectSemesterLabel2 = ctk.CTkLabel(master=self.frame_info,
                                                 text="Semestre",
                                                 height=30,
                                                 corner_radius=6,
                                                 text_font=("Roboto Medium", -20), text_color="white",
                                                 justify=LEFT)
        self.selectSemesterLabel2.grid(
            column=0, row=4, sticky="nwe", padx=15, pady=15)

        '''Create the labels of the second column to show the data'''
        self.approvalDataLabel = ctk.CTkLabel(master=self.frame_info,
                                              text=self.creditsApprovalInfo,
                                              height=30,
                                              corner_radius=6,
                                              text_font=("Roboto Medium", -20), text_color="white",
                                              justify=LEFT)
        self.approvalDataLabel.grid(
            column=1, row=0, sticky="nwe", padx=15, pady=15)

        self.studyingDataLabel = ctk.CTkLabel(master=self.frame_info,
                                              text=self.creditsStudyingInfo,
                                              height=30,
                                              corner_radius=6,
                                              text_font=("Roboto Medium", -20), text_color="white",
                                              justify=LEFT)
        self.studyingDataLabel.grid(
            column=1, row=1, sticky="nwe", padx=15, pady=15)

        self.pendingDataLabel = ctk.CTkLabel(master=self.frame_info,
                                             text=self.creditsPendingInfo,
                                             height=30,
                                             corner_radius=6,
                                             text_font=("Roboto Medium", -20), text_color="white",
                                             justify=LEFT)
        self.pendingDataLabel.grid(
            column=1, row=2, sticky="nwe", padx=15, pady=15)

        self.obligatoryCreditsDataLabel = ctk.CTkLabel(master=self.frame_info,
                                                       text="0",
                                                       height=30,
                                                       corner_radius=6,
                                                       text_font=("Roboto Medium", -20), text_color="white",
                                                       justify=LEFT)
        self.obligatoryCreditsDataLabel.grid(
            column=1, row=3, sticky="nwe", padx=15, pady=15)

        self.pickSemesterToObligatoryCredits = ttk.Spinbox(
            master=self.frame_info,
            from_=1, to=12, increment=1, state="readonly")
        self.pickSemesterToObligatoryCredits.grid(
            column=1, row=4, sticky="nwe", padx=15, pady=15)

        self.currentCreditsLabel = ctk.CTkLabel(master=self.frame_info,
                                                text="0",
                                                height=30,
                                                corner_radius=6,
                                                text_font=("Roboto Medium", -20), text_color="white",
                                                justify=LEFT)
        self.currentCreditsLabel.grid(
            column=1, row=5, sticky="nwe", padx=15, pady=15)

        self.pickCurrentSemester = ttk.Spinbox(master=self.frame_info,
                                               from_=10, to=30, increment=1, state="readonly")
        self.pickCurrentSemester.grid(
            column=1, row=6, sticky="nwe", padx=15, pady=15)

        '''Create a button to count credits depending of the function'''
        self.obligatoryCreditsButton = ctk.CTkButton(master=self.frame_info,
                                                     text="Contar",
                                                     height=30,
                                                     corner_radius=6,
                                                     text_font=("Roboto Medium", -20), text_color="white",
                                                     command=self.getDataAtCurrentSemester)
        self.obligatoryCreditsButton.grid(
            column=2, row=4, sticky="nwe", padx=15, pady=15)

        self.currentCreditsButton = ctk.CTkButton(master=self.frame_info,
                                                  text="Contar",
                                                  height=30,
                                                  corner_radius=6,
                                                  text_font=("Roboto Medium", -20), text_color="white",
                                                  command=self.getDataAtCurrentSemester)
        self.currentCreditsButton.grid(
            column=2, row=6, sticky="nwe", padx=15, pady=15)

    def getDataAtCurrentSemester(self):
        creditsAtSemester = CoursesByStudent().countCreditsAtCurrentSemester(
            int(self.pickSemesterToObligatoryCredits.get()))

        self.obligatoryCreditsDataLabel.configure(text=creditsAtSemester)

    def getDataBySemester(self):
        creditsBySemester = CoursesByStudent().countCreditsBySemester(
            int(self.pickCurrentSemester.get()))

        self.currentCreditsLabel.configure(text=creditsBySemester)

    def back(self):
        self.destroy()
        from views.home.mainMenu import MainMenu
        MainMenu()
