import os
from os.path import join
import nbformat
from nbconvert import PythonExporter

import re

IMPORT_CONTENTS = """import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List
"""


def split_string(s):
    # Splitting based on underscore
    parts = s.split('_')

    # Further splitting each part if it contains consecutive numbers and letters, and is not purely numeric
    split_parts = []
    for part in parts:
        if part.isdigit():  # If the part is purely numeric, keep it as is
            split_parts.append(part)
        else:  # Otherwise, split into consecutive numbers and letters
            split_part = re.findall(r'[A-Za-z]+|\d+', part)
            split_parts.extend(split_part)

    return split_parts


def build_ruleunit_dirs(fname: str):
    fname_str = fname.replace(".ipynb", "")
    dirnames = split_string(fname_str)
    
    dirnames[0] = dirnames[0].lower()
    if len(dirnames) == 4:
        dirnames[2] = dirnames[2] + '_' + dirnames[3]
        dirnames = dirnames[:-1]
    
    cur_dir = "./ruleunits"
    for dname in dirnames[:-1]:
        cur_dir = join(cur_dir, dname)
        if not os.path.exists(cur_dir):
            os.makedirs(cur_dir, exist_ok=True)
    
    # return target_dir, target_fname
    return cur_dir, dirnames[-1]


def ipynb_2_py(f_path, contents):
    first = -1
    last = 99999
    for i, line in enumerate(contents):
        if "# 작성하는 룰에 맞게 클래스 이름 수정" in line:
            first = i
        if "작성한 룰 유닛은 아래의 코드 블럭과 같이 생성하여, 작성자가 임의로 검증을 수행할 수 있습니다." in line:
            last = i
        if "tomok." in line:
            temp_line = line.replace("tomok.", "")
            contents[i] = temp_line

    new_contents = contents[first:last]
    
    with open(f_path, 'w') as fp:
        fp.write(IMPORT_CONTENTS + '\n')
        for line in new_contents:
            fp.write(line)
    

if __name__ == "__main__":
    exporter = PythonExporter()
    
    ipynb_dir = "./raw_files/ipynbs"
    filenames = os.listdir(ipynb_dir)
    for fname in filenames:
        target_dir, target_fname = build_ruleunit_dirs(fname=fname)
        notebook_path = join(ipynb_dir, fname)
        py_path = join(target_dir, target_fname) + '.py'
        with open(notebook_path, 'r', encoding='utf-8') as nf:
            nb_content = nbformat.read(nf, as_version=4)
        
        python_contents, _ = exporter.from_notebook_node(nb_content)
        with open(py_path, 'w', encoding='utf-8') as fp:
            fp.write(python_contents)
        
        with open(py_path, 'r') as fp:
            contents = fp.readlines()            
        ipynb_2_py(py_path, contents)