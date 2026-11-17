class person:
    def __init__(self,name:str) -> None:
        self.name=name
        
    def greet(self)->str:
        return f"Hello, my name is {self.name}."
    
class student(person):
    
    def __init__(self,name:str,roll_no:int) ->None:
        super().__init__(name)
        self.roll_no=roll_no
        self.marks:list[float]=[]
        
    def add_marks(self,score:float)-> None:
        self.marks.append(score)
        
    def averafe_marks(self) -> float:
        if not self.marks:
            return 0
        return sum(self.marks)/len(self.marks)
    
    def greet(self) -> str:
        return f"hello < my name is {self.name} and my roll_no is {self.roll_no}."
    
class teacher(person):
    def __init__(self,name:str,subject:str) ->None:
        super().__init__(name)
        self.subject=subject
        
student1=student("Suryadeep",27)
teacher1=teacher("krinal","Mbbs")

print(student1.greet())
print(teacher1.greet())
print(f"Teacher:{teacher1.name} teaches {teacher1.subject}")


"""
In this task code the student and teacher role might chang with time for that reason Composition may suit better here
and even if we change something in parent class it affect subclasses as it relies on parent class 
"""
