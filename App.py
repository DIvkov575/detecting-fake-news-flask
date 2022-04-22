from flask import Flask, render_template, request
import pickle

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
    global pac, tfidf_vectorizer

    input_raw = request.form.to_dict()
    input_1 = input_raw['input_1']

    # if url get text data from url
    if input_1.startswith("https://"):
        import requests
        from bs4 import BeautifulSoup
        res = requests.get(input_1)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.get_text()
        link = input_1
    else:
        text = input_1
        link = None

    tfidf_out = tfidf_vectorizer.transform([text])
    result = str(pac.predict(tfidf_out))

    return render_template('template-b-post-submit.html', result=result[2:-2], full_input_text=text, link=link)


if __name__ == '__main__':
    app.run()
