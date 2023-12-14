import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS241711_04060303_06)
class KDS241711_04060303_06(RuleUnit): # KDS241711_04060303_06

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.3.3 (6)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '축방향철근과 횡방향철근'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.3 축방향철근과 횡방향철근
    (6)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    #### 4.6.3.3 축방향철근과 횡방향철근
    \n (6) 심부구속 횡방향철근과 단부구역의 횡방향철근은 인접부재와의 연결면으로부터 기둥 치수의 0.5배와 380mm 중 큰 값 이상까지 연장해서 설치하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A([축방향철근과 횡방향철근])
	  B["KDS 24 17 11 4.6.3.3(6)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn[/입력변수: 기둥치수/]
	  end
	  Python_Class ~~~ Variable_def---> D
	  D["심부구속 횡방향철근과 단부구역의 횡방향철근 설치 ≥ max(기둥치수 x0.5, 380mm)"]
	  E(["PASS or Fail"])

	  D-->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def additional_length_of_horizontal_rebar(fIadlehore, fIcolsiz) -> bool:
        """횡방향철근의 연장길이

        Args:
            fIadlehr (float): 횡방향철근의 연장길이
            fIcolsiz (float): 기둥치수

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.6.3.3 축방향철근과 횡방향철근 (6)의 통과 여부
        """

        if fIadlehr >= max(0.5 * fIcolsiz, 380):
          return "Pass"
        else:
          return "Fail"


# In[4]:


my_RuleUnit = KDS241711_04060303_06()


# In[5]:


fIadlehr = 600
fIcolsiz = 1000


# In[6]:


Rule_Review_Result = my_RuleUnit.additional_length_of_horizontal_rebar(fIadlehr,fIcolsiz)
print("RuleUnit Review Result: {}".format(Rule_Review_Result))


# <br><br>
# 아래의 코드를 통해, 룰 유닛의 content(건설기준 항목의 실제 내용)의 markdown 렌더링 결과를 확인할 수 있습니다.

# In[7]:


my_RuleUnit.render_markdown()

