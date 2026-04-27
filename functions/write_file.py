import os
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write file in a specified directory relative to the working directory, providing output results",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path","content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to files from, relative to the working directory (default is the working directory itself)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Input of content that will be written to the file",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    valid_path = os.path.dirname(target_file)

    if not valid_target_file:
        return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    if os.path.isdir(target_file):
        return (f'Error: Cannot write to "{file_path}" as it is a directory')
    if not os.path.exists(valid_path):
        os.makedirs(valid_path)

    with open(target_file, 'w') as f:
        f.write(content)

    return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
