from flask import Flask, request, jsonify
import pykakasi

app = Flask(__name__)
kks = pykakasi.kakasi()

def process_text(text):
    output = ""
    converted_text = kks.convert(text)
    for phrase in converted_text:
        original = phrase["orig"]
        hiragana = phrase["hira"]
        if original != hiragana:
            output += f"<ruby>{original}<rt>{hiragana}</rt></ruby>"
        else:
            output += original
    return output

@app.route('/furigana', methods=['POST'])
def furigana():
    if request.is_json:
        text = request.json['text']
        result = process_text(text)
        print(result)
        return jsonify({'result': result})
    else:
        return "Invalid or missing JSON", 400

if __name__ == '__main__':
    app.run(debug=True)
