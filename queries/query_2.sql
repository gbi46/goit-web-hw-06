   SELECT g.student_id, s.first_name, s.last_name, AVG(grade) AS avg_grade, sj.subject_name
    FROM grades g
    JOIN students s ON g.student_id = s.student_id
    JOIN subjects sj ON sj.subject_id = g.subject_id
    WHERE g.subject_id = 2
    GROUP BY g.student_id
    ORDER BY avg_grade DESC
    LIMIT 1