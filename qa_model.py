import simpletransformers

from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs

def get_qa_model(model_path, use_cuda=False):
    print('Loading model from', model_path)
    qa_model = QuestionAnsweringModel('bert', model_path, use_cuda=use_cuda)
    return qa_model