class Student:
    def __init__(self, name=None):
        self.name = name
    def __del__(self):
        print("Training is over.I am now an expert!")

nick = Student()