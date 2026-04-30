from config import WORKING_DIRECTORY
from functions.get_file_content import *
from functions.get_files_info import *
from functions.run_python_file import *
from functions.write_file import *

def call_function(function_call, verbose=False):

    if verbose:
        print(f"Calling function: {function_call.function.name}({function_call.function.arguments})")
    else:
        print(f" - Calling function: {function_call.function.name}")

    function_map = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
    }
    function_name = function_call.function.name or ""
    if function_name not in function_map:
        return ({
            "role":"tool",
            "tool_name":function_name,
            "content":f"error Unknown function: {function_name}",}
        )
    
    args = dict(function_call.function.arguments) if function_call.function.arguments else {}
    args["working_directory"] = WORKING_DIRECTORY
    
    if function_name in function_map:
        function_result = function_map[function_name](**args)
        return ({
            "role":"tool",
            "tool_name":function_name,
            "content":function_result,}
        )