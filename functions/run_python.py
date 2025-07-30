import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_directory_path = os.path.abspath(working_directory)
    file_path_arg = os.path.abspath(os.path.join(working_directory, file_path))
    process_args = ["python3", file_path_arg] + args
    if not file_path_arg.startswith(working_directory_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_path_arg):
        return f'Error: File "{file_path}" not found.'
    if not file_path_arg.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        completed_process = subprocess.run(process_args, capture_output=True, timeout=30, cwd=working_directory_path, text=True)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    result_output = ''

    if completed_process.stdout:
        result_output += f'STDOUT:{completed_process.stdout}\n'
    if completed_process.stderr:
        result_output += f'STDERR:{completed_process.stderr}\n'
    if completed_process.returncode != 0:
        result_output += f'Process exited with code {completed_process.returncode}'

    if not result_output:
        result_output = "No output produced."

    return result_output
