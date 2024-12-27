import random
import sqlite3
from colorama import init, Fore
from connection import create_connection
from data import get_subjects
from db import add_data, create_tables
from pathlib import Path

def get_db_results(query_num):
    QUERY_STR = 'query_'
    QUERY_FILE_EXTENSION = '.sql'

    db_connection = create_connection()
    cursor = db_connection.cursor()

    q_file_name = QUERY_STR + str(query_num) + QUERY_FILE_EXTENSION
    file_path = Path(__file__).parent / 'queries' / q_file_name
    
    with open(file_path, 'r') as f:
        query = f.read()

    cursor.execute(query)
    results = cursor.fetchall()

    return results

def main():

    init()

    subjects = get_subjects()

    # 1. get 5 students with highest grade point average in all subjects
    query_num = 1
    results = get_db_results(query_num)    

    print(f"\n\n{Fore.BLUE}1. 5 students with highest grade point average in all subjects{Fore.RESET}:\n")
    for row in results:
        print(f"Student: {row[1]} {row[2]}, Average Grade: {round(row[3], 2)}")

    # 2. get student with highest grade point in definitive subject
    query_num = 2
    results = get_db_results(query_num) 

    print(f"\n\n{Fore.BLUE}2. student with highest grade point in definitive subject{Fore.RESET}:\n")
    for row in results:
        grade = round(row[3],2)
        print(f"Student: {row[1]} {row[2]}, Subject: {row[4]}, Grade: {grade}")

    # 3. get average point in groups in definitive subject
    query_num = 3
    results = get_db_results(query_num)

    print(f"\n\n{Fore.BLUE}3. Average point in groups:{Fore.RESET}\n")

    for row in results:
        grade = round(row[2],2)
        print(f"Group: {row[0]}, Subject: {row[1]}, Grade: {grade}")

    #4. average point in grade
    query_num = 4
    results = get_db_results(query_num) 

    print(f"\n\n{Fore.BLUE}4. Average point in grade{Fore.RESET}:\n")
    for row in results:
        grade = round(row[0],2)
        print(f"Grade: {grade}")

    #5. get all courses of definitive teacher
    query_num = 5
    results = get_db_results(query_num)

    print(f"\n\n{Fore.BLUE}5. All courses of definitive teacher{Fore.RESET}:\n")

    if results:
        teacher_first_name = results[0][1]
        teacher_last_name = results[0][2]

        print(f"Teacher: {teacher_first_name} {teacher_last_name}\nSubjects:\n")
        subjects = set()
        for row in results:
            subjects.add(row[0])
        #for row in results:
            #subjects.add(row[0])
        print(f"{(', ').join(subjects)}")
    else:
        print(f"\n\n{Fore.BLUE}5. Get all courses of definitive teacher:{Fore.RESET} {Fore.RED}no courses was found{Fore.RESET}\n")

    #6. get students in a definitive group
    query_num = 6
    results = get_db_results(query_num) 

    if len(results) > 0:
        group_name = results[0][2]
        print(f"\n\n{Fore.BLUE}6. Students in the group {group_name}{Fore.RESET}: \n")

        if results:
            for row in results:
                print(f"{row[0]} {row[1]}")
        else:
            print(f"\n\n{Fore.BLUE}6. Get students in a definitive group:{Fore.RESET} {Fore.RED}There is no students in this group{Fore.RESET}\n")
    else:
        print(f"\n\n{Fore.BLUE}6. Get students in a definitive group:{Fore.RESET} {Fore.RED} there is no students in the group{Fore.RESET}\n")

    #7. student's points in definitive group in definitive subject
    query_num = 7
    results = get_db_results(query_num) 

    if results:
        print(f"\n\n{Fore.BLUE}7. Student's points in definitive group in definitive subject{Fore.RESET}:\n")

        student = results[0][0] + " " + results[0][1] 
        group = results[0][3]
        subject = results[0][4]

        print(f"Group: {group}, Subject: {subject}, Student: {student}\nPoints:\n")
        grades = []

        for row in results:
            grades.append(str(row[2]))
        print(f"{(', ').join(grades)}")
    else:
        print(f"\n\n{Fore.BLUE}7. Student's points in definitive group in definitive subject: {Fore.RESET} {Fore.RED} no point was found{Fore.RESET}")

    #8. get average point, that definitive teacher gives in his subjects
    query_num = 8
    results = get_db_results(query_num) 

    if len(results) > 0 and results[0][1] is not None and results[0][2] is not None:
        teacher = results[0][1] + " " + results[0][2]
        print(f"\n\n{Fore.BLUE}8. Average point, that teacher {teacher} gives in his (her) subjects{Fore.RESET}:\n")

        for row in results:
            grade = round(row[0], 2)
            print(f"{grade}")
    else:
        print(f"\n\n{Fore.BLUE}8. Get average point, that definitive teacher gives in his subjects: {Fore.RESET} {Fore.RED} no results{Fore.RESET}\n")

    #9. get courses, that visits definitive student
    query_num = 9
    results = get_db_results(query_num) 

    student = results[0][1] + " " + results[0][2]
    print(f"\n\n{Fore.BLUE}9. Student {student} visits{Fore.RESET}:\n")

    subjects = set()

    for row in results:
        subjects.add(row[0])
    print(f"{(', ').join(subjects)}")

    #10. get courses, that devinitive teacher teaches to definitive student
    query_num = 10
    results = get_db_results(query_num) 

    if results:

        teacher = results[0][1] + " " + results[0][2]
        student = results[0][3] + " " + results[0][4]

        print(f"\n\n{Fore.BLUE}10. The teacher {teacher} teaches to student {student}{Fore.RESET}:\n")

        subjects = set()

        for row in results:
            subjects.add(row[0])
        print(f"{', '.join(subjects)}")
    else:
        print(f"\n\n{Fore.BLUE}10. Get courses, that definitive teacher teaches to definitive student: {Fore.RESET} {Fore.RED} no results {Fore.RESET}")

    #A1. get average point, that definitive teacher gives to definitive student
    query_num = 11
    results = get_db_results(query_num) 

    if results and len(results[0]) > 0:
        teacher = results[0][3] + " " + results[0][4]
        student = results[0][1] + " " + results[0][2]
        print(f"\n\n{Fore.BLUE} A1. Average point, that teacher {teacher} gives to student {student}{Fore.RESET}:\n")

        for row in results:
            print(f"{round(row[0], 2)}")
    else:
        print(f"\n\n{Fore.BLUE} A1. Average point, that definitive teacher gives to a definitive student: {Fore.RESET} {Fore.RED} no results {Fore.RESET}\n")

    #A2. Get student's points in a definitive group in definitive subject on the last lesson
    query_num = 12
    results = get_db_results(query_num) 

    if results:
        group = results[0][4]
        subject = results[0][3]
        print(f"\n\n{Fore.BLUE}A2. Student's points in a group {group} in subject {subject} on the last lesson {Fore.RESET}:\n")
        
        grades = []
        
        for row in results:
            grades.append(str(row[2]))
            
        print(f"\n{', '.join(grades)}\n")
    else:
        print("\n\n no results")

if __name__ == '__main__':
    create_tables()
    add_data()
    main()