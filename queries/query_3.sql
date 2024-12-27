SELECT gr.group_name, sj.subject_name, AVG(grade) AS avg_grade
    FROM grades g
    JOIN students s ON g.student_id = s.student_id
    JOIN groups gr ON s.group_id = gr.group_id
    JOIN subjects sj ON sj.subject_id = g.subject_id
    WHERE g.subject_id = 3
    GROUP BY gr.group_id