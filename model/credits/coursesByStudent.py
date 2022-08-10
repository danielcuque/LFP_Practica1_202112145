from model.credits.courses import Courses


from model.credits.courses import Courses


class CoursesByStudent:

    # The ID courses will be separated by a ;
    coursesData = []

    def __init__(self, routeFile):
        self.routeFile = routeFile

    def uploadCourses(self):
        if(self.routeFile == ""):
            return False
        else:
            f = open(self.routeFile, "r")
            for line in f:
                newCourse = Courses(line.split(",")[0], line.split(",")[1], line.split(",")[
                                    2], line.split(",")[3], line.split(",")[4], line.split(",")[5], line.split(",")[6])
                self.coursesData.append(newCourse)
            f.close()
            return True
