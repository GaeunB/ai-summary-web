# 자소서 요약 페이지
팀원: 변가은, 김지환, 남경현, 이대헌, 이성민, 최민재

<br>
# About
대략적 설명

<br>전체 구조 및 작동 방식은 다음과 같다. 


## Architecture
Frontend: Svelte.js
(프론트 캡쳐 화면)
Engine: k-, textrankr, kobart
(전반적인 도식화)

## Model
### kobart 원리


### textrankr 원리 


### qa모델 원리 설명



## 기능_(간단)
Generative Summarize: 간단하게 
<br>Keysentence Extraction: 
<br>Question Answering: 

 
## Code Architecture
app.py
- app.py 에서는 엔진을 초기 세팅하고, flask 서버 설정을 통해 프론트와 통신을 할 수 있도록 한다. 엔진에서 가장 중점으로 실행되는 코드 파일이며, 백엔드에서 요청이 들어올 경우, 그에 맞는 작업을 수행하여 처리한다.
- 다음 코드는 app이라는 Flask 변수를 생성한다.
/code

<br>ext.py
- 중요문장 추출~
- /code
<br>qa_model.py
- qa모델불러와서 단답형 대답
- /code
<br>gsum.py
- kobart모델불러와서 포괄적 요약을 진행한다~
/code

