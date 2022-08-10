
# Model class for courses
class Courses():

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

    def __init__(self, idCourse, name, idCourseRequired, isRequired, semester, credits, currentState):
        self.idCourse = idCourse
        self.name = name
        self.idCoursesRequired = idCourseRequired
        self.isRequired = isRequired
        self.semester = semester
        self.credits = credits
        self.currentState = currentState
