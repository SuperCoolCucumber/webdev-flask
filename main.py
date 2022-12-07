from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def search_get(q):
    results = [{'id': 1, 'name': 'hello'}, {'id': 2, 'name': 'test'}]
    return [result for result in results if q.lower() in result['name'].lower()]

@app.route("/search")
def search():
    q = request.args.get("q", "")
    search_get(q)
    return render_template("search.html.j2", q=q, results=results)


"""
@app.route("/test", methods = ["GET", "POST"])
def hello_test():
    q = request.values.get('q', '')
    return render_template("index.html.j2", q1=q)

@app.route("/hello/<path:hello_name>")
def hello_hello(hello_name=None):
    return f"<p>Hello, {hello_name}!</p>"
"""

if __name__ == "__main__":
    app.run(debug=True)