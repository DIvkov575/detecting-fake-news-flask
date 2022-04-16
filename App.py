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


@app.route('/', methods=['POST', 'GET'])
def output():

    with open("Assets/sklearn_fit.pkl", 'rb') as weights_file:
        pac = pickle.load(weights_file)
    with open("Assets/tfidf_vectorizer_w_fit.pkl", 'rb') as tfidf_file:
        tfidf_vectorizer = pickle.load(tfidf_file)

    input_raw = request.form.to_dict()
    input_1 = input_raw['input_1']

    tfidf_out = tfidf_vectorizer.transform([input_1])
    result = pac.predict(tfidf_out)

    # result = 'sd'

    return render_template('template-a.html', input_1=result)






# @app.route('/post_screen', methods=['POST', 'GET'])
# def output():
#     input_1 = request.form.to_dict()
#     print(input_1['input_1'], file=sys.stderr)
#
#     return render_template('template-b-post-submit.html', input_1=input_1['input_1'])


def tmp_ml():
    input = ""
    with open("Assets/sklearn_fit.pkl", 'rb') as weights_file:
        pac = pickle.load(weights_file)
    with open("Assets/tfidf_vectorizer_w_fit.pkl", 'rb') as tfidf_file:
        tfidf_vectorizer = pickle.load(tfidf_file)

    tfidf_out = tfidf_vectorizer.transform(input)
    result = pac.predict(tfidf_out)

    # print(input_1, file=sys.stderr)

if __name__ == '__main__':
    app.run()
