import json 
class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
stud = Student("Petr", 19)
def student_to_dict(obj):
    if isinstance(obj, Student):
        return{"name": obj.name, "age": obj.age, "type": "Student"}
    raise TypeError ("Unknown objet type")
json_str = json.dumps(stud, default=student_to_dict)