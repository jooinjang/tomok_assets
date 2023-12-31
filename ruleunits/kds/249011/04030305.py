import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS249011_04030305)
class KDS249011_04030305 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.3.3.5' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최대압축응력'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.3 적층고무형 지진격리받침
    4.3.3 설계 요구조건
    4.3.3.5 최대압축응력
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    ####  4.3.3.5 최대압축응력
    지진격리받침에 작용하는 최대압축응력은 다음의 조건을 만족해야 한다.
    $$\sigma _{max} = \frac{P_{max}}{A_{e}}$$&#160;&#160;&#160;&#160;&#160;(4.3-18)


    표 4.3-2 최대압축응력

    | 1차 형상계수 $$S_{1}$$| 최대압축응력(MPa) 	|
    |----------------       |----------------       |
    | $$S_{1}< 12$$   	    | 8                 	|
    | $$S\leq S_{1}< 12$$   | $$S_{1}$$        	    |
    | $$12\leq S_{1}$$	    | 12                	|

    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[최대압축응력];
    B["KDS 24 90 11 4.3.3.5"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/입력변수: 최대압축응력/];
		VarIn1[/입력변수: 자가격리받침면적/];
		VarIn2[/입력변수: 최대하중/];
		VarOut1~~~VarIn1 & VarIn2

		end

		Python_Class ~~~ Variable_def;
		Variable_def-->D--->E
		D["<img src='https://latex.codecogs.com/svg.image?\sigma&space;_{max}=\frac{P_{max}}{A_e}'>--------------------------------------------------------"];
		D~~~ |"Table 24 90 11 4.3-2"| D
		E(["최대압축응력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_Compressive_Stress(fIAe, fIPmax) -> bool:
        """최대압축응력

        Args:
            fOsigmamax (float): 최대압축응력
            fIAe (float): 자가격리받침면적
            fIPmax (float): 최대하중

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법) 4.3.3.5 최대압축응력의 값
        """

        fOsigmamax = fIPmax/fIAe
        return fOsigmamax


# 

