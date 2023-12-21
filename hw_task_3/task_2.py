class Human:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender


class Student(Human):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.knowledge = []

    def __len__(self):
        return len(self.knowledge)

    def forget(self, study):
        self.knowledge.remove(study)

    def take(self, study):
        self.knowledge.append(study)


class Teacher(Human):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.student_count = 0

    def teach(self, study, students):
        for student in students:
            student.take(study)
            self.student_count += 1


class StudyMat:
    def __init__(self, *args):
        self.materials = list(args)

    def __len__(self):
        return len(self.materials)


materials = StudyMat('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')
teacher = Teacher('Александр', 'Петрович', 51, 'Муж')
St1 = Student('Павел', 'Павлов', 13, 'Муж')
St2 = Student('Алексей', 'Иванов', 12, 'Муж')
St3 = Student('Кристина', 'Ивановна', 11, 'Жен')
St4 = Student('Петр', 'Максимов', 17, 'Муж')
teacher.teach(materials.materials[0], [St1, St3, St4])
teacher.teach(materials.materials[1], [St1, St2])
teacher.teach(materials.materials[2], [St1, St2, St3, St4])
teacher.teach(materials.materials[3], [St2, St3])
teacher.teach(materials.materials[4], [St1, St4])
print(St1.knowledge)
print(St2.knowledge)
print(St3.knowledge)
print(St4.knowledge)
print(len(materials))
print(len(St3))
St3.forget('Python')
print(len(St3))
