import re, ast, argparse

def extract_function_string(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    func_str = ""
    in_function = False
    decorator_found = False

    for line in lines:
        if '@rule_method' in line.strip():
            decorator_found = True
            in_function = False
            func_str += line
        if decorator_found and 'def' in line:
            func_str += line
            in_function = True
            decorator_found = False  # Reset to ensure multiple methods aren't captured
        elif in_function and 'return' in line:
            func_str += line
            break
        elif in_function:
            func_str += line

    return func_str


def remove_leading_spaces(text):
    # Split the text into lines, remove leading 4 spaces, and rejoin back into text
    lines = text.split('\n')
    trimmed_lines = [line[4:] if line.startswith('    ') else line for line in lines]
    return '\n'.join(trimmed_lines)


def remove_first_computed_variable(func_str):
    # Parse the function into an AST
    func_ast = ast.parse(func_str)
    visitor = ComputedVariableVisitor()
    
    # Traverse the AST to find the first assignment
    visitor.visit(func_ast)
    
    # Get the name of the first computed variable
    computed_var = visitor.first_computed_variable()
    if not computed_var:
        raise ValueError("No variable computation found inside the function.")
    
    # Create regex pattern to find and remove the computed variable from the function signature
    pattern = r'\b{}\b[, ]'.format(computed_var)
    
    # Find the function definition line
    func_def_line = re.search(r'^(def [^\(]*\([^\)]*\))', func_str, flags=re.MULTILINE)
    if func_def_line:
        # Replace the computed variable in the function definition
        new_func_def = re.sub(pattern, '', func_def_line.group(0))
        new_func_def = re.sub(r'\s*\s*,', ', ', new_func_def)  # Fix doubled commas, if any
        new_func_def = re.sub(r',\s*\)', ')', new_func_def)  # Remove trailing comma, if any

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path')
    args = parser.parse_args()
    
    func_str = extract_function_string(args.file_path)
    func_str = remove_leading_spaces(func_str)
    new_func_str = remove_first_computed_variable(func_str)
    print(new_func_str)

# python rule_unit_parsing.py --file_path tomok_ex.py