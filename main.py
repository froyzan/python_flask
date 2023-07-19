from flask import Flask, render_template, request
import plotly.graph_objs as go
import plotly


app = Flask(__name__)


def analyze_text(text):
    freq = {}
    for char in text:
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        freq = analyze_text(text)
        x = list(freq.keys())
        y = list(freq.values())
        bar = go.Bar(x=x, y=y)
        data = [bar]
        graphJSON = plotly.offline.plot(data, output_type='div')
        return render_template("results.html", graphJSON=graphJSON)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
