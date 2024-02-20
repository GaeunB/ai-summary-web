# 📋 자소서 요약 페이지
팀원: 변가은, 김지환, 남경현, 이대헌, 이성민, 최민재<br>
[Notion](https://jungle-crane-580.notion.site/27be448bebcb4ca39ac9182033d7a293?pvs=4)
<br>

## 📁 About
프로젝트 계획 이유~

<br>전체 구조 및 작동 방식은 다음과 같다. 


## 🔧 Architecture
Frontend: HTML,CSS,JS
<br>(프론트 캡쳐 화면)
<br>Engine: KorQuAD, textrankr, kobart
<br>(전반적인 도식화)



## Engine
#### ✅ kobart (원리)


#### ✅ textrankr (원리)
TextRank 알고리즘은 2004년 구글에서 발표한 PageRank 알고리즘을 기반으로 한 알고리즘이다[1].<br />
PageRank 알고리즘은 수집된 인터넷 문서 각각을 그래프의 노드, 문서 내부의 링크 정보를 간선으로 가정하여 방향성이 있는 그래프를 만들어 문서의 중요도를 계산한다[2]. 조금 더 쉽게 말하자면 PageRank는 각 웹페이지마다 하이퍼링크가 있을 때 얼마나 링크를 받느냐에 따라 순위를 매기는 알고리즘을 말한다. 즉, 해당 링크를 클릭할 확률로 그 순위를 매기는 것이다.<br />
TextRank 알고리즘은 PageRank의 개념을 자연어 처리에 응용한 것으로 문장, 단어와 같은 특정 단위들 간의 중요도를 계산하는 알고리즘이다. 문서 내의 각 문장을 그래프의 정점(vertex)으로 가정하는 경우 중요한 문장들을 선별할 수 있으며, 이를 통해 문서 요약이 가능하다. 결국, TextRank는 앞서 PageRank에서의 페이지 개념을 단어의 개념으로 바꾼 알고리즘이다. 텍스트로 이루어진 글에서 특정 단어가 다른 문장과 얼마만큼의 관계를 맺고 있는지를 계산한다.<br />
<img width="450" alt="스크린샷 2024-02-20 오전 11 22 32" src="https://github.com/28sungmin/study/assets/115343559/e807a8ef-b229-404d-8be0-3059ce4304cd">
<br /> 위 이미지는 주어진 글에 대해 텍스트 간 관계를 나타낸 그래프로 그린 샘플 이미지이다. 각 문장에서 단어 간의 관계를 선으로 연결한 것이다.<br />
그렇다면 핵심 문장을 추출하기 위해서는 어떻게 해야 할까? 아래의 그림처럼 문장 그래프를 만들어야 한다. 각 문장이 마디가 되는 것이다.
<img width="450" alt="스크린샷 2024-02-20 오전 11 28 52" src="https://github.com/28sungmin/study/assets/115343559/0e6bf9db-ab64-4ece-bac8-1b77cd2a277c">
<br />정석원 외(2017) "TextRank 알고리즘과 주의 집중 순환 신경망을 이용한 하이브리드 문서 요약" 논문에서는 TextRank 알고리즘은 각 문장의 중요도를 구할 때, 문장 간 상관행렬을 이용하여 구하였다.
<img width="400" alt="textrank1" src="https://github.com/28sungmin/study/assets/115343559/b4f130bc-a2ac-40f8-bd2a-cf7a73ddd75c">
<br />입력 문서의 각 문장들에 대해 형태소 분석을 수행하고, 체언류와 용언류의 TF-IDF를 계산하여 문장-단어 행렬을 생성한다. 그 뒤 생성된 문장-단어 행렬의 전치 행렬을 구하여 서로 곱해주면 문장 간의 상관관계(correlation)을 나타내는 행렬을 얻을 수 있다. 이렇게 구한 문장 간 상관행렬은 문장 간의 가중치 그래프로 나타낼 수 있고, TextRank 알고리즘을 통해 각 문장의 중요도를 구할 수 있다. 이렇게 구한 중요도 순으로 문장들을 정렬한 뒤 상위 n개의 문장들을 재배치하면 요약 결과를 얻을 수 있다[3].<br />


참고문헌<br />
[1] 이상영 외(2023), "TextRank 알고리즘 및 인공지능을 활용한 브레인스토밍", JPEE : Journal of practical engineering education = 실천공학교육논문지, v.15 no.2, pp.509 - 517 <br />
[2] 배원식과 차정원(2010), "TextRank 알고리즘을 이용한 문서 범주화", 정보과학회논문지. Journal of KIISE. 컴퓨팅의 실제 및 레터, v.16 no.1, pp.110-114 <br />
[3] 정석원 외(2017), "TextRank 알고리즘과 주의집중 순환 신경망을 이용한 하이브리드 문서 요약", 한국어정보학회 2017년도 제29회 한글및한국어정보처리학술대회, pp.47 - 50 <br />



#### ✅ KorQuAD (원리)



## 주요기능
(간단하게)
- General Summarize:
- Keysentence Extraction: 
- Question Answering: 

 
## 📑 Code Architecture
`app.py`
- app.py 에서는 엔진을 초기 세팅하고, flask 서버 설정을 통해 프론트와 통신을 할 수 있도록 한다. 엔진에서 가장 중점으로 실행되는 코드 파일이며, 백엔드에서 요청이 들어올 경우, 그에 맞는 작업을 수행하여 처리한다.
- 다음 코드는 app이라는 Flask 변수를 생성한다.
<br>
  <details>
**code**
   ```Python
   
   ```
  </details>
<br>

`ext.py`
- 중요문장 추출~
<br>
  <details>
 **code**
   ```Python
   
   ```
  </details>
<br>

`qa_model.py`
- qa모델불러와서 단답형 대답
<br>
  <details>
   **code**
   ```Python

   ```
  </details>
<br>

`gsum.py`
- kobart모델불러와서 포괄적 요약을 진행한다~
<br>**code**
  <details>
   ```Python

   ```
  </details>
