# PowerShell Run Guide

## 1. Virtual Environment Setup

### Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```
> *If PowerShell prevents script execution, run this first:*
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> .\venv\Scripts\Activate.ps1
> ```

### Or Run Directly Without Activation
```powershell
.\venv\Scripts\python.exe <path-to-script>
```

---

## 2. Install / Manage Dependencies
```powershell
.\venv\Scripts\python.exe -m pip install matplotlib pandas jupyter
```

---

## 3. Run Sales Project
Generates and displays the total sales bar chart:
```powershell
.\venv\Scripts\python.exe Sales_project\scripts\create_products.py
```

---

## 4. Run Student Project

### Generate Analysis & Report (`report.txt`)
```powershell
.\venv\Scripts\python.exe -c "import sys; sys.path.append('student_project'); from students import generate_students; from analysis import calculate_class_statistics, save_report; s = generate_students(10); stats = calculate_class_statistics(s); save_report(s, stats, 'student_project/results/report.txt'); print('Report generated successfully in student_project/results/report.txt')"
```

### Launch Jupyter Notebook
```powershell
.\venv\Scripts\jupyter.exe notebook student_project\main.ipynb
```