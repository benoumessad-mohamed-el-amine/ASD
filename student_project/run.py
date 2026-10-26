from students import generate_students
from analysis import calculate_class_statistics, save_report

s = generate_students(10)
stats = calculate_class_statistics(s)
save_report(s, stats, 'student_project/results/report.txt')
print('done')
