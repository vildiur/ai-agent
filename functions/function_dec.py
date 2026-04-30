available_functions = [
    {
        "type": "function",
        "function": {
            "name": "get_file_content",
            "description": "Read file content in a specified directory relative to the working directory, providing output results",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to files from, relative to the working directory (default is the working directory itself)"
                    }
                },
                "required": ["file_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_files_info",
            "description": "Lists directories and files in a specified directory, providing file size and directory status",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)"
                    }
                },
                "required": ["directory"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_python_file",
            "description": "Run python script in a specified directory relative to the working directory, providing output results",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to python scripts files from, relative to the working directory (default is the working directory itself)"
                    },
                    "args": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "Content inside args"
                        },                      
                        "description": "Additional arguments required for the script to work"
                    },
                },
                "required": ["file_path,"]                
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write file in a specified directory relative to the working directory, providing output results",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to files from, relative to the working directory (default is the working directory itself)"
                    },
                    "content": {
                        "type": "string",
                        "description": "Input of content that will be written to the file"
                    },                      
                },
                "required": ["file_path","content"]
            }
        }
    }
]