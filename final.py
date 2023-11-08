from pylint.lint import Run
files_to_lint = ['flaskapp.py','data_leakage.py','insecure_authentication.py','app3.py']  # Replace with the path to your Python file
# results = Run(["--rcfile=.pylintrc"] + files_to_lint, exit=False)
results = Run(["--rcfile=.pylintrc"] + files_to_lint, exit=False)
