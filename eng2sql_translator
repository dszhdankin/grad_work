#!./venv/bin/python

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

import nltk
nltk.download('punkt')

model_name = "t5-small-english-to-sql-raw-translation/checkpoint-18600"
model_dir = f"models/{model_name}"

tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

max_input_length = 512
max_output_length = 128

while True:
    print("question >> ", end='')
    text = input()
    if text == "\\quit":
        break
    inputs = ["translate English to SQL: " + text]

    inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=8, do_sample=True, min_length=4, max_length=128)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    predicted_query = nltk.sent_tokenize(decoded_output.strip())[0]

    print(predicted_query)


print("OK")
