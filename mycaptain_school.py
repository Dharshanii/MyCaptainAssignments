#Basic School administration tool
import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(['Name','Age','Contact No:','E-mail ID'])
        writer.writerow(info_list)

if __name__=='__main__' :       
    condition= True
    student_num=1
    
    while(condition):
        student_info=input('Enter student info for student number {} in this format-(Name Age Contact_No. E-mail_id): '.format(student_num))
        student_info_list=student_info.split(' ')
              
        print("\nThe entered information is-\nName: {}\nAge: {}\nContact_no: {}\nE-mail: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input('Is the entered information correct?(yes/no )')
        if choice_check=='yes':
            write_into_csv(student_info_list)
            
            condition_check=input('enter (y/n) if you want to enter information for another student: ')
            if condition_check=='y':
                condition=True
                student_num+=1
            elif condition_check=='n':
                condition=False
        elif choice_check=='no':
            print('\nPlease re-enter the values!!')
        