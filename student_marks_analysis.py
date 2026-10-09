'''
Question 1: Student Marks Analysis 
A college stores students' marks in a list. Write a function that 
accepts a list of marks and displays the highest mark, lowest 
mark, average mark, and number of students who passed (marks 
of 40 or above). 
'''
marks=[30,39,45,40,60,70,50,80,90,55]
def student_info(marks: list):
    c= 0
    for i in marks:
        if i>40:
            c+=1
    return max(marks), min(marks), sum(marks)/len(marks),c
print('maximum marks={}, minimum marks={},average={},students passed={}'.format(*student_info(marks)))
    