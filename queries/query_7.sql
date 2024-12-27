SELECT students.first_name, students.last_name, g.grade, gr.group_name, sj.subject_name
    FROM grades g
    JOIN students ON g.student_id = students.student_id
    JOIN groups gr ON gr.group_id = students.group_id
    JOIN subjects sj ON sj.subject_id = g.subject_id
    WHERE students.group_id = 2 AND g.subject_id = 5