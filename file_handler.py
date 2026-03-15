import json
import os
from student import Student
class FileHandler:
    def __init__ (self,filename="students.json"):
        self.filename=filename
    def save_data(self,students):
        student_data=[]
        for s in students:
            S_dict={
                "student_id":s.student_id,
                "name":s.name,
                "age": s.age,
                "email": s.email,
                "grades": s.grades
            }
            student_data.append(S_dict)
        try:
            with open(self.filename,"w") as f:
                json.dump(student_data,f,indent=2)
                print(f" Successfully saved {len(students)} students to {self.filename}")
        except Exception as e:
            print(f" Error during saving: {e}")
    def load_data(self):
        if not os.path.exists(self.filename):
            print(" No file found.Starting with an empty list.")
            return []
        try:
            with open(self.filename,"r")as f:
                data=json.load(f)
            reconstructed_students = []
            for item in data:
                new_student = Student(
                    item['student_id'], 
                    item['name'], 
                    item['age'], 
                    item['email']
                )
                new_student.grades = item['grades']
                reconstructed_students.append(new_student)
            return reconstructed_students
        except Exception as e:
            print(f" Error during loading: {e}")
            return []