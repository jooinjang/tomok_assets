
    import sys
    import os

    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)

    from tomok.core.rule_unit import RuleUnit
    from tomok.core.decorator import rule_method

    import math
    from typing import List
    
