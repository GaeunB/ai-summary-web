# -*- coding: utf-8 -*-
from flask import Flask,render_template,request, jsonify
from flask_cors import CORS
import torch
from sum_model import summarize_model
from ext import textrank_summarize
from qa_model import get_qa_model

app = Flask(__name__)

cors = CORS(app)

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
		keytext = textrank_summarize(context,2)
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

if __name__ == '__main__':
	model_path = 'model/checkpoint-1119-epoch-1'
	qa_model = get_qa_model(model_path, use_cuda=False)
	
    # general summarization
    # summodel_path = 'model/model.pt'
    # sum_model=get_sum_model(summodel_path)
    # sum_model.load_state_dict(torch.load(summodel_path), strict=False)
    # sum_model.eval()

	app.run(host='127.0.0.1',port=5000,debug=True)