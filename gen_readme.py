import subprocess
import os

files = [f"task{i}.py" for i in range(1, 10)]
outputs = {}

print("Running files to generate outputs for README...")

for file in files:
    if os.path.exists(file):
        # Run the file and capture the output
        result = subprocess.run(["python", file], capture_output=True, text=True)
        outputs[file] = result.stdout.strip()
    else:
        outputs[file] = "File not found. Please make sure the file exists."

# Build the README content
readme = "# Assignment 10: Pandas (Series, DataFrame, Functions, Filtering & Analysis)\n\n"
readme += "This assignment demonstrates data manipulation, filtering, grouping, and basic plotting using the Pandas library.\n\n"
readme += "## Folder Structure\n"
readme += "GenAI-Task10-PKhalilulla-Khan/\n"
for f in files:
    readme += f"├── {f}\n"
readme += "└── README.md\n\n"
readme += "## Code Execution Output\n\n"

for file, output in outputs.items():
    task_name = file.replace(".py", "").capitalize()
    readme += f"### {task_name}\n"
    readme += f"```text\n{output}\n```\n\n"

# Write to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("Success! README.md has been generated with all task outputs.")
