SELECT s.subject_name, th.first_name, th.last_name
    FROM subjects s
    JOIN teachers th ON th.teacher_id = s.teacher_id
    WHERE s.teacher_id = 2