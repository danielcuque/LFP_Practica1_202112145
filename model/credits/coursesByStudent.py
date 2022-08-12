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
    allowValuesForId = re.compile(r'^[0-9]{3,4}$')
    allowValuesForName = re.compile(
        r'^[0-9A-Za-z À-ÿ\u00f1\u00d1]+$')
    allowValuesForPrecourses = re.compile(r'(\d*;?)*')
    allowValuesForOptionals = re.compile(r'(0|1)')
    allowValuesForSemesterAndCredits = re.compile(r'^[0-9]{1,2}$')
    allowValuesForState = re.compile(r'(-1|0|1)')

    errorReport = ""
    count = 1

    def uploadCourses(self, routeFile):
        if(routeFile == ""):
            self.errorReport = "No se seleccionó ningun archivo"
        else:
            file = open(routeFile, "r", encoding="utf8")
            if (len(self.coursesData) > 0):
                self.coursesData.clear()
            for line in file:
                if(line != ""):
                    verifyCourse = line.split(",")
                    if len(verifyCourse) == 7:
                        # Define a regex to validate just numbers and limite the length of the field to 3-4 characters

                        if verifyCourse[0] is None or not re.fullmatch(self.allowValuesForId, verifyCourse[0].strip()):
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor - " + \
                                verifyCourse[0] + " - no es válido para Id\n"
                        elif verifyCourse[1] is None or not re.fullmatch(self.allowValuesForName, verifyCourse[1].strip()):
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor - " + \
                                verifyCourse[1] + \
                                " - no es válido para Curso\n"
                        elif verifyCourse[2] is None or not re.fullmatch(self.allowValuesForPrecourses, verifyCourse[2].strip()):
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor - " + \
                                verifyCourse[2] + \
                                " - no es válido para Prerrequisitos\n"

                        elif verifyCourse[3] is None or not re.fullmatch(self.allowValuesForOptionals, verifyCourse[3].strip()):
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor " + \
                                verifyCourse[3]+" no es válido para Opción\n"
                        elif verifyCourse[4] is None or not re.fullmatch(self.allowValuesForSemesterAndCredits, verifyCourse[4].strip()):
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor - " + \
                                verifyCourse[4] + \
                                " - no es válido para Semestre\n"
                        elif verifyCourse[5] is None or not re.fullmatch(self.allowValuesForSemesterAndCredits, verifyCourse[5].strip()):
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor - " + \
                                verifyCourse[5] + \
                                " - no es válido para Créditos\n"

                        elif verifyCourse[6] is None or not re.fullmatch(self.allowValuesForState, verifyCourse[6].strip()):
                            print(type(verifyCourse[6]))
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor - " + \
                                verifyCourse[6] + \
                                " - no es válido para Estado\n"
                        else:

                            newCourse = Course(int(verifyCourse[0]), verifyCourse[1], verifyCourse[2],
                                               int(verifyCourse[3]), verifyCourse[4], int(verifyCourse[5]), int(verifyCourse[6]))
                            # Verify if the course exist in the system
                            for course in self.coursesData:
                                if newCourse.idCourse == course.idCourse:
                                    self.coursesData.remove(course)
                            self.coursesData.append(newCourse)
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

    def createCourseByForm(self, idCourse, nameCourse, prerequisites, optional, semester, credits, state):
        newCourse = Course(idCourse, nameCourse, prerequisites,
                           optional, semester, credits, state)
        # Verify if the course exist in the system
        for course in self.coursesData:
            if newCourse.idCourse == course.idCourse:
                self.coursesData.remove(course)
        self.coursesData.append(newCourse)
        return newCourse
