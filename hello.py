from flask import Flask, jsonify, abort, request
from pyteaser import SummarizeUrl
from pyteaser import Summarize

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/api/website')
def get_summary_for_url():
    url = request.args.get('url')
    summaries = SummarizeUrl(url)
    if summaries is None:
        return jsonify({'url': url, 'summaries': []})
    else:
        return jsonify({'url': url, 'summaries': summaries})


@app.route('/api/content')
def get_summary():
    text = request.args.get('text')
    title = request.args.get('title')

    summaries = Summarize(title, text)
    if summaries is None:
        jsonify({'url': url, 'summaries': []})
    else:
        return jsonify({'title': title, 'summaries': summaries})


if __name__ == '__main__':
    app.run(debug=True)