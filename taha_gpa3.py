#Taha Shahid GPA

def report_card():
    
    def avgGPA(listofgpa):
        total = 0
        length = len(listofgpa)
        for gpa in listofgpa:
            total += gpa
        return total/length

    classes = input("How many classes did you take? ")
    classNames = []
    gradeList = []
    gpaList = []
    
    for i in range(classes):
        classNames.append(raw_input("Name of class #" + str(i+1) + "? "))
        grade = input("What was your grade on a scale of 0 to 100? ")
        gradeList.append(grade)
        gpaList.append(gpa(grade))

    print
    print "REPORT CARD"
    for i in range(classes):
        print classNames[i] +  str(gradeList[i]) + str(gpaList[i])
    print "Overall GPA: " + str(avgGPA(gpaList))


report_card()

