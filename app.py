import requests
from flask import Flask,render_template,url_for
from flask import request as req
import nltk
from newspaper import Article
import urllib.request
from bs4 import BeautifulSoup

def summarize(url):
    article = Article(url)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()
    authors = article.authors
    date = article.publish_date
    data = article.text
    summary = article.summary
    return summary

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    if req.method == "POST":
        url = req.form.get("url")
        url_content = summarize(url)
        return render_template("main.html",value=url_content)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)