import os

def write_file(working_directory, file_path, content):
    working_directory_path = os.path.abspath(working_directory)
    file_path_arg = os.path.abspath(os.path.join(working_directory, file_path))
    directory_path = os.path.dirname(file_path_arg)
    if not file_path_arg.startswith(working_directory_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    with open(file_path_arg, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'