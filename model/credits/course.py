
# Model class for courses
class Course():

    idCourse = ""
    name = ""

    # The ID courses will be separated by a ;
    idCoursesRequired = ""

    # 0 = Optional, 1 = Required
    isRequired = 0

    semester = 0
    credits = 0
    # Aprove = 1, Pending = -1, Studying = 0
    currentState = 0

    def __init__(self, idCourse, name, idCoursesRequired, isRequired, semester, credits, currentState):
        self.idCourse = idCourse
        self.name = name
        self.idCoursesRequired = idCoursesRequired
        self.isRequired = isRequired
        self.semester = semester
        self.credits = credits
        self.currentState = currentState

    def getIdCourse(self):
        return self.idCourse

    def getName(self):
        return self.name

    def getIdCoursesRequired(self):
        return self.idCoursesRequired

    def getIsRequired(self):
        return self.isRequired

    def getSemester(self):
        return self.semester

    def getCredits(self):
        return self.credits

    def getCurrentState(self):
        return self.currentState

    def setIdCourse(self, idCourse):
        self.idCourse = idCourse

    def setName(self, name):
        self.name = name

    def setCurrentState(self, currentState):
        self.currentState = currentState

    def setCredits(self, credits):
        self.credits = credits

    def setSemester(self, semester):
        self.semester = semester

    def setIdCoursesRequired(self, idCoursesRequired):
        self.idCoursesRequired = idCoursesRequired

    def setIsRequired(self, isRequired):
        self.isRequired = isRequired

    def getCourse(self):
        return self.idCourse + "," + self.name + "," + self.idCoursesRequired + "," + self.isRequired + "," + self.semester + "," + self.credits + "," + self.currentState
