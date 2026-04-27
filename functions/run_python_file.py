import os
import subprocess
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python script in a specified directory relative to the working directory, providing output results",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to python scripts files from, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Content inside args"
                ),
                description="Additional arguments required for the script to work",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    valid_path = os.path.dirname(target_file)

    if not valid_target_file:
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    if not target_file.endswith(".py"):
        return (f'Error: "{file_path}" is not a Python file')
    if not os.path.isfile(target_file):
        return (f'Error: "{file_path}" does not exist or is not a regular file')
    #if not os.path.exists(valid_path):
    #    os.makedirs(valid_path)
    
    command = ["python", target_file]
    if args is not None:
        command.extend(args)
    
    results = subprocess.run(command,text=True,timeout=30,capture_output=True)
    output = ''
    
    if results.returncode != 0:
        output += f"Process exited with code {results.returncode}\n"
    if not results.stdout and not results.stderr:
        output += f"No output produced\n"
    if results.stdout:
        output += f"STDOUT: {results.stdout}\n"
    if results.stderr:
        output += f"STDERR: {results.stderr}\n"   
     
    return output
        
