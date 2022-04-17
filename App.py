from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import sys

app = Flask(__name__, template_folder='./template/')


@app.route('/', methods=['GET', 'POST'])
def main():
    # with open("Assets/sample.pkl", 'r') as weights_file:
    #     pac = pickle.load(weights_file)
    # with open("Assets/tfidf_vectorizer_w_fit.pkl", 'r') as tfidf_file:
    #     tfidf_vectorizer = pickle.load(tfidf_file)

    return render_template('template-a.html')


@app.route('/output', methods=['POST', 'GET'])
def output():
    with open("Assets/sklearn_fit.pkl", 'rb') as weights_file:
        pac = pickle.load(weights_file)
    with open("Assets/tfidf_vectorizer_w_fit.pkl", 'rb') as tfidf_file:
        tfidf_vectorizer = pickle.load(tfidf_file)

    input_raw = request.form.to_dict()
    input_1 = input_raw['input_1']

    tfidf_out = tfidf_vectorizer.transform([input_1])
    result = pac.predict(tfidf_out)

    return render_template('template-b-post-submit.html', input_1=result)


if __name__ == '__main__':
    app.run()
