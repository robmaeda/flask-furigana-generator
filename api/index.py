from flask import Flask, request, jsonify
import MeCab
import jaconv

app = Flask(__name__)
tagger = MeCab.Tagger("-Ochasen")

def process_text(text):
    parsed = tagger.parse(text)
    output = ""
    lines = parsed.split('\n')
    for line in lines:
        columns = line.split('\t')
        if len(columns) >= 3:
            original = columns[0]
            reading = columns[1]
            hiragana = jaconv.kata2hira(reading)
            if original != hiragana:
                # Create Ruby annotation if original and reading are different
                output += f"<ruby>{original}<rt>{hiragana}</rt></ruby>"
            else:
                output += original
    return output

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
