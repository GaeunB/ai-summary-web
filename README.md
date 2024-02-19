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
