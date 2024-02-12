from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

def get_sum_model(model_path, use_cuda=False):
    sum_model = BartForConditionalGeneration('bart', model_path, use_cuda=use_cuda)
    return sum_model
