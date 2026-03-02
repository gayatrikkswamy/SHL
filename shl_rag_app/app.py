
from flask import Flask,request
from rag import search

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h2>SHL Product Recommendation Tool</h2>
    <form method="post" action="/search">
    Enter Query:
    <input name="query">
    <input type="submit">
    </form>
    '''

@app.route("/search",methods=["POST"])
def result():
    query = request.form["query"]
    results = search(query)
    return str(results)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=10000)
