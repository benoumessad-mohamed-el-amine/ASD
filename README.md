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
.\venv\Scripts\python.exe student_project\run.py
```

## student project - notebook

```
.\venv\Scripts\jupyter.exe notebook student_project\main.ipynb
```