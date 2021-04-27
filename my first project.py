import cvs

def write_into_csv():
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(["name","age","email","contact number"])



condition= True


while(condition):
    
    
    student_info=input("enter the student information")
    check=input("enter yes of u want to enter more student information or enter no")\
    info_list=student_info.split('')
write_into_csv(info_list)        
if check==yes:
    condition=True
elif check==no:
     condition=False
    