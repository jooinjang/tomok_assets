import os
from pathlib import Path
import re, ast, argparse


def extract_function_string(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    func_str = ""
    in_function = False
    decorator_found = False

    for line in lines:
        if "@rule_method" in line.strip():
            decorator_found = True
            in_function = False
            func_str += line
        if decorator_found and "def" in line:
            func_str += line
            in_function = True
            decorator_found = False  # Reset to ensure multiple methods aren't captured
        elif in_function and "return" in line:
            func_str += line
            break
        elif in_function:
            func_str += line

    return func_str


def remove_leading_spaces(text):
    # Split the text into lines, remove leading 4 spaces, and rejoin back into text
    lines = text.split("\n")
    trimmed_lines = [line[4:] if line.startswith("    ") else line for line in lines]
    return "\n".join(trimmed_lines)


def remove_first_computed_variable(func_str):
    # Parse the function into an AST
    func_ast = ast.parse(func_str)
    visitor = ComputedVariableVisitor()

    # Traverse the AST to find the first assignment
    visitor.visit(func_ast)

    # Get the name of the first computed variable
    computed_var = visitor.first_computed_variable()
    if not computed_var:
        return "OK"
        # raise ValueError("No variable computation found inside the function.")

    # Create regex pattern to find and remove the computed variable from the function signature
    pattern = r"\b{}\b[, ]".format(computed_var)

    # Find the function definition line
    func_def_line = re.search(r"^(def [^\(]*\([^\)]*\))", func_str, flags=re.MULTILINE)
    if func_def_line:
        # Replace the computed variable in the function definition
        new_func_def = re.sub(pattern, "", func_def_line.group(0))
        new_func_def = re.sub(
            r"\s*\s*, ", ", ", new_func_def
        )  # Fix doubled commas, if any
        new_func_def = re.sub(
            r",\s*\)", ")", new_func_def
        )  # Remove trailing comma, if any

        # Replace the old function definition with the new one in the function string
        new_func_str = func_str.replace(func_def_line.group(0), new_func_def)

        return new_func_str
    else:
        return func_str


class ComputedVariableVisitor(ast.NodeVisitor):
    def __init__(self):
        self._first_computed_var = None

    def visit_Assign(self, node):
        if not self._first_computed_var:
            if isinstance(node.targets[0], ast.Name):
                self._first_computed_var = node.targets[0].id

    def first_computed_variable(self):
        return self._first_computed_var


def collect_python_files(base_path):
    base_path = Path(base_path).resolve()
    python_files = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                full_path = Path(root) / file
                relative_path = full_path.relative_to(base_path)
                python_files.append(str(relative_path))

    return python_files


def remove_assigned_parameters(func_text):
    # Extract the function definition line using regular expression
    func_def = re.search(r"def\s+\w+\((.*?)\)", func_text, re.DOTALL)
    if not func_def:
        return "Function definition not found."

    # Extract all parameters from the function definition
    params = func_def.group(1).split(",")

    # Check if each parameter is assigned before use
    for param in params:
        param = param.strip()
        # Pattern to find assignment before use
        pattern = r"(\b" + re.escape(param) + r"\b\s*=)"
        # If parameter is assigned before use, remove it from the list
        if re.search(pattern, func_text, re.DOTALL):
            params.remove(param)

    # Reconstruct the function definition with unassigned parameters
    new_func_def = re.sub(
        r"\(.*?\)", "(" + ", ".join(params) + ")", func_def.group(0), 1
    )
    # Replace the old function definition with the new one in the original function text
    new_func_text = re.sub(re.escape(func_def.group(0)), new_func_def, func_text, 1)

    return new_func_text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_path", type=str, default="./ruleunits")
    args = parser.parse_args()

    py_paths = collect_python_files(args.base_path)

    for p in py_paths:
        print(p)
        p = os.path.join(args.base_path, p)
        func_str = extract_function_string(p)
        func_str = remove_leading_spaces(func_str)
        # new_func_str = remove_first_computed_variable(func_str)
        # if new_func_str == "OK":
        #     continue

        new_func_str = remove_assigned_parameters(func_str)
        # if new_func_str == "Function definition not found.":
        #     continue

        with open(p, "r") as fp:
            temp = fp.readlines()
        contents = ""
        for line in temp:
            contents += line

        sliced_func = func_str.split("\n")
        sliced_new_func = new_func_str.split("\n")

        for f_line, new_f_line in zip(sliced_func, sliced_new_func):
            contents = contents.replace(f_line, new_f_line)

        with open(p, "w") as fp:
            fp.write(contents)
