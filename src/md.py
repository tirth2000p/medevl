import os
import re

# Define the directory with your files
dir_path = "mock"

# Initialize a list for storing the extracted docstrings
docstrings = []

# Define a regex pattern for extracting docstrings
docstring_pattern = re.compile(r'"""(.*?)"""', re.DOTALL)

# Iterate over files in the directory
for entry in os.scandir(dir_path):
    if entry.path.endswith(".py") and entry.is_file():
        with open(entry.path, "r") as file:
            contents = file.read()
            # Search for docstrings in the file contents
            matches = docstring_pattern.findall(contents)

            if matches:
                # Get all function definitions in the file
                function_defs = re.findall(r'def\s+(\w+)\s*\(', contents)
                for idx, match in enumerate(matches[:len(function_defs)]):
                    # Match each docstring with its corresponding function name
                    docstrings.append((function_defs[idx], match.strip()))

# Save the extracted docstrings to a Markdown file
doc_file_path = "../Documentation/developerdocumentation.md"
with open(doc_file_path, "w") as doc_file:
    for docstring in docstrings:
        doc_file.write(f"# {docstring[0]}\n\n")
        doc_file.write(f"* {docstring[1]}\n\n")

print(f"Documentation generated in '{doc_file_path}'")
