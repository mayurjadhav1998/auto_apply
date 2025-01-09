import subprocess

commands = [
    "python -m pip install --upgrade pip",
    "pip install selenium webdriver-manager",
    "pip install --upgrade tensorflow",
    "python 0_1yrs.py",
    "python 1_3yrs.py",
    "python backend_dev0_1.py",
    "python backend_dev1_3.py",
    "python frontend_dev0_1.py",
    "python frontend_dev1_3.py",
    "python python_dev_0_1.py",
    "python python_dev1_3.py",
    "python ROR_0_1yrs.py",
    "python ROR_1_3yrs.py",
    "python django_0_1yrs.py",
    "python django_1_3.py",
    "python java_0_1yrs.py",
    "python java_1_3yrs.py",
    "python run_all.py"
    
]

for cmd in commands:
    subprocess.run(cmd, shell=True, check=True)
