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