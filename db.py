from connection import create_connection
from data import get_groups, get_subjects
from faker import Faker

db_connection = create_connection()
cursor = db_connection.cursor()

def create_tables():
    with open('create_tables.sql', 'r') as cr_tbl_file:
        query = cr_tbl_file.read()
        queries = query.split(';')
        
        for q in queries:
            cursor.execute(q)

def add_data():
    fake = Faker()

    # add groups
    groups = get_groups()
    for group in groups:
        cursor.execute('INSERT INTO groups (group_name) VALUES (?)', (group,))

    # add teachers
    teachers = [(fake.first_name(), fake.last_name()) for _ in range(5)]
    for teacher in teachers:
        cursor.execute('INSERT INTO teachers (first_name, last_name) VALUES (?, ?)', teacher)

    # add subjects
    subjects = get_subjects()
    for subject in subjects:
        teacher_id = fake.random_int(1, 5)
        cursor.execute('INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)', (subject, teacher_id))

    # add students
    for _ in range(50):
        first_name = fake.first_name()
        last_name = fake.last_name()
        group_id = fake.random_int(1, 3)
        cursor.execute('INSERT INTO students (first_name, last_name, group_id) VALUES (?, ?, ?)', (first_name, last_name, group_id))

    # add grades
    for student_id in range(1, 51):
        for subject_id in range(1, len(subjects)):
            grade = fake.random_int(1, 5)
            date = fake.date_this_year()
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade, date))

    # confirm changes in db
    db_connection.commit()