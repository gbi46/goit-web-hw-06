SELECT AVG(gr.grade) AS avg_grade, s.first_name, s.last_name, th.first_name, th.last_name
    FROM grades gr
    JOIN subjects sj ON gr.subject_id = sj.subject_id
    JOIN students s ON s.student_id = gr.student_id
    JOIN teachers th ON th.teacher_id = sj.teacher_id
    WHERE gr.student_id = 8 AND sj.teacher_id = 5