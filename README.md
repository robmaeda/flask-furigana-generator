# flask-furigana-generator

Input Japanese text to add furigana above Kanji characters.

The backend for [react-furigana-generator](https://github.com/robmaeda/react-furigana-generator).

This utilizes [tinysegmenter](https://pypi.org/project/tinysegmenter3/0.1.0/) to tokenize Japanese text into the correct parts, then [pykakasi](https://pypi.org/project/pykakasi/) to add hiragana above Kanji characters and katakana.
