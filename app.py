from aitextgen import aitextgen
from flask import Flask, abort, jsonify, request, render_template

app = Flask(__name__)
model = aitextgen(model="model/pytorch_model.bin", config="model/config.json")

@app.route('/')
def home():
    return render_template('index.html') 

@app.route("/generate", methods=['POST'])
def generate():
    prompt = request.form['prompt']
    result = model.generate(
                n=1,
                prompt=prompt,
                max_length=200,
                temperature=1.0,
                top_p=0.9,
                top_k=10,
                return_as_list=True
            )[0]
    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)

