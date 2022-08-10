
# Model class for courses
class Course():

    idCourse = ""
    name = ""

    # The ID courses will be separated by a ;
    idCoursesRequired = ""

    # 0 = Optional, 1 = Required
    isRequired = 0

    semester = ""
    credits = ""
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

    def getCourse(self):
        return self.idCourse + "," + self.name + "," + self.idCoursesRequired + "," + self.isRequired + "," + self.semester + "," + self.credits + "," + self.currentState
