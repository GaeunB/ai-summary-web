# -*- coding: utf-8 -*-
from flask import Flask,render_template,request, jsonify
from flask_cors import CORS
import os
from ext import summarize_text

app = Flask(__name__)

cors = CORS(app)

@app.route('/')	
def index():
	return render_template('index.html')

@app.route('/key',methods=['POST'])
def key():
	try:
		data = request.get_json(force=True)
		context = data['context']
		keytext = summarize_text(context)
		response = jsonify({'keytext': keytext})
		

	except Exception as e:
		response = jsonify({'error': str(e)})	
		
	return response
	

if __name__ == '__main__':
	app.run(debug=True)