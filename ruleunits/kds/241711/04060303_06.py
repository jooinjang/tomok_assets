
    import sys
    import os

    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)

    from tomok.core.rule_unit import RuleUnit
    from tomok.core.decorator import rule_method

    import math
    from typing import List
    
{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[{"file_id":"1CF4mEkZIkJEDv_3YWrDJKpMvliJCsObv","timestamp":1694582086331},{"file_id":"1AjfPs7fZq571GayM7OCK45oG46DxPiKP","timestamp":1694578487763},{"file_id":"1RLG-ElL-RB0QZTLLAzUcuXGBF2BqOw1t","timestamp":1691543517336},{"file_id":"1T-kPFUJTy0JUtisu6LLIsNK6yjl9AE5z","timestamp":1690960458929},{"file_id":"1FKcEkmC8sjFendaUJI5nY9FQVPYBFWnt","timestamp":1689903322566},{"file_id":"1p6jLaorqf3Zl1Og2wHOctERtkgjwBjrU","timestamp":1689753625918},{"file_id":"15jZPegTcUqCXxee33FxMzfCjeMAwcNRA","timestamp":1688037542443}]},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["# Rule Unit 작성 예시\n","\n","본 문서는 1차년도 6월에 개발된 RuleUnit 클래스를 활용하여 룰 유닛을 작성하고 실행하는 과정을 설명합니다."],"metadata":{"id":"-0-qnEblh80w"}},{"cell_type":"markdown","source":["⚠︎ 주의사항: 코드를 변경하며 작업할 때는, 사본을 생성한 후 작업해주십시오."],"metadata":{"id":"AR83L9Pxh_6F"}},{"cell_type":"markdown","source":["## 룰 유닛 작성하기\n","이 부분에서는 기존의 IFC 파일에 종속적이었던 실행 흐름에서 벗어나, 새로이 정의한 RuleUnit 구조에 기반하여 룰에 포함된 항목을 작성하는 방법을 다룹니다.<br><br>\n","본 예시에서는 KDS 24 14 21 4.6.5.1(5) 를 룰 유닛으로 작성합니다."],"metadata":{"id":"33RPd0N_iCuY"}},{"cell_type":"markdown","source":["먼저, Rule 작성에 필요한 프로그램을 불러오기 위해 Github에서 아래의 주소가 가리키는 파일 모음을 불러옵니다. (Github Repository를 clone합니다.)"],"metadata":{"id":"qL08gaStiE0L"}},{"cell_type":"code","source":["!git clone https://github.com/KU-HIAI/.git"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"5AR_68PDk-KZ","executionInfo":{"status":"ok","timestamp":1700295256655,"user_tz":-540,"elapsed":1489,"user":{"displayName":"digitalcodes KICT","userId":"11324252449574396480"}},"outputId":"e92be149-dada-4b3e-978a-c817c88e4e7a"},"execution_count":1,"outputs":[{"output_type":"stream","name":"stdout","text":["Cloning into ''...\n","remote: Enumerating objects: 175, done.\u001b[K\n","remote: Counting objects: 100% (117/117), done.\u001b[K\n","remote: Compressing objects: 100% (86/86), done.\u001b[K\n","remote: Total 175 (delta 54), reused 85 (delta 31), pack-reused 58\u001b[K\n","Receiving objects: 100% (175/175), 451.83 KiB | 2.24 MiB/s, done.\n","Resolving deltas: 100% (62/62), done.\n"]}]},{"cell_type":"markdown","source":["필요한 파일을 불러온 다음에는 현재 작업 경로를 의 파일이 있는 위치로 이동합니다.<br><br>\n","아래의 코드 블록을 실행하면, 작성자의 기본 작업 경로가 필요한 파일이 있는 위치로 이동됩니다."],"metadata":{"id":"poob594xiNFU"}},{"cell_type":"code","source":["cd "],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"qyIxAqkriO26","executionInfo":{"status":"ok","timestamp":1700295256655,"user_tz":-540,"elapsed":15,"user":{"displayName":"digitalcodes KICT","userId":"11324252449574396480"}},"outputId":"d026b8c0-eed5-4800-a2cc-ae870e4d3fe7"},"execution_count":2,"outputs":[{"output_type":"stream","name":"stdout","text":["/content/\n"]}]},{"cell_type":"markdown","source":["RuleUnit의 실행 함수는 기존의 OKNGResult 클래스를 활용하지 않고, 해당 실행함수의 기준을 만족하였는지의 여부를 bool 타입의 값(참/거짓)으로 반환합니다."],"metadata":{"id":"vsLFVLLCidR7"}},{"cell_type":"markdown","source":["## 룰 유닛 작성해보기\n","지금까지의 내용을 바탕으로 룰 유닛을 작성해봅시다.\n","\n","새로운 룰 유닛을 작성하기 위해서는, 아래 코드 블럭에서 클래스 이름, 메타정보에 해당하는 변수, 실행 함수의 이름과 내용을 수정하면 됩니다."],"metadata":{"id":"8lGDCXNZiej5"}},{"cell_type":"code","source":["import math\n","from typing import List\n","\n","import \n","\n","# 작성하는 룰에 맞게 클래스 이름 수정 (KDS241711_04060303_06)\n","class KDS241711_04060303_06(.RuleUnit): # KDS241711_04060303_06\n","\n","    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정\n","    priority = 1   # 건설기준 우선순위\n","    author = 'Chanwoo Yang'  # 작성자명\n","    ref_code = 'KDS 24 17 11 4.6.3.3 (6)' # 건설기준문서\n","    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)\n","    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)\n","    title = '축방향철근과 횡방향철근'   # 건설기준명\n","\n","    # 건설기준문서항목 (분류체계정보)\n","    description = \"\"\"\n","    교량내진설계기준(한계상태설계법)\n","    4. 설계\n","    4.6 콘크리트교 설계\n","    4.6.3 기둥\n","    4.6.3.3 축방향철근과 횡방향철근\n","    (6)\n","    \"\"\"\n","    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트\n","    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html\n","    # 건설기준문서내용(text)\n","    content = \"\"\"\n","    #### 4.6.3.3 축방향철근과 횡방향철근\n","    \\n (6) 심부구속 횡방향철근과 단부구역의 횡방향철근은 인접부재와의 연결면으로부터 기둥 치수의 0.5배와 380mm 중 큰 값 이상까지 연장해서 설치하여야 한다.\n","    \"\"\"\n","\n","    # 플로우차트(mermaid)\n","    flowchart = \"\"\"\n","    flowchart TD\n","\t  subgraph Python_Class\n","\t  A([축방향철근과 횡방향철근])\n","\t  B[\"KDS 24 17 11 4.6.3.3(6)\"]\n","\t  A ~~~ B\n","\t  end\n","\n","\t  subgraph Variable_def\n","\t  VarIn[/입력변수: 기둥치수/]\n","\t  end\n","\t  Python_Class ~~~ Variable_def---> D\n","\t  D[\"심부구속 횡방향철근과 단부구역의 횡방향철근 설치 ≥ max(기둥치수 x0.5, 380mm)\"]\n","\t  E([\"PASS or Fail\"])\n","\n","\t  D-->E\n","    \"\"\"\n","\n","    # 작성하는 룰에 맞게 함수 이름과 내용을 수정\n","    @.rule_method\n","    def additional_length_of_horizontal_rebar(fIadlehore,fIcolsiz) -> bool:\n","        \"\"\"횡방향철근의 연장길이\n","\n","        Args:\n","            fIadlehr (float): 횡방향철근의 연장길이\n","            fIcolsiz (float): 기둥치수\n","\n","        Returns:\n","            bool: 교량내진설계기준(한계상태설계법) 4.6.3.3 축방향철근과 횡방향철근 (6)의 통과 여부\n","        \"\"\"\n","\n","        if fIadlehr >= max(0.5 * fIcolsiz, 380):\n","          return \"Pass\"\n","        else:\n","          return \"Fail\""],"metadata":{"id":"rfDi2pQqicoD","executionInfo":{"status":"ok","timestamp":1700295256655,"user_tz":-540,"elapsed":13,"user":{"displayName":"digitalcodes KICT","userId":"11324252449574396480"}}},"execution_count":3,"outputs":[]},{"cell_type":"code","source":["my_RuleUnit = KDS241711_04060303_06()"],"metadata":{"id":"D1Pm_gEtikei","executionInfo":{"status":"ok","timestamp":1700295256655,"user_tz":-540,"elapsed":13,"user":{"displayName":"digitalcodes KICT","userId":"11324252449574396480"}}},"execution_count":4,"outputs":[]},{"cell_type":"code","source":["fIadlehr = 600\n","fIcolsiz = 1000"],"metadata":{"id":"HVyDu2z7imJC","executionInfo":{"status":"ok","timestamp":1700295256656,"user_tz":-540,"elapsed":14,"user":{"displayName":"digitalcodes KICT","userId":"11324252449574396480"}}},"execution_count":5,"outputs":[]},{"cell_type":"code","source":["Rule_Review_Result = my_RuleUnit.additional_length_of_horizontal_rebar(fIadlehr,fIcolsiz)\n","print(\"RuleUnit Review Result: {}\".format(Rule_Review_Result))"],"metadata":{"id":"UDa_8Sh_iraQ","executionInfo":{"status":"ok","timestamp":1700295256656,"user_tz":-540,"elapsed":13,"user":{"displayName":"digitalcodes KICT","userId":"11324252449574396480"}},"colab":{"base_uri":"https://localhost:8080/"},"outputId":"472f132c-938f-412a-85a3-dbf67fc14543"},"execution_count":6,"outputs":[{"output_type":"stream","name":"stdout","text":["RuleUnit Review Result: Pass\n"]}]},{"cell_type":"markdown","source":["<br><br>\n","아래의 코드를 통해, 룰 유닛의 content(건설기준 항목의 실제 내용)의 markdown 렌더링 결과를 확인할 수 있습니다."],"metadata":{"id":"7TnAwYSbiqpE"}},{"cell_type":"code","source":["my_RuleUnit.render_markdown()"],"metadata":{"id":"3BSi3TyUiu6H","executionInfo":{"status":"ok","timestamp":1700295256656,"user_tz":-540,"elapsed":12,"user":{"displayName":"digitalcodes KICT","userId":"11324252449574396480"}},"colab":{"base_uri":"https://localhost:8080/","height":81},"outputId":"546e4eb2-dce0-456d-acc6-e3e4fef80c09"},"execution_count":7,"outputs":[{"output_type":"display_data","data":{"text/plain":["<IPython.core.display.Markdown object>"],"text/markdown":"\n    #### 4.6.3.3 축방향철근과 횡방향철근\n    \n (6) 심부구속 횡방향철근과 단부구역의 횡방향철근은 인접부재와의 연결면으로부터 기둥 치수의 0.5배와 380mm 중 큰 값 이상까지 연장해서 설치하여야 한다.\n    "},"metadata":{}}]}]}
