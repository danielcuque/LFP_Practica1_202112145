from model.credits.course import Course
import re  # Regular expression


class CoursesByStudent:

    # 0. The Id will be int
    # 1. The name will be string
    # 2. The prerequisites will be a list of strings
    # 3. Optional will be int (0 or 1)
    # 4. The semester will be string
    # 5. The credits will be int
    # 6. The state will be int (-1, 0, 1)

    coursesData = []

    # Keys for the dictionary of the elective courses String
    elegibilityCourseStr = {
        "Obligatorio": "0",
        "Opcional": "1"
    }
    # List of options to state of the course
    stateCourseStr = {
        "Aprobado": "0",
        "Cursando": "1",
        "Pendiente": "-1"
    }

    # List of options to elective of the course int
    # List of options to elegibility of the course
    elegibilityCourse = {
        0: "Obligatorio",
        1: "Opcional"
    }
    # List of options to state of the course
    stateCourse = {
        0: "Aprobado",
        1: "Cursando",
        - 1: "Pendiente"
    }

    # Regex to validate the fields
    allowValuesForId = re.compile(r'^[0-9]{1,4}$')
    allowValuesForName = re.compile(
        r'^[0-9A-Za-z À-ÿ\u00f1\u00d1]+$')
    allowValuesForPrecourses = re.compile(r'(\d*;?)*')
    allowValuesForOptionals = re.compile(r'(0|1)')
    allowValuesForSemesterAndCredits = re.compile(r'^[0-9]{1,2}$')
    allowValuesForState = re.compile(r'(-1|0|1)')

    # Create a error report to show the errors in the file
    errorReport = ""
    count = 1

    def validateFields(self, idCourse, nameCourse, prerequisites, optional, semester, credits, state):
        self.errorReport = ""
        if idCourse is None or not re.fullmatch(self.allowValuesForId, idCourse.strip()):
            self.errorReport += "Error en la línea " + \
                str(self.count) + \
                ": El valor - " + \
                idCourse + " - no es válido para Id\n"
        elif nameCourse is None or not re.fullmatch(self.allowValuesForName, nameCourse.strip()):
            self.errorReport += "Error en la línea " + \
                str(self.count) + \
                ": El valor - " + \
                nameCourse + \
                " - no es válido para Curso\n"
        elif prerequisites is None or not re.fullmatch(self.allowValuesForPrecourses, prerequisites.strip()):
            self.errorReport += "Error en la línea " + \
                str(self.count) + \
                ": El valor - " + \
                prerequisites + " - no es válido para Prerrequisitos\n"
        elif optional is None or not re.fullmatch(self.allowValuesForOptionals, optional.strip()):
            self.errorReport += "Error en la línea " + \
                str(self.count) + \
                ": El valor " + \
                optional+" no es válido para Opción\n"
        elif semester is None or not re.fullmatch(self.allowValuesForSemesterAndCredits, semester.strip()):
            self.errorReport += "Error en la línea " + \
                str(self.count) + \
                ": El valor - " + \
                semester + \
                " - no es válido para Semestre\n"
        elif credits is None or not re.fullmatch(self.allowValuesForSemesterAndCredits, credits.strip()):
            self.errorReport += "Error en la línea " + \
                str(self.count) + \
                ": El valor - " + \
                credits + " - no es válido para Créditos\n"
        elif state is None or not re.fullmatch(self.allowValuesForState, state.strip()):

            self.errorReport += "Error en la línea " + \
                str(self.count) + \
                ": El valor - " + \
                state + \
                " - no es válido para Estado\n"
        if re.fullmatch(self.allowValuesForSemesterAndCredits, semester.strip()):
            if int(semester) > 12 or int(semester) < 1:
                self.errorReport += "Error en la línea " + \
                    str(self.count) + \
                    ": El valor - " + \
                    semester + \
                    " - no es válido para Semestre\n"
        if re.fullmatch(self.allowValuesForSemesterAndCredits, credits.strip()):
            if int(credits) > 10 or int(credits) < 1:
                self.errorReport += "Error en la línea " + \
                    str(self.count) + \
                    ": El valor - " + \
                    credits + \
                    " - no es válido para Créditos\n"

    def uploadCourses(self, routeFile):
        if(routeFile == ""):
            self.errorReport = "No se seleccionó ningun archivo"
        else:
            file = open(routeFile, "r", encoding="utf8")
            for line in file:
                if(line != ""):
                    verifyCourse = line.split(",")
                    if len(verifyCourse) == 7:
                        # Define a regex to validate just numbers and limite the length of the field to 3-4 characters
                        self.validateFields(verifyCourse[0], verifyCourse[1], verifyCourse[2],
                                            verifyCourse[3], verifyCourse[4], verifyCourse[5], verifyCourse[6])
                        if self.errorReport == "":
                            newCourse = Course(int(verifyCourse[0]), verifyCourse[1], verifyCourse[2],
                                               int(verifyCourse[3]), int(verifyCourse[4]), int(verifyCourse[5]), int(verifyCourse[6]))
                            # Verify if the course exist in the system
                            for course in self.coursesData:
                                if newCourse.idCourse == course.idCourse:
                                    self.coursesData.remove(course)
                            self.coursesData.append(newCourse)
                        else:
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": " + \
                                "Campos erróneos\n"
                    else:
                        self.errorReport += "Error en la línea " + \
                            str(self.count) + ": " + \
                            line + " - Error en la cantidad de campos\n"
                else:
                    self.errorReport += "Error en la línea " + \
                        str(self.count) + ": " + " - La línea está vacía\n"

                self.count += 1
            file.close()
            return self.errorReport

    def getCoursesData(self):
        return self.coursesData

    def createCourseByForm(self, idCourse, nameCourse, prerequisites, semester, optional,  credits, state):
        optional = self.elegibilityCourse[optional]
        state = self.stateCourse[state]

        self.validateFields(idCourse, nameCourse, prerequisites,
                            optional, semester, credits, state)
        if self.errorReport == "":
            idCourse = int(idCourse)
            newCourse = Course(idCourse, nameCourse, prerequisites, int(
                optional), semester, int(credits), int(state))
            # Verify if the course exist in the system
            for course in self.coursesData:
                if self.getCourseById(idCourse) is not None:
                    self.coursesData.remove(course)
            self.coursesData.append(newCourse)
            return self.errorReport
        else:
            return self.errorReport

    def getCourseById(self, idCourse):
        for course in self.coursesData:
            if course.idCourse == idCourse:
                return course
        return None

    def getLengthCoursesData(self):
        return len(self.coursesData)

    def updateCourse(self, idCourse, nameCourse, prerequisites, semester, optional,  credits, state):
        elegibilityCourse = {
            "Obligatorio": "0",
            "Opcional": "1"
        }
        # List of options to state of the course
        stateCourse = {
            "Aprobado": "0",
            "Cursando": "1",
            "Pendiente": "-1"
        }

        optional = elegibilityCourse[optional]
        state = stateCourse[state]

        self.validateFields(idCourse, nameCourse, prerequisites,
                            optional, semester, credits, state)
        if self.errorReport == "":
            idCourse = int(idCourse)
            if self.getCourseById(idCourse) is not None:
                for course in self.coursesData:
                    if course.idCourse == idCourse:
                        course.setName(nameCourse)
                        course.setIdCoursesRequired(prerequisites)
                        course.setIsRequired(int(optional))
                        course.setSemester(int(semester))
                        course.setCredits(int(credits))
                        course.setCurrentState(int(state))

                        return self.errorReport
            else:
                self.errorReport += "Error en la línea " + \
                    str(self.count) + ": " + \
                    " - El curso no existe\n"
                return self.errorReport
        else:
            return self.errorReport

    def deleteCourse(self, idCourse):
        for course in self.coursesData:
            if course.idCourse == int(idCourse):
                self.coursesData.remove(course)
                return True
        return False
