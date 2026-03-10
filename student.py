class Student:
    def __init__(self,student_id,name,age,email,grades=None):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.email=email
        if grades==None:
            self.grades={}
        else:
            self.grades=grades

    def add_grade(self,subject,marks):
        if 0<=marks<=100:
            self.grades[subject]=marks
        else:
            print("you enter invalid marks")
    def get_avg(self):
        if self.grades=={}:
            print(f"the grades of {self.student_id} are not added yet")
            return 0.0
        else:
            avg=sum(self.grades.values())/len(self.grades)
            print(f"the student of ID : {self.student_id} has average of :")
            return avg
    def get_grade_letter(self):
        avg=self.get_avg()
        if avg >=90:
            return "A+"
        elif avg >=85:
            return "A"
        elif avg >=75:
            return "B"
        elif avg >=65:
            return "C"
        elif avg >=50:
            return "D"
        else:
            return "F"
    def display_info(self):
        avg=self.get_avg()
        gradeL=self.get_grade_letter()
        print(f"Student ID :: {self.student_id} Student Name :: {self.name}\nStudent Age :: {self.age} Student Email :: {self.email}\nStudent Average :: {avg:.2f} Student Grade :: {gradeL}")
    def __str__(self):
        return (f"Student ID :: {self.student_id} Student Name :: {self.name}\nStudent Age :: {self.age} Student Email :: {self.email}\nStudent Average :: {self.get_avg():.2f} Student Grade :: {self.get_grade_letter()}")
    def __repr__(self):
        return (f"Student ID :: {self.student_id} Student Name :: {self.name!r}\nStudent Age :: {self.age} Student Email :: {self.email!r}\nStudent Average :: {self.get_avg():.2f} Student Grade :: {self.get_grade_letter()!r}")
    


