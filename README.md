# ASD

ok so to run this stuff you need to activate the venv first

```
.\venv\Scripts\Activate.ps1
```

if that doesnt work (execution policy error or whatever) run this before it:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

## install the dependencies

```
.\venv\Scripts\python.exe -m pip install matplotlib pandas jupyter
```

## run the sales project

```
.\venv\Scripts\python.exe Sales_project\scripts\create_products.py
```

## run the student project (report)

```
.\venv\Scripts\python.exe -c "import sys; sys.path.append('student_project'); from students import generate_students; from analysis import calculate_class_statistics, save_report; s = generate_students(10); stats = calculate_class_statistics(s); save_report(s, stats, 'student_project/results/report.txt'); print('done')"
```

## run the student project (jupyter notebook)

```
.\venv\Scripts\jupyter.exe notebook student_project\main.ipynb
```