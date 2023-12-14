import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS241421_04060503_02)
class KDS241421_04060503_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.5.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '바닥판 지간 중앙부의 배력철근'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.5 교량의 콘크리트 바닥슬래브
    4.6.5.3 전통적 설계법
    (2)
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
    A["배력철근"];
    B["KDS 24 14 21 4.6.5.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:바닥판의 지간/];
		VarIn2[/입력변수:배력철근량/];
		VarIn3[/입력변수:온도 및 건조수축에 소요되는 철근량/];

		VarIn1 & VarIn2 & VarIn3


		end

		Python_Class ~~~ Variable_def--->F
		F{"주철근의 방향"}
		F--열차진행 방향에 직각--->E
		F--열차진행 방향에 평행--->G
		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\frac{120}{\sqrt{L}}\leq&space;67%'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?\inline&space;\frac{55}{\sqrt{L}}\leq&space;50%'>---------------------------------"]
		H["배치할 배력철근량≥온도 및 건조수축에 소요되는 철근량"]

		Variable_def--->H

		E ---> I(["Pass or Fail"])
		G ---> J(["Pass or Fail"])
		H ---> K(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Thrust_reinforcement_at_the_center_of_the_floor_section(fIL,fIamorei,fIamrbts,fIuserdefined) ->float:
        """바닥판 지간 중앙부의 배력철근
        Args:
             fIL (float): 바닥판의 지간
             fIamorei (float): 배력철근량
             fIamrbts (float): 온도 및 건조수축에 소요되는 철근량
             fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.5.3 바닥판 하부와 지간 중앙부의 배력철근 (2)의 통과 여부
        """
        #주철근이 차량 및 열차진행 방향에 직각인 경우: fIuserdefined = 1
        #주철근이 차량 및 열차 진행 방향에 평행한 경우: fIuserdefined = 2

        if fIuserdefined == 1:
          if 120 / ((fIL/1000)**0.5) <= 67 and fIamorei >= fIamrbts :
            return "Pass"
          else:
            return "Fail"
        elif fIuserdefined == 2:
          if 55 / ((fIL/1000)**0.5) <= 50 and fIamorei >= fIamrbts :
            return "Pass"
          else:
            return "Fail"



# 

