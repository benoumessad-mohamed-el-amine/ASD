import os
import statistics
from datetime import date


def calculate_age(birth_date):
    birth_year = int(birth_date.split("-")[0])
    current_year = date.today().year
    return current_year - birth_year


def calculate_student_average(grades):
    return round(sum(grades) / len(grades), 2)


def calculate_class_statistics(students):
    averages = []
    ages = []
    for s in students:
        averages.append(s["average"])
        ages.append(s["age"])

    return {
        "mean": round(statistics.mean(averages), 2),
        "median": round(statistics.median(averages), 2),
        "standard_deviation": round(statistics.stdev(averages), 2),
        "min_average": min(averages),
        "max_average": max(averages),
        "mean_age": round(statistics.mean(ages), 2)
    }


def save_report(students, stats, output_path="results/report.txt"):
    if not os.path.exists("results"):
        os.makedirs("results")

    with open(output_path, "w") as f:
        f.write("Student Report\n")
        f.write("--------------------\n")
        for s in students:
            f.write("ID: " + str(s["student_id"]) + " | Birth Date: " + str(s["birth_date"]) + " | Age: " + str(s["age"]) + " | Average: " + str(s["average"]) + " | Grades: " + str(s["grades"]) + "\n")

        f.write("\nClass Statistics\n")
        f.write("--------------------\n")
        f.write("Mean: " + str(stats["mean"]) + "\n")
        f.write("Median: " + str(stats["median"]) + "\n")
        f.write("Standard Deviation: " + str(stats["standard_deviation"]) + "\n")
        f.write("Min: " + str(stats["min_average"]) + "\n")
        f.write("Max: " + str(stats["max_average"]) + "\n")
        f.write("Mean Age: " + str(stats["mean_age"]) + "\n")
