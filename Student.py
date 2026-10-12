from Mixins import SerializationMixin, SearchMixin, LoggingMixin, ValidationMixin, gradeMixin

class Student(SerializationMixin, SearchMixin, LoggingMixin, ValidationMixin, gradeMixin):
    def __init__(self,Student_ID, name, age, 
                 units_done, marks):
        self.Student_ID = Student_ID
        self.name = name
        self.age = age
        self.units_done = units_done  # List to hold units done in course the student is enrolled in
        self.marks = marks  # Dictionary to hold grades for each course taken
    
    def list_courses(self):
        return [unit.course_name for unit in self.units_done]

    def grade_calculations(self):
        Total_marks = sum(self.marks.values())
        Average_marks = Total_marks / len(self.marks)
        letter_grade = self.grade_allocator(Average_marks)
        if letter_grade  == 'A':
            print(f"Excellent performance! , Grade: {letter_grade}")
        elif letter_grade == 'B':
            print(f"Good job! , Grade: {letter_grade}")
        elif letter_grade == 'C':
            print(f"Average performance. , Grade: {letter_grade}")
        elif letter_grade == 'D':
            print(f"Below average performance. , Grade: {letter_grade}")
        elif letter_grade == 'F':
            print(f"Failing performance. , Grade: {letter_grade}")
        else:
            print(f"Invalid grade. , Grade: {letter_grade}")


class Course(SerializationMixin, SearchMixin, LoggingMixin):
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name



student1 = Student(Student_ID=1, name="Ishmael Chesire", age=20, 
                   units_done=["COM410", "COM405E", "COM404E", "BIT413", "COM416", "COM450"], 
                   marks={
                          "COM410": 85,
                          "COM405E": 75,
                          "COM404E": 60,
                          "BIT413": 92,
                          "COM416": 45,
                          "COM450": 25
                   }
                   )
print(student1.to_dict())
print(student1.to_json())
print(student1.grade_calculations())