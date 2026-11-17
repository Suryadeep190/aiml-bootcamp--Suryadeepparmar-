class Student:
    def __init__(self, name:str, roll_no:int) -> None:
        self.name=name
        self.roll_no=roll_no
        self.marks:list[float]=[]
        
    def add_marks(self,score:float)-> None:
        self.marks.append(score)
        
    def average_marks(self) -> float:
        if not self.marks:
            return 0
        return sum(self.marks)/len(self.marks)
    
    def highest_marks(self) -> float:
        if not self.marks:
            return 0
        return max(self.marks)
    
    def lowest_marks(self) -> float:
        if not self.marks:
            return 0
        return min(self.marks)
    
    def __str__(self) -> str:
        return f"Student: {self.name} (Roll #{self.roll_no}) | Avg: {self.average_marks():.2f}"
    
    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, roll_number={self.roll_no!r})"
    
Student1=Student("Suryadeep", 27)
Student2=Student("krinal", 34)
Student3=Student("Aashka", 45)

Student1.add_marks(87)
Student1.add_marks(90)
Student1.add_marks(78)

Student2.add_marks(85)
Student2.add_marks(92)


print(Student1)

classroom = [Student1, Student2, Student3]
print(classroom)

for student in [Student1, Student2, Student3]:
    print(f"{student.name}(Roll No: {student.roll_no}) - Average Marks: {student.average_marks()}")
    