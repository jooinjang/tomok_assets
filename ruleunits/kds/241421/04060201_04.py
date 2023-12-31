import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS241421_04060201_04)
class KDS241421_04060201_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.1 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '철근 단면적'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
    (4)
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
    A["주철근"];
    B["KDS 24 14 21 4.6.2.1 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:인장철근 단면적/];
		VarIn2[/입력변수: 콘크리트 단면적/];
		VarIn3[/입력변수: 압축철근 단면적/];
		VarIn4[/입력변수:콘크리트 단면적/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

		Python_Class ~~~ Variable_def--->F & G

		F["인장철근 단면적<콘크리트 단면적X0.04"]
		G["압축철근 단면적<콘크리트 단면적X0.04"]
		F & G---->J
		J(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    Function definition not found.
    def Cross_sectional_area_of_rebar (fIcrosat,fIconcse,fIcompba) ->float:
        """철근 단면적
        Args:
             fIcrosat (float): 인장철근 단면적
             fIconcse (float): 콘크리트 단면적
             fIcompba (float): 압축철근 단면적

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.2.1 주철근 (4)의 값
        """

        if fIcrosat <= fIconcse * 0.04 and fIcompba <= fIconcse * 0.04 :
          return "Pass"
        else:
          return "Fail"


# 

