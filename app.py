# -*- coding: utf-8 -*-
from flask import Flask,render_template,request, jsonify
from flask_cors import CORS
from ext import textrank_summarize

app = Flask(__name__)

cors = CORS(app)

@app.route('/')	
def index():
	return render_template('index.html')

@app.route('/key',methods=['POST'])
def key():
	try:
		# data = request.get_json(force=True)
		# context = data['context']
		# text
		context = ("현장을 아는 전문가"+
                "코오롱생명과학에 입사한다면, 다음과 같은 계획을 바탕으로 해외영업 전문가로서 성장하겠습니다."+
                " 먼저, 우선 내부 상황 전문가가 되겠습니다."+
                "공장 및 연구 부서를 방문하여 모든 것을 직접 눈으로 확인하여, 생산 공정 및 제품의 특성을 파악하도록 하겠습니다."+
                "또한, 담당자들과 반드시 1번씩은 술자리를 가지며 친분을 쌓고, 각자가 처한 상황을 이해하겠습니다."+
                "그 후에, 해외 현지 상황에 대한 철저한 분석을 바탕으로 영업 전략 수립을 추진하겠습니다."+
                "최근 유럽, 미국 등 해외에서는 현지의 처방 의약품에 대한 비용 부담 증가로 인해, 상대적으로 가격이 저렴한 해외 의약품의 수입을 정부 주도하에 장려하고 있는 상황입니다."+
                "이러한 제네릭 의약품 시장의 호황을 기회로 보아야 합니다."+
                "따라서, 국가별로 소비자들의 수요가 많은 의약품을 분석한 후, 당사의 글로벌 네트워크를 활용하여 해외 제약사에게 오퍼 하는 방식으로 시장 특성에 맞는 제품 공급 체결을 위해 힘쓰겠습니다.")
		#context에 관하여 추가해야할 것같다. 
		keytext = textrank_summarize(context,2)
		response = jsonify({'keytext': keytext})

	except Exception as e:
		response = jsonify({'error': str(e)})	
		
	return response
	

if __name__ == '__main__':
	app.run(host='127.0.0.1',port=5000,debug=True)