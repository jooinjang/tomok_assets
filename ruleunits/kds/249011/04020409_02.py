import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS249011_04020409_02)
class KDS249011_04020409_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.4.9 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '피스톤과 포트 접촉부 검토'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.9 피스톤과 포트 접촉부 검토
    (2)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    ####  4.2.4.9 피스톤과 포트 접촉부 검토
    (2) 접촉면은 극한한계상태에서 아래 조건을 만족하도록 설계한다. $$V_{Sd}$$ 는 수평력(N), $$V_{Rd}$$ 는 포트의 설계강도(N)로 접촉면에 따라 구분된다.
    $$V_{Sd}\leq V_{Sd}$$&#160;&#160;&#160;&#160;&#160;(4.2-27)

    ① 평면 접촉면
	  $$V_{Rd} = \frac{f_{y}\times D\times w}{1.95}$$&#160;&#160;&#160;&#160;&#160;(4.2-28)

    여기서, D = 포트의 내부 직경(mm)
		$$f_{y}$$ = 재료의 항복 강도(MPa)
	  w = 피스톤 면의 폭(mm)

    ② 곡면 접촉면
    $$V_{Rd} = \frac{8.8\times f^{2}_{y}\times R\times D}{1.95}$$&#160;&#160;&#160;&#160;&#160;(4.2-29)

    여기서, R = 접촉면의 반경(mm)
		$$f_{y}$$ = 재료의 항복 강도(MPa)
		$$E_{d}$$ = 포트의 탄성계수(MPa)
		D = 그림 4.2.5 참고(mm)

    <img src='http://drive.google.com/uc?export=view&id=1KdCE4dXqayww4wNaWi-jLSYqBi1fNic0'>
    ![건설기준문서](http://drive.google.com/uc?export=view&id=1KdCE4dXqayww4wNaWi-jLSYqBi1fNic0)


    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[피스톤과 포트 접촉부 검토];
    B["KDS 24 90 11 4.2.4.9 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 포트의 내부 직경/];
		VarIn2[/입력변수: 재료의 항복 강도/];
		VarIn3[/입력변수: 피스톤 면의 폭/];
		VarIn4[/입력변수: 접촉면의 반경/];
		VarIn5[/입력변수: 재료의 항복 강도/];
		VarIn6[/입력변수: 포트의 탄성계수/];
		VarIn7[/입력변수: 포트의 내부 직경/];
		VarIn8[/입력변수: 수평력/];
		VarIn9[/입력변수: 포트의 설계강도/];
		VarIn10[/입력변수: 포트의 설계강도/];
		VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
    VarIn4 ~~~ VarIn5 & VarIn6 & VarIn7
		VarIn5 ~~~ VarIn8 & VarIn9 & VarIn10


		end

		Python_Class ~~~ Variable_def;
		Variable_def--->K
		Variable_def--->L

		K["<img src='https://latex.codecogs.com/svg.image?&space;V_{Rd}=\frac{f_{y}Dw}{1.95}'>--------------------------------------------------------"];
		L["<img src='https://latex.codecogs.com/svg.image?&space;V_{Rd}=\frac{8.8f_{y}^{2}RD}{E_{d}}'>--------------------------------------------------------"];
		K & L--->M--->N
		M["<img src='https://latex.codecogs.com/svg.image?V_{Sd}\leq V_{Rd}'>---------------"]
    N(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_Strength_Of_Pot( fIVSd,  fIwidsop,  fIR,  fIfy,  fIEd,  fID) -> bool:
        """피스톤과 포트 접촉부 검토

        Args:
            fIVRd (float): 포트의 설계강도
            fIVSd (float): 수평력
            fIwidsop (float): 피스톤 면의 폭
            fIR (float): 접촉면의 반경
            fIfy (float): 재료의 항복 강도
            fIEd (float): 포트의 탄성계수
            fID (float): 포트의 내부 직경
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.4.9 피스톤과 포트 접촉부 검토 (2)의 값
        """

        #평면 접촉면 > fIuserdefined == 1
        #곡면 접촉면 > fIuserdefined == 2

        if fIuserdefined == 1:
          fIVRd = fIfy*fID*fIwidsop/1.95
          if fIVSd <= fIVRd :
            return "Pass"
          else:
            return "Fail"

        if fIuserdefined == 2:
          fIVRd = 8.8*fIfy*fIfy*fIR*fID/fIEd
          if fIVSd <= fIVRd :
            return "Pass"
          else:
            return "Fail"




# 

