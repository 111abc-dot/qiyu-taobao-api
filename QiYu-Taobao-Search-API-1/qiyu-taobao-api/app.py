from flask import Flask, request, jsonify
from urllib.parse import quote

app = Flask(__name__)

@app.get('/')
def index():
    return jsonify({
        'name': 'QiYu Taobao Search API',
        'status': 'ok',
        'usage': '/search?query=中国书法初学者套装'
    })

@app.get('/search')
def search():
    query = (request.args.get('query') or '').strip()
    if not query:
        return jsonify({'error': 'query is required'}), 400
    url = 'https://s.taobao.com/search?q=' + quote(query, safe='')
    return jsonify({'platform': 'Taobao', 'query': query, 'url': url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
