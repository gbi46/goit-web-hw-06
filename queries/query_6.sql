SELECT s.first_name, s.last_name, gr.group_name
    FROM students s
    JOIN groups gr ON gr.group_id = s.group_id
    WHERE s.group_id = 1