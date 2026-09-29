# QiYu Taobao Search API

A tiny URL-builder API for QiYu Culture Kit. It does not call Taobao APIs and does not access user accounts, prices, inventory, sellers, or orders.

## Endpoint
GET /search?query=<Chinese search phrase>

Example response:
{
  "platform": "Taobao",
  "query": "中国书法初学者套装",
  "url": "https://s.taobao.com/search?q=..."
}

## Deploy
Any public HTTPS Python hosting works. Build: `pip install -r requirements.txt`; Start: `gunicorn app:app --bind 0.0.0.0:$PORT`.
