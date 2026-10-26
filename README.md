<style>
  @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Patrick+Hand&family=Kalam:wght@400;700&display=swap');

  /* Notebook handwriting aesthetic */
  body, .vscode-body {
    font-family: 'Caveat', 'Ink Free', 'Segoe Print', 'Patrick Hand', 'Kalam', 'Comic Sans MS', cursive, sans-serif !important;
    font-size: 19px !important;
    line-height: 1.85 !important;
    letter-spacing: 0.3px;
    color: #24292e;
    background-color: #faf8f0 !important;
    background-image: 
      linear-gradient(90deg, transparent 54px, #f87171 55px, #f87171 57px, transparent 58px),
      linear-gradient(#e5e1d3 1px, transparent 1px) !important;
    background-size: 100% 2.2rem !important;
    padding: 30px 40px 40px 75px !important;
  }

  /* Dark mode chalkboard / dark journal support */
  @media (prefers-color-scheme: dark) {
    body, .vscode-body, .vscode-dark {
      color: #f1f5f9 !important;
      background-color: #1a1a22 !important;
      background-image: 
        linear-gradient(90deg, transparent 54px, rgba(239, 68, 68, 0.45) 55px, rgba(239, 68, 68, 0.45) 57px, transparent 58px),
        linear-gradient(rgba(255, 255, 255, 0.06) 1px, transparent 1px) !important;
    }
  }

  h1, h2, h3, h4 {
    font-family: 'Caveat', 'Ink Free', 'Segoe Print', 'Patrick Hand', cursive !important;
    font-weight: 700 !important;
    letter-spacing: 0.8px;
    margin-top: 1.2em !important;
  }

  h1 {
    font-size: 2.5rem !important;
    color: #1e3a8a !important;
    border-bottom: 3px wavy #3b82f6 !important;
    display: inline-block;
    padding-bottom: 2px;
  }

  h2 {
    font-size: 1.8rem !important;
    color: #0369a1 !important;
    margin-bottom: 0.4em !important;
  }

  h3 {
    font-size: 1.35rem !important;
    color: #0f766e !important;
  }

  /* Post-It sticky notes */
  blockquote {
    position: relative;
    background: #fef9c3 !important;
    color: #713f12 !important;
    border-left: 6px solid #eab308 !important;
    border-radius: 4px 14px 6px 16px !important;
    padding: 14px 20px !important;
    margin: 18px 0 !important;
    box-shadow: 3px 4px 12px rgba(0, 0, 0, 0.08) !important;
    transform: rotate(-0.6deg);
  }

  /* Clean readable code cards pinned onto notebook */
  pre {
    background: #1e293b !important;
    border: 2px dashed #94a3b8 !important;
    border-radius: 8px !important;
    padding: 14px 16px !important;
    box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.15) !important;
    overflow-x: auto;
  }

  code {
    font-family: 'Consolas', 'Cascadia Code', 'Fira Code', monospace !important;
    font-size: 0.95em !important;
  }

  /* Inline highlighted tags */
  :not(pre) > code {
    font-family: 'Consolas', monospace !important;
    background: #fef08a !important;
    color: #854d0e !important;
    padding: 2px 7px !important;
    border-radius: 4px !important;
    border: 1px dashed #ca8a04 !important;
  }

  hr {
    border: none !important;
    border-top: 2px dashed #cbd5e1 !important;
    margin: 30px 0 !important;
  }

  ul, ol {
    padding-left: 24px !important;
  }

  li {
    margin-bottom: 6px !important;
  }
</style>

# ✍️ 𝒫𝑜𝓌𝑒𝓇𝒮𝒽𝑒𝓁𝓁 𝑅𝓊𝓃 𝒢𝓊𝒾𝒹𝑒 📓
*— personal field notes & quick-start cheatsheet —*

---

## ① Virtual Environment Setup ⚙️

First things first, activate the local `.venv`:

```powershell
.\venv\Scripts\Activate.ps1
```

> 📌 **Note to self:** If PowerShell blocks script execution with a permissions error, run this quick unlock command first:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> .\venv\Scripts\Activate.ps1
> ```

<br>

↳ **Alternative:** Or run scripts directly through Python without activating:
```powershell
.\venv\Scripts\python.exe <path-to-script>
```

---

## ② Dependencies 📦

Keep the environment stocked with our core libraries (`matplotlib`, `pandas`, `jupyter`):

```powershell
.\venv\Scripts\python.exe -m pip install matplotlib pandas jupyter
```

---

## ③ Sales Project 📊

Generate and display the total sales bar chart:

```powershell
.\venv\Scripts\python.exe Sales_project\scripts\create_products.py
```

↳ *Creates fresh product sales data and plots the interactive chart.*

---

## ④ Student Project 🎓

### ✎ Generate Analysis & Report (`report.txt`)
Run the automated calculation pipeline:

```powershell
.\venv\Scripts\python.exe -c "import sys; sys.path.append('student_project'); from students import generate_students; from analysis import calculate_class_statistics, save_report; s = generate_students(10); stats = calculate_class_statistics(s); save_report(s, stats, 'student_project/results/report.txt'); print('Report generated successfully in student_project/results/report.txt')"
```

↳ *Generates 10 students, evaluates class statistics, and writes the output directly to `student_project/results/report.txt`.*

### ✎ Launch Interactive Jupyter Notebook
```powershell
.\venv\Scripts\jupyter.exe notebook student_project\main.ipynb
```

---

*✎ Happy coding! Keep this note handy.* ✨