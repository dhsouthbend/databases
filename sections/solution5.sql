SELECT student, program_level
FROM students INNER JOIN programs
ON students.id_program = programs.id;