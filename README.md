# 👋안녕하세요, '자소서 요약단'입니다.
**팀원**: 변가은, 김지환, 남경현, 이대헌, 이성민, 최민재<br />
**팀노션페이지**: [Notion](https://jungle-crane-580.notion.site/27be448bebcb4ca39ac9182033d7a293?pvs=4)
<br />
<img src="https://github.com/GaeunB/read_/assets/115343409/8b8a19aa-bae9-473b-9875-37f65656e2c4" height="1200"/>


## 🔎 Table of Contents
+ About
+ Main Fuctions
+ Architecture
+ Setting
+ Engine
  + General_Summarization
  + Keysentence_Extraction
  + Question_Answering
+ Code_Architecture

## 📁 About
💡**주제**: 인공지능 활용 자기소개서 요약 페이지 <br />
`#NLP` `#Text_Summarization` `#Question_Answering` `#Flask` <br />
<aside>

- **개요**  <br />
	<img src="https://github.com/GaeunB/read_/assets/115343409/a0306374-660e-4f03-bb69-e2daa384bb56">

    - 매 채용시 지원자는 동일한 질문을 제한된 글자 수 내에서 답변을 하고 있다.
    - 신입사원 채용은 이력서보다 자기소개서를 중요하게 평가
        - 경력이 없는 신입사원의 업무 수행능력은 비슷하기 때문에 지원자의 잠재력을 파악하기 위한 도구로 자기소개서가 큰 비중을 차지한다.

	 ⇒‘**자소서 요약단**’은 기업 임원진을 대상으로 자기소개서의 내용을 요약하여 효과적으로 사용자에게 전달하고, 상호작용할 수 있는 인공지능 기반의 자기소개 요약 페이지를 제공한다.

</aside>
<br />

- **랜딩 페이지**

![랜딩페이지@3x height='200'](https://github.com/GaeunB/read_/assets/115343409/b701310c-9fda-4647-8f42-b9bd59d7c0c5)

- **시연 영상**
<br />
<br />

## 🚦 Main Fuctions
- **General Summarization**: 자연어 처리 모델을 활용한 자기소개서 요약
- **Keysentence Extraction**: 키워드 중심의 문장 추출
- **Question Answering**: 질문에 대한 답변 제공 

## 🔧 Architecture
+ **Frontend**: HTML, CSS, JS <br />
+ **Engine** : Pytorch <br /> 
	+ Kobart, Textrankr, Bert 
+ **Backend**: Flask <br />

<br />전체 구조 및 작동 방식은 다음과 같다. 
<br /> (다이어그램)
## 💾 Setting
- **Install modules**
```bash
pip install -r requirements.txt 
``` 
- **Execute**
```bash
flask run
```

## ⚡ Engine
#### ✅ General Summarization_kobart
https://github.com/SKT-AI/KoBART <br /> 
- BART(Bidirectional and Auto-Regressive Transformers)는 입력 텍스트 일부에 노이즈를 추가하여 이를 다시 원문으로 복구하는 autoencoder의 형태로 학습이 됩니다.<br /> 
![image width=650 height=550](https://github.com/Oneourbefore/ai-summary-web/assets/102707496/68021f7e-9981-4a97-9ae3-b3e6ff830132)
1. Bart는 Transformer의 기본 아키텍처인 Encoder-Decoder구조를 갖고 있다.
2. 따라서 코드도 Encoder와 Decoder를 차례로 통과한다.
3. Input data도 Encoder_input과 Decoder_input을 따로 준비해야한다.
4. 어떻게 input을 넣어주냐에 따라 Task마다 학습/추론 방법이 갈린다.

- 한국어 BART는 논문에서 사용된 Text Infilling 노이즈 함수를 사용하여 40GB 이상의 한국어 텍스트에 대해서 학습한 한국어 encoder-decoder 언어 모델입니다. <br /> 
이를 통해 도출된 KoBART-base를 배포합니다. 
한국어 위키 백과 이외, 뉴스, 책, 모두의 말뭉치 v1.0(대화, 뉴스, ...), 청와대 국민청원 등의 다양한 데이터가 모델 학습에 사용되었습니다.

- KoBART란 페이스북에서 공개한 BART모델을 SKT에서 40GB이상의 한국어 텍스트로 사전 학습시킨 모델이다.<br /> 
BART는 seq2seq 모델을 사전학습하기 위한 denoising autoencoder(DAE, 잡음제거 오토 인코더)로, 임의의 noising function으로 텍스트를 손상시킨 후 모델이 원본 텍스트를 재구축하는 방식으로 학습이 진행된다.<br /> 
BART는 기존 BERT모델과 GPT를 합친 구조를 가지고 있는데, 이로 인해 BERT의 Bidirectional 특징과 GPT의 Auto-Regressive한 특징을 모두 가진다. 덕분에 BART는 기존 MLM모델들에 비해 다양한 분야에서 높은 활용성을 나타낸다. 
![image width=650 height=550](https://github.com/GaeunB/ai-summary-web/assets/118701576/f2e5c8e6-cedc-4ccf-b9f2-90f6ccc25501 ) <br /> 
**Fig.1 Bart구조**<br /> 
- BART는 손상된 Text를 입력으로 받아 Bidirectional 모델로 encoding하고 정답 Text에 대한 likelihood를 autoregressive 모델로 decoding하여 계산한다. 
BART에서는 다음과 같은 5가지 noising 기법이 존재한며, 이를 통해 손상된 Text를 얻는다.
![image width=650 height=550](https://github.com/GaeunB/ai-summary-web/assets/118701576/d4db2cc4-2686-40e3-b4dd-38312d0c3ff1) <br /> 
**Fig.2 Noising기법**<br /> 
- BART는 자기회귀 디코더를 갖기 때문에, abstractive QA와 summarization과 같은 시퀀스 일반화(Sequence Generation) 태스크에 직접적으로 파인튜닝 될 수 있다. 이번 프로젝트에서는 이력서 요약 기능을 수행하기 위해 KoBART모델에 채용면접 데이터로 파인튜닝을 진행하였다.(데이터셋: https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=realm&dataSetSn=71592) 
<br />

<details><summary>참고문헌</summary>
[1] Mike Lewis외(2019), "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension", ACL <br /> 
[2] 수다르산 라비찬디란(2021), "구글 BERT의 정석", 한빛미디어
</details>


#### ✅ Keysentence Extraction_Textrankr
- TextRank 알고리즘은 2004년 구글에서 발표한 PageRank 알고리즘을 기반으로 한 알고리즘이다[1].<br />
PageRank 알고리즘은 수집된 인터넷 문서 각각을 그래프의 노드, 문서 내부의 링크 정보를 간선으로 가정하여 방향성이 있는 그래프를 만들어 문서의 중요도를 계산한다[2]. 조금 더 쉽게 말하자면 PageRank는 각 웹페이지마다 하이퍼링크가 있을 때 얼마나 링크를 받느냐에 따라 순위를 매기는 알고리즘을 말한다. 즉, 해당 링크를 클릭할 확률로 그 순위를 매기는 것이다.<br />
- TextRank 알고리즘은 PageRank의 개념을 자연어 처리에 응용한 것으로 문장, 단어와 같은 특정 단위들 간의 중요도를 계산하는 알고리즘이다. 문서 내의 각 문장을 그래프의 정점(vertex)으로 가정하는 경우 중요한 문장들을 선별할 수 있으며, 이를 통해 문서 요약이 가능하다. 결국, TextRank는 앞서 PageRank에서의 페이지 개념을 단어의 개념으로 바꾼 알고리즘이다. 텍스트로 이루어진 글에서 특정 단어가 다른 문장과 얼마만큼의 관계를 맺고 있는지를 계산한다.<br />
<img width="450" alt="스크린샷 2024-02-20 오전 11 22 32" src="https://github.com/28sungmin/study/assets/115343559/e807a8ef-b229-404d-8be0-3059ce4304cd">
<br />

- 위 이미지는 주어진 글에 대해 텍스트 간 관계를 나타낸 그래프로 그린 샘플 이미지이다. 각 문장에서 단어 간의 관계를 선으로 연결한 것이다.<br />
그렇다면 핵심 문장을 추출하기 위해서는 어떻게 해야 할까? 아래의 그림처럼 문장 그래프를 만들어야 한다. 각 문장이 마디가 되는 것이다.
<img width="450" alt="스크린샷 2024-02-20 오전 11 28 52" src="https://github.com/28sungmin/study/assets/115343559/0e6bf9db-ab64-4ece-bac8-1b77cd2a277c">
<br />정석원 외(2017) "TextRank 알고리즘과 주의 집중 순환 신경망을 이용한 하이브리드 문서 요약" 논문에서는 TextRank 알고리즘은 각 문장의 중요도를 구할 때, 문장 간 상관행렬을 이용하여 구하였다.
<img width="400" alt="textrank1" src="https://github.com/28sungmin/study/assets/115343559/b4f130bc-a2ac-40f8-bd2a-cf7a73ddd75c"><br />

- 입력 문서의 각 문장들에 대해 형태소 분석을 수행하고, 체언류와 용언류의 TF-IDF를 계산하여 문장-단어 행렬을 생성한다. 그 뒤 생성된 문장-단어 행렬의 전치 행렬을 구하여 서로 곱해주면 문장 간의 상관관계(correlation)을 나타내는 행렬을 얻을 수 있다. 이렇게 구한 문장 간 상관행렬은 문장 간의 가중치 그래프로 나타낼 수 있고, TextRank 알고리즘을 통해 각 문장의 중요도를 구할 수 있다. 이렇게 구한 중요도 순으로 문장들을 정렬한 뒤 상위 n개의 문장들을 재배치하면 요약 결과를 얻을 수 있다[3].<br />

<br />
<details><summary>참고문헌</summary>
[1] 이상영 외(2023), "TextRank 알고리즘 및 인공지능을 활용한 브레인스토밍", JPEE : Journal of practical engineering education = 실천공학교육논문지, v.15 no.2, pp.509 - 517 <br />
[2] 배원식과 차정원(2010), "TextRank 알고리즘을 이용한 문서 범주화", 정보과학회논문지. Journal of KIISE. 컴퓨팅의 실제 및 레터, v.16 no.1, pp.110-114 <br />
[3] 정석원 외(2017), "TextRank 알고리즘과 주의집중 순환 신경망을 이용한 하이브리드 문서 요약", 한국어정보학회 2017년도 제29회 한글및한국어정보처리학술대회, pp.47 - 50 <br />
</details>


#### ✅ Question Answering_Bert (원리)
-Question Answering model은 사용자로부터 받은 특정한 질의에 관련된 정답을 자연어로 자동으로 출력하는 시스템이다. [1] 

QA 작업은 주어진 질문과 문맥을 이해하여 답변을 제시하는 것이 목표인데, 답변을 찾는 방식에 따라 추출형(extractive), 추상형(abstractive) 으로 나뉜다. 문장 내에서 질문에 해당하는 답변을 찾아내는지 / 주어진 질문에 대한 답변을 직접 생성하는 방식의 차이이다. QA 작업을 진행하기 위해, 구글에서 개발한 NLP 처리 모델인 BERT 모델을 활용하였다. 

BERT 모델은 사전 훈련 언어 모델로서, 특정 분야에 국한된 기술이 아니라 모든 자연어 처리 분야에서 좋은 성능을 내는 범용 Language Model이다. Transformer architerture에서 encoder만 사용한다는 특징이 있다.구조는 다음과 같다.

##### 1. Input 

![image](https://github.com/GaeunB/ai-summary-web/assets/145184645/fdf376d2-bda1-43b5-8341-f290b3a490c9){: width="100" height="100"}

Input은 Token Embedding + Segment Embedding + Position Embedding 3가지 임베딩을 결합한 방식으로 진행한다.
-Token Embedding : Word Piece 임베딩 방식을 사용한다. Char 단위로 임베딩 후 등장 빈도에 따라 sub-word 로 구분한다.
-Segment Embedding : Sentence Embedding으로, 토큰 시킨 단어들을 다시 하나의 문장으로 만드는 작업이다. 구분자 [SEP] 를 통해 문장을 구분하고 두 문장을 하나의 Segment 로 지정한다. 
-Position Embedding : 입력 토큰의 위치 정보를 고려하지 않고, 토큰 순서대로 인코딩한다. 

##### 2. Pre-Training

!<img src="https://github.com/GaeunB/ai-summary-web/assets/145184645/56f14403-b877-4de7-b0a3-5278a01910b0" width="50%" height="50%">

-MLM(masked Language Model) : 입력 문장에서 임의로 토큰을 버리고(Mask) 그 토큰을 맞추는 방식으로 학습을 진행한다. 

-NSP(Next Sentence Prediction) : 두 문장이 주어졌을 때, 두 문장의 순서를 예측하는 방식이다. 두 문장 간 관련이 고려되야 하는 NLI와 QA의 파인 튜닝을 위해 두 문장의 연관을 맞추는 학습을 진행한다.

#### 3. Fine-tuning

![image](https://github.com/GaeunB/ai-summary-web/assets/145184645/100973f4-d8ea-4ac3-bc8e-b014a0a45e56){: width="100" height="100"}

Bert는 fine-tuning 단계에서 pre-training 과 거의 동일한 하이퍼파라미터를 사용한다. 각 NLP task마다 fine-tuning 후 Bert 모델을 transfer learning시켜 성능을 확인한다.

BERT 기반 QA 모델은 크게 두 가지 접근 방식을 사용한다. 
1. 질문과 문맥을 함께 입력으로 받아 답변을 예측하는 방식
2. 질문과 문맥을 각각 따로 입력으로 받아 각각에 대한 임베딩을 생성하고, 이를 다양한 방식으로 결합하여 답변을 예측하는 방식 
본 프로젝트에서는 question과 reference를 동시에 input 으로 사용하여 extractive question answering 모델을 구성하였다.
![image](https://github.com/GaeunB/ai-summary-web/assets/145184645/4f0335a4-1310-46ac-a5be-55c3609d5b05)

<details><summary>참고문헌</summary>
[1] 권세린, et al. "의료 관련 질의응답을 위한 BERT 기반 한국어 QA 모델." Proceedings of KIIT Conference. 2022. <br />
[2] Devlin, Jacob, et al. "Bert: Pre-training of deep bidirectional transformers for language understanding." arXiv preprint arXiv:1810.04805 (2018). <br />
[3] 송다연, 조상현, and 권혁철. "한국어 문법 QA 시스템을 위한 BERT 기반 시퀀스 분류모델." 한국정보과학회 학술발표논문집 (2021): 754-756. <br />
</details>

## 📑 Code Architecture
**✔️ `app.py`** <br />
- `app.py` 에서는 엔진을 초기 세팅하고, flask 서버 설정을 통해 프론트와 통신을 할 수 있도록 한다. 엔진에서 가장 중점으로 실행되는 코드 파일이며, 백엔드에서 요청이 들어올 경우, 그에 맞는 작업을 수행하여 처리한다.
- flask_cors를 활용하여 CORS 이슈를 해결한다.<br />

```Python
from flask import Flask,render_template,request, jsonify
from flask_cors import CORS
import torch
from sum_model import summarize_model
from ext import textrank_summarize
from qa_model import get_qa_model
	
app = Flask(__name__)
cors = CORS(app)
```

- flask 앱을 생성하고 다음 경로에 대한 라우팅을 설정한다.
	- `'/'`: 홈 페이지를 렌더링
	- `'/sum'`: 요약 페이지를 렌더링
	- `'/sum/gsummarize'`: 일반적인 요약을 수행
	- `'/sum/key'`: 키워드 중심의 문장 추출을 수행
	- `'/sum/qa'`: 질문에 대한 답변을 제공

```Python
#home
@app.route('/')	
def home():
	return render_template('home.html')
	
#summary page
@app.route('/sum')	
def index():
	return render_template('index.html')
	
#general summarization
@app.route('/sum/gsummarize', methods=['POST'])
def gsummarize():
	try:
		data = request.get_json(force=True)
		context = data['context']
		gsum = summarize_model(context)
		response = jsonify({'gsum': gsum})
	
		except Exception as e:
			response = jsonify({'error': str(e)})	
		return response
	
	
# keysentence extraction
@app.route('/sum/key',methods=['POST'])
def key():
	try:
		data = request.get_json(force=True)
		context = data['context']
		keytext = textrank_summarize(context,1) #문장 수 조절 필요
		response = jsonify({'keytext': keytext})
	
		except Exception as e:
			response = jsonify({'error': str(e)})	
			
		return response
		
#qa
@app.route('/sum/qa', methods=['POST'])
def qa_endpoint():
	try:
		data = request.get_json(force=True)
	
		context = data['context']
		question = data['question']
		if question == "":
			response = jsonify({'error': '질문을 입력해주세요.'})
			return response
	
			to_predict = [{"context": context, "qas": [{"question": question, "id": "0"}]}]
	
			result = qa_model.predict(to_predict)
	
			answer = result[0][0]['answer'][0]
			answer = "적절한 답변을 찾을 수 없습니다." if answer == '' else answer
	
			response = jsonify({'answer': answer})
	
		except Exception as e:
			response = jsonify({'error': str(e)})
	
		return response
```
- 지정된 모델의 경로로부터 CUDA를 사용하지 않고 모델을 로드하며, 해당 모델은 `'qa_model'` 변수에 저장된다. 마지막으로, 포트 '5000'에서 flask 애플리케이션을 실행시킨다.

```Python
if __name__ == '__main__':
	model_path = 'model/checkpoint-1119-epoch-1'
	qa_model = get_qa_model(model_path, use_cuda=False)
	
	app.run(host='127.0.0.1',port=5000,debug=True)
	
```


**✔️ `ext.py`**<br />
- 키워드 중심으로 중요문장을 추출하는는 모듈이다.<br />
- 사용된 라이브러리:<br />
`konlpy`: 한국어 자연어 처리를 위한 라이브러리 <br />
`textrankr`: TextRank 알고리즘을 활용한 텍스트 요약을 제공하는 라이브러리

```Python
from typing import List
from konlpy.tag import Okt
from textrankr import TextRank
	
class OktTokenizer:
okt: Okt = Okt()

def __call__(self, text: str) -> List[str]:
	tokens: List[str] = self.okt.phrases(text)
	return tokens
	
def textrank_summarize(text: str, num_sentences: int, verbose: bool = True) -> str:
	mytokenizer: OktTokenizer = OktTokenizer()
	textrank: TextRank = TextRank(mytokenizer)
	summarized: str = textrank.summarize(text, num_sentences, verbose)
	return summarized
```


**✔️ `qa_model.py`**<br />
- 질문에 대한 답변을 제공하는 모듈이다.<br />
- 사용된 라이브러리:
	- `simpletransformers`: 간편한 사용을 위한 트랜스포머 모델 래핑 라이브러리<br />

```Python
import simpletransformers
	
from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs
	
def get_qa_model(model_path, use_cuda=False):
	print('Loading model from', model_path)
	qa_model = QuestionAnsweringModel('bert', model_path, use_cuda=use_cuda)
	return qa_model
```	



**✔️ `sum_model.py`**<br />
- 자기소개서를 포괄적으로 생성요약하는 모듈이다.<br />
- 사용된 라이브러리:<br />
	- `transformers`: Hugging Face의 트랜스포머 모델 라이브러리<br />

```Python	
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration
def summarize_model(text: str, verbose: bool = True) -> str:
	tokenizer = PreTrainedTokenizerFast.from_pretrained('digit82/kobart-summarization')
	model = BartForConditionalGeneration.from_pretrained('digit82/kobart-summarization')
	input_ids = tokenizer.encode(text, return_tensors="pt")
	    summary_text_ids = model.generate(
	        input_ids=input_ids,
	        bos_token_id=model.config.bos_token_id,
	        eos_token_id=model.config.eos_token_id,
	        length_penalty=2.0,
	        max_length=102,
	        min_length=20,
	        num_beams=4,
	    )
	    summarized_text = tokenizer.decode(summary_text_ids[0], skip_special_tokens=True)
	    
	    return summarized_text
```
