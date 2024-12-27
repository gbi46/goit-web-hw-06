SELECT s.first_name, s.last_name, gr.grade, sj.subject_name, grp.group_name
    FROM grades gr
    JOIN students s ON s.student_id = gr.student_id
    JOIN groups grp ON grp.group_id = s.group_id
    JOIN subjects sj ON sj.subject_id = gr.subject_id
    WHERE s.group_id = 1 AND gr.subject_id = 8
    ORDER BY gr.date DESC
    LIMIT 7