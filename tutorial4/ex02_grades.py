import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(101)
grades_of_students = np.random.randint(0, 21, size=(100, 5))
modules = ['THL', 'DSS', 'DB', 'SE', 'RE']

print("First 5 students:\n", grades_of_students[:5])

mean_per_student = grades_of_students.mean(axis=1)
mean_per_module = grades_of_students.mean(axis=0)
median_per_module = np.median(grades_of_students, axis=0)
var_per_module = grades_of_students.var(axis=0)
std_per_module = grades_of_students.std(axis=0)

print("Mean per student:", mean_per_student)
print("Mean per module:", mean_per_module)
print("Median per module:", median_per_module)
print("Variance per module:", var_per_module)
print("Std per module:", std_per_module)
print("Overall min:", grades_of_students.min(), "max:", grades_of_students.max())

thl = grades_of_students[:, 0]
print("THL percentiles (25/50/75):", np.percentile(thl, [25, 50, 75]))

mask = (grades_of_students >= 10) & (grades_of_students <= 15)
print("Count grades 10-15:", mask.sum())
print("Grades 10-15:", grades_of_students[mask])

plt.figure()
plt.bar(modules, mean_per_module)
plt.title("Average Grades per Module")
plt.xlabel("Module")
plt.ylabel("Average Grade")
plt.tight_layout()
plt.savefig("tutorial4/avg_grades.png")
plt.close()

plt.figure()
plt.boxplot(grades_of_students, tick_labels=modules)
plt.title("Grade Distribution per Module")
plt.xlabel("Module")
plt.ylabel("Grade")
plt.tight_layout()
plt.savefig("tutorial4/boxplot_grades.png")
plt.close()

all_above_15 = np.where(grades_of_students.min(axis=1) > 15)[0]
print("Students with all grades > 15:", all_above_15)

top5_idx = mean_per_student.argsort()[-5:][::-1]
print("Top 5 students:", top5_idx)

best_module = modules[mean_per_module.argmax()]
print("Module with highest average:", best_module)
