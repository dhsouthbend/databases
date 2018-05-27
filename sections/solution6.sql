SELECT student, program_name, gpa
FROM students INNER JOIN gpas
ON gpas.id_student = students.id
INNER JOIN programs
ON programs.id = students.id_program
ORDER BY gpas.gpa ASC;
