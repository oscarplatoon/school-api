from builtins import object


class StudentSerializer(object):
    def __init__(self, data) -> None:
        self.data = data

    @property
    def all_students(self):
        output = {'students':[], 'courses':[]}

        for student in self.data:
            student_detail={
                'student_name':student.student_name,
                'courses': []
            }
            for course in student.courses.all():
                course_detail={
                    'title':course.title,
                    'credits': course.credits
                }
                student_detail['courses'].append(course_detail)
            output['students'].append(student_detail)
            print(output)
        return output

    @property
    def student_detail(self):
        output = {
            'student_name':self.data.student_name,
            'courses': []
        }
        print(self.data.courses)
        for course in self.data.courses.all():
            course_detail={
                'title':course.title
            }
            output['courses'].append(course_detail)
        return output


class CourseSerializer(object):
    def __init__(self, data) -> None:
        self.data = data

    @property
    def all_courses(self):
        output = {'courses':[]}

        for course in self.data:
            course_detail={
                'title':course.title,
                'credits': course.credits,
                'students': []
            }
            for student in course.students.all():
                student_detail= {
                    "student_name": student.student_name
                }
                course_detail['students'].append(student_detail)
            output['courses'].append(course_detail)
        return output

    @property
    def course_detail(self):
        output = {
            'title':self.data.title,
            'credits': self.data.credits,
            'students': []
        }
        for student in self.data.students.all():
            student_detail = {
                'student_name':student.student_name
            }
            output['students'].append(student_detail)
        print(output)
        return output