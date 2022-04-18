from flask import Flask, render_template, request
import pickle
import sys
from bs4 import BeautifulSoup
import requests
import urllib
import re

app = Flask(__name__, template_folder='./template/')


@app.route('/', methods=['GET', 'POST'])
def main():
    global pac, tfidf_vectorizer

    with open("Assets/sklearn_fit.pkl", 'rb') as weights_file:
        pac = pickle.load(weights_file)
    with open("Assets/tfidf_vectorizer_w_fit.pkl", 'rb') as tfidf_file:
        tfidf_vectorizer = pickle.load(tfidf_file)

    return render_template('template-a.html')


@app.route('/output', methods=['POST', 'GET'])
def output():
    global pac, tfidf

    input_raw = request.form.to_dict()
    url_link = input_raw['input_1']

    res = requests.get(url_link)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser'
                                    '')
    text = soup.find_all(text=True)


    print(text, file=sys.stderr)

    # input_1 = ""
    # tfidf_out = tfidf_vectorizer.transform([text])
    # result = str(pac.predict(tfidf_out))
    #
    # # print(result[2:-2], file=sys.stderr)

    return render_template('template-b-post-submit.html', result=result[2:-2], full_input_text=input_1)


if __name__ == '__main__':
    app.run()
