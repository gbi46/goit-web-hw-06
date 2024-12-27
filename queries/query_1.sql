SELECT g.student_id, s.first_name, s.last_name AS student, AVG(g.grade) AS avg_grade
    FROM grades g
    JOIN students s ON g.student_id = s.student_id
    GROUP BY g.student_id
    ORDER BY avg_grade DESC
    LIMIT 5