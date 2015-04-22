from flask import Flask, jsonify, abort, request, current_app
from pyteaser import SummarizeUrl
from pyteaser import Summarize
from functools import wraps

app = Flask(__name__)


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f().data) + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)

    return decorated_function


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/api/website')
@support_jsonp
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