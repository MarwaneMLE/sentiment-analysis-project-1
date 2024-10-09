from flask import Flask, request, jsonify, render_template
from model.model import GetSentimentModel 

app = Flask(__name__)

model = GetSentimentModel()

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():  
    text = request.form.get("text") 
    
    if not text:
        return jsonify({"Error": "No text provided"}), 400 #converts the output of a function to a JSON response object
 
    prediction = model.predict_sentiment(text).upper()
    return render_template("index.html", sentiment=prediction, text=text)


if __name__ == "__main__":
    app.run(debug=True)