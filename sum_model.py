from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

def get_sum_model(model_path, use_cuda=False):
    sum_model = BartForConditionalGeneration.from_pretrained(model_path)
    return sum_model
