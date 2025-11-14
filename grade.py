class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print(self.name,"Got A grade")
        elif self.marks>=80:
            print(self.name,"Got B grade")
        else:
            print(self.name,"Got C grade")
s1=student("Anu",92)
s2=student("Rahul",80)
s3=student("Meera",60)
s1.grade()
s2.grade()
s3.grade()
