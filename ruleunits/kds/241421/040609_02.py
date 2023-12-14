import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS241421_040609_02)
class KDS241421_040609_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.9 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '철근망의 두 인접한 철근 사이의 간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.9 깊은 보
    (2)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    ####  4.6.9 깊은 보
    (2) 철근망의 두 인접한 철근 사이의 간격은 깊은 보 두께의 2배 또는 300mm 중 작은 값 이하여야 한다.

    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["깊은 보"];
    B["KDS 24 14 21 4.6.9 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:철근 사이의 간격/];
		VarIn2[/입력변수:깊은 보 두께/];


		VarIn1 & VarIn2
		end

		Python_Class ~~~ Variable_def
		Variable_def--->C


		C["철근 사이의 간격≤min(깊은 보 두께x2,300mm)"]

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Spacing_between_rebars(fIspbere,fIdebeth) ->bool:
        """철근망의 두 인접한 철근 사이의 간격
        Args:
             fIspbere (float): 철근 사이의 간격
             fIdebeth (float): 깊은 보 두께


        Returns:
            bool: 철근 사이의 간격이 콘크리트교 설계기준 (한계상태설계법) 4.6.9(2)의 기준을 만족하는지 여부
        """

        if fIspbere <= min( 2*fIdebeth, 300 ):
          return "Pass"
        else:
          return "Fail"


# 

