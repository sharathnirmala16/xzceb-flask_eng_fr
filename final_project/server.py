
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def englishToFrench(english_text):
    textToTranslate = request.args.get(english_text)
    # Write your code here
    resp = translator.english_to_french(textToTranslate)
    return resp

@app.route("/french_to_english")
def frenchToEnglish(french_text):
    textToTranslate = request.args.get(french_text)
    # Write your code here
    resp = translator.french_to_english(textToTranslate)
    return resp

@app.route("/static/mywebscript.js")
def renderIndexPage():
    # Write the code to render template
    return render_template('/xzceb-flask_eng_fr/final_project/static/mywebscript.js')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
