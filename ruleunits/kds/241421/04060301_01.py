import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS241421_04060301_01)
class KDS241421_04060301_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.3.1 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '철근 최대간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.3 슬래브
    4.6.3.1 휨철근
    (1)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    ####  4.6.3.1 휨철근
    \n (1) 일반사항
    ① 주방향에 대한 최소 및 최대철근비는 4.6.2.1(1)과 (3)을 적용한다. 4.6.2.1(1)의 적용에 있어 취성파괴의 위험이 적은 슬래브 경우 최소인장철근은 극한한계상태에 필요한 철근량의 1.2배로 하여도 된다.
    ② 일반적으로 1방향 슬래브의 경우 주철근량의 20% 이상의 배력철근을 배치하여야 한다. 배력 방향 휨모멘트가 발생하지 않는 영역에서는 받침점 부근의 상부 주철근에 대한 배력철근을 배치할 필요가 없다.
    ③ 철근 최대간격에 관한 규정은 다음과 같다.
    가. 주철근 : $3*h \leq 400mm$(h는 슬래브 깊이)
    나. 배력철근 : $3.5*h \leq 450mm$
    ④ 집중하중 또는 최대 휨모멘트가 작용하는 영역에 대해서는 다음 철근간격 규정을 적용한다.
    가. 주철근 : $2*h \leq 250mm$
    나. 배력철근 : $3*h \leq 400mm$
    ⑤ 슬래브에 대하여 4.6.2.2의 규정에서 $a_{l}$을 $d$로 대체하여 해당 규정의 조항을 적용할 수 있다.
    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["철근의 최대간격"];
    B["KDS 24 14 21 4.6.3.1 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:주철근의 최대간격/];
		VarIn2[/입력변수:슬래브 깊이/];
		VarIn3[/입력변수:배력철근의 최대간격/]

		VarIn1 & VarIn2 & VarIn3
		end

		Python_Class ~~~ Variable_def--->E

		E{"철근 최대간격"}
		E--주철근--->D["3h≤400mm"]
		E--배력철근--->F["3.5h≤450mm"]
		D & F ---> K(["Pass or Fail"])

		Variable_def--"집중하중 또는 최대 휨모멘트가 작용하는 영역"-->H
		H{"철근 최대간격"}
		H--주철근--->I["2h≤250mm"]
		H--배력철근--->J["3h≤400mm"]
		I & J ---> L(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_spacing_between_reinforcing_bars(fIh, fIuserdefined) ->float:
        """철근 최대간격
        Args:
             fImaspmr (float): 주철근의 최대간격
             fIh (float): 슬래브 깊이
             fImasprr (float): 배력철근의 최대간격
             fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.3.1 휨철근의 철근 최대간격(1)의 값
        """
        # fIuserdefined = 1
        # 집중하중 또는 최대 휨모멘트가 작용하는 영역: fIuserdefined = 2

        if fIuserdefined == 1:
          fImaspmr = 3*fIh
          fImasprr = 3.5*fIh
          if fImaspmr <= 400 and fImasprr <= 450 :
            return "Pass"
          else:
            return "Fail"
        elif fIuserdefined == 2:
          fImaspmr = 2*fIh
          fImasprr = 3*fIh
          if fImaspmr <= 250 and fImasprr <= 400 :
            return "Pass"
          else:
            return "Fail"


# 

