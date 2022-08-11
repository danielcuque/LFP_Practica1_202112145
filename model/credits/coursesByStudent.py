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

    allowValorsForOptionals = ["1", "0"]
    allowValorsForState = ["-1", "0", "1"]

    errorReport = ""
    count = 1

    def uploadCourses(self, routeFile):
        if(routeFile == ""):
            self.errorReport = "No se selecciono ningun archivo"
        else:
            file = open(routeFile, "r")
            if (len(self.coursesData) > 0):
                self.coursesData.clear()
            for line in file:
                if(line != ""):
                    verifyCourse = line.split(",")
                    if len(verifyCourse) == 7:
                        # Define a regex to validate just numbers and limite the length of the field to 3-4 characters
                        if verifyCourse[0] is None or not re.search(r"^[0-9]{3,4}$", verifyCourse[0].strip()):
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor - " + \
                                verifyCourse[0] + " - no es válido para Id\n"
                        elif verifyCourse[1] is None or not re.search(r"^[a-zA-Z À-ÿ\u00f1\u00d1]{1,50}$", verifyCourse[1].strip()):
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor - " + \
                                verifyCourse[1] + \
                                " - no es válido para Curso\n"

                        elif verifyCourse[3] is None or verifyCourse[3] not in self.allowValorsForOptionals:
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor" + \
                                verifyCourse[3]+"no es válido para Opción\n"
                        elif verifyCourse[6] is None or verifyCourse[6].strip() not in self.allowValorsForState:
                            print(type(verifyCourse[6]))
                            self.errorReport += "Error en la línea " + \
                                str(self.count) + \
                                ": El valor - " + \
                                verifyCourse[6] + \
                                " - no es válido para Estado\n"

                        else:

                            newCourse = Course(int(verifyCourse[0]), verifyCourse[1], verifyCourse[2],
                                               verifyCourse[3], verifyCourse[4], verifyCourse[5], verifyCourse[6])
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
                        str(self.count) + ": " + \
                        line + " - La línea está vacía\n"

                self.count += 1
            file.close()
            return self.errorReport
