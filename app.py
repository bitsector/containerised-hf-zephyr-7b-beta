from flask import Flask, request, jsonify
import torch
from transformers import pipeline

app = Flask(__name__)

# Initialize the pipeline
pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta", torch_dtype=torch.bfloat16, device_map="auto")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    
    response = outputs[0]["generated_text"].split("<|assistant|>")[-1].strip()
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
