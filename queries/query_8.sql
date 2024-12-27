SELECT AVG(g.grade) AS avg_grade, th.first_name, th.last_name
    FROM grades g
    JOIN subjects sj ON g.subject_id = sj.subject_id
    JOIN teachers th ON th.teacher_id = sj.teacher_id
    WHERE sj.teacher_id = 4