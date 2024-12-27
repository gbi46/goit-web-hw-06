SELECT sj.subject_name, s.first_name, s.last_name
    FROM subjects sj
    JOIN grades gr ON sj.subject_id = gr.subject_id
    JOIN students s ON s.student_id = gr.student_id
    WHERE gr.student_id = 6