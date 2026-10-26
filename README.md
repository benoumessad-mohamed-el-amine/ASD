# ASD

## activate venv

```
.\venv\Scripts\Activate.ps1
```

if execution policy error:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

## install dependencies

```
.\venv\Scripts\python.exe -m pip install matplotlib pandas jupyter
```

## sales project

```
.\venv\Scripts\python.exe Sales_project\scripts\create_products.py
```

## student project - report

```
.\venv\Scripts\python.exe -c "import sys; sys.path.append('student_project'); from students import generate_students; from analysis import calculate_class_statistics, save_report; s = generate_students(10); stats = calculate_class_statistics(s); save_report(s, stats, 'student_project/results/report.txt'); print('done')"
```

## student project - notebook

```
.\venv\Scripts\jupyter.exe notebook student_project\main.ipynb
```