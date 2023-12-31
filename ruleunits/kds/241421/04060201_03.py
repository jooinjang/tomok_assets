import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS241421_04060201_03)
class KDS241421_04060201_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.1 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '극한한계상태에서 중립축의 깊이'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
    (3)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    ####  4.6.2.1 주철근
    \n (3) 극한한계상태에서 중립축의 깊이가 식 (4.6-3) 으로 결정되는 최대 중립축 깊이 이하가 되도록 인장철근 단면적 또는 긴장재 단면적을 제한하거나 압축철근 단면적을 증가시켜야 한다.
    \n $$ \\c_{max} = \left ( \frac{\delta*\varepsilon_{cu}}{0.0033} - 0.6\right )*d (4.6-3)$$
    여기서, \\c_{max} = 극한한계상태에서의 최대중립축 깊이
    \delta = 모멘트 재분배 후의 $\frac{계수휨모멘트}{탄성휨모멘트}$ 비율,
    모멘트를 재분배하지 않는 경우에는 \delta = 1
    $d$ = 단면의 유효깊이
    \varepsilon_{cu} = 표 3.1-3에 따른 콘크리트의 극한변형률

    """
    # 플로우차트(mermaid)
    flowchart = """
   flowchart TD
    subgraph Python_Class
    A["최대 중립축 깊이"];
    B["KDS 24 14 21 4.6.2.1 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:중립축의 깊이/];
		VarIn2[/입력변수: 모멘트 재분배 후의 계수휨모멘트/탄성휨모멘트 비율/];
		VarIn3[/입력변수: 단면의 유효깊이/];
		VarIn4[/입력변수:콘크리트의 극한변형률/];

		VarOut1[/출력변수: 최대 중립축 깊이/];
		VarOut2[/출력변수: 극한한계상태에서의 최대중립축 깊이/];


		VarOut1 & VarOut2~~~VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

		Python_Class ~~~ Variable_def--->F--->I

		F["<img src='https://latex.codecogs.com/svg.image?C_{max}=(\frac{\delta\varepsilon&space;_{cu}}{0.0033}-0.6)d'>---------------------------------"]

		I(["최대 중립축 깊이"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Depth_of_the_neutral_axis_in_extreme_limits(fIdepnea, fIdelta, fId, fIepsiloncu) ->float:
        """극한한계상태에서 중립축의 깊이
        Args:
             fIdepnea (float): 중립축의 깊이
             fOcmax (float): 극한한계상태에서의 최대중립축 깊이
             fIdelta (float): 모멘트 재분배 후의 계수휨모멘트/탄성휨모멘트 비율
             fId (float): 단면의 유효깊이
             fIepsiloncu (float): 콘크리트의 극한변형률


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.2.1 극한한계상태에서의 중립축의 깊이(3)의 값
        """

        fOcmax = ((fIdelta*fIepsiloncu)/0.0033 - 0.6) * fId
        if fIdepnea <= fOcmax:
          return fOcmax, "Pass"
        else:
          return fOcmax, "Fail"


# 

