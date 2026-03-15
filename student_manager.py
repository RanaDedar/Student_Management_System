from student import Student
from file_handler import FileHandler
class Student_manager:
    def __init__ (self):
        self.handler = FileHandler()
        self.students = self.handler.load_data()
    def _autosave(self):
        self.handler.save_data(self.students)
    def add_student(self,student_id,name,age,email):
        if any(s.student_id==student_id  for s in self.students):
            print("the student already exist with",student_id)
            return
        new_student=Student(student_id,name,age,email,grades=None)
        self.students.append(new_student)
        print(f"The student named :: {name} has been added")
    def search_student(self,querry):
        querry=str(querry).lower()
        result=[]
        for s in self.students:
            if querry == str(s.student_id).lower() or querry == str(s.name).lower():
                result.append(s)
        if result:
            print(f"{len(result)} Students have been found")
            for student in result:
                student.display_info()
        else:
            print(f"there is no student matching {querry}")
        return result
    def remove_student(self,student_id):
        for s in self.students:
            if s.student_id ==student_id:
                self.students.remove(s)
                print(f"student with {student_id} is removed")
                return True
            print(f"no student with {student_id} found")
            return False
    def update_student(self,student_id,**kwargs):
        required_student=None
        for s in self.students:
            if s.student_id==student_id:
                required_student=s
                break
        if not required_student:
            print(f"The student with {student_id} does not exist")
            return False
        for key,values in kwargs.items():
            if hasattr(required_student,key):
                setattr(required_student,key,values)
                print(f"Updated {key} for {values}")
            else:
                print(f"the attribute doesn't exist for the student {student_id}")
        print(f"the Student {student_id} has been updated successfully")
        return True
    def list_all_students(self):
        if not self.students:
            print("there are no student")
            return
        for s in self.students:
            s.display_info()
    def get_stats(self):
        if not self.students:
            print("there are no students yet")
            return False
        avg=[s.get_avg() for s in self.students]
        stats={
            "total_students" : len(self.students),
            "Class_Average" :sum(avg)/len(avg),
            "Highest_Score" :max(avg),
            "Lowest_Score" :min(avg),
            "pass_rate" :(len([a for a in avg if a>=50])/len(avg))*100
        }
        for key,value in stats.items():
            unit="%" if "Average" in key or "rate" in key else ""
            print(f"{key} : {value:2f}{unit}")
        return stats

    def get_top_students(self,TS):
        if not self.students:
            print("There are no students yet")
            return []
        sorted_students=sorted(self.students,key=lambda s: s.get_avg(),reverse=True)
        top_s=sorted_students[:TS]
        print(f"Top {len(top_s)} Students")
        for s in top_s:
            print(f"{s.name} :: {s.get_avg():.2f}")
        return top_s   
        
            
        

    
            