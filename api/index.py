from flask import Flask, request, jsonify
from flask_cors import CORS
import tinysegmenter
import pykakasi

app = Flask(__name__)
segmenter = tinysegmenter.TinySegmenter()
kks = pykakasi.kakasi()

def process_text(text):
    tokenized_statement = segmenter.tokenize(text)
    output = ""
    for token in tokenized_statement:
        token_dict = kks.convert(token)
        hiragana = token_dict[0]["hira"]
        if token != hiragana:
            output += f"<ruby>{token}<rt>{hiragana}</rt></ruby>"
        else:
            output += token
    return output

CORS(app, resources={r"/furigana": {"origins": "https://react-furigana-generator.vercel.app"}})
@app.route('/furigana', methods=['POST'])
def furigana():
    if request.is_json:
        text = request.json['text']
        result = process_text(text)
        return jsonify({'result': result})
    else:
        return "Invalid or missing JSON", 400

if __name__ == '__main__':
    app.run(debug=True)
