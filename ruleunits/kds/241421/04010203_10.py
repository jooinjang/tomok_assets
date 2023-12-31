import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS241421_04010203_10)
class KDS241421_04010203_10 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.3 (10)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-09'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '경량콘크리트의 유효강도계수'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (10)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """


    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["경량콘크리트의 유효강도계수"];
    B["KDS 24 14 21 4.1.2.3 (10)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 유효강도계수/];
		VarIn2[/입력변수: 경량콘크리트 계수/];
		VarIn3[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn1 & VarIn2 & VarIn3

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C
		C["<img src='https://quicklatex.com/cache3/f0/ql_30104ad3fb9f832222894dd5289150f0_l3.png'>---------------------------------"]

		C~~~|KDS 24 14 3.1-9|C
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_strength_factor_of_lightweight_concrete(fIetal, fIfck) -> float:
        """경량콘크리트의 유효강도계수

        Args:
             fOnu (float): 콘크리트의 유효강도계수
             fIetal (float): 경량콘크리트 계수
             fIfck (float): 28일 콘크리트 공시체의 기준압축강도



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.3 전단보강철근이 배치된 부재 (10)의 값
        """

        fOnu = 0.5 * fIetal * ( 1- fIfck / 250 )
        return fOnu


# 

