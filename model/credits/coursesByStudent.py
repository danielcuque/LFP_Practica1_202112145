from model.credits.course import Course


class CoursesByStudent:

    # The ID courses will be separated by a ;
    coursesData = []

    def __init__(self, routeFile):
        self.routeFile = routeFile

    def uploadCourses(self):
        if(self.routeFile == ""):
            return False
        else:
            file = open(self.routeFile, "r")
            if (len(self.coursesData) > 0):
                self.coursesData.clear()
            for line in file:
                if(line != ""):
                    newCourse = Course(line.split(",")[0], line.split(",")[1], line.split(",")[
                        2], line.split(",")[3], line.split(",")[4], line.split(",")[5], line.split(",")[6])
                    for course in self.coursesData:
                        if newCourse.idCourse == course.idCourse:
                            self.coursesData.remove(course)
                    self.coursesData.append(newCourse)
            file.close()
            return True
