from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator", static_folder="static")


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


@app.route("/englishToFrench", methods=["GET"])
def englishToFrench():
    textToTranslate = request.args.get("textToTranslate")
    translated = translator.english_to_french(textToTranslate)

    return "Translated text to French: " + translated


@app.route("/frenchToEnglish", methods=["GET"])
def frenchToEnglish():
    textToTranslate = request.args.get("textToTranslate")
    translated = translator.french_to_english(textToTranslate)

    return "Translated text to English: " + translated


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
