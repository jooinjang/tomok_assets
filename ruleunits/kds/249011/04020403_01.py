import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List


# 작성하는 룰에 맞게 클래스 이름 수정 (KDS249011_04020403_01)
class KDS249011_04020403_01(RuleUnit):
    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1  # 건설기준 우선순위
    author = "Seohyun Jin"  # 작성자명
    ref_code = "KDS 24 90 11 4.2.4.3 (1)"  # 건설기준문서
    ref_date = "2021-04-12"  # 디지털 건설문서 작성일
    doc_date = "2023-10-10"  # 건설기준문서->디지털 건설기준 변환 기준일
    title = "회전수용능력"  # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.3 회전수용능력
    (1)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    ####  4.2.4.3 회전수용능력
    (1)
    극한한계상태에서 포트받침에 발생하는 최대 회전각($$\alpha _{dmax}$$)은 0.03 rad을 초과할 수 없으며, 활하중에 의한 회전각 변동(\Delta \alpha _{d2})은 0.005rad을 초과하지 못한다.
    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[회전한계];
    B["KDS 24 90 11 4.2.4.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 포트받침에 발생하는 최대 회전각/];
		VarIn2[/입력변수: 활하중에 의한 회전각 변동/];

		VarIn1 & VarIn2
		end

		Python_Class ~~~ Variable_def;
		Variable_def--> C & D--->E

		C["포트받침에 발생하는 최대 회전각≤0.03rad"]
		D["활하중에 의한 회전각 변동≤0.005rad"]

		E(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_Rotation_Angle_For_Potholders(fIalphadmax,  fIdeltaalphad2) -> bool:
        """회전수용능력
        Args:
            fIalphadmax (float): 포트받침에 발생하는 최대 회전각
            fIdeltaalphad2 (float): 활하중에 의한 회전각 변동

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)   4.2.4.3 회전수용능력 (1)의 통과 여부
        """

        if fIalphadmax <= 0.03 and fIdeltaalphad2 <= 0.005:
            return "Pass"

        else:
            return "Fail"


#
