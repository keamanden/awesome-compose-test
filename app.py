from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='database', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'<h1>Hello from GitHub Actions!</h1><p>This page has been viewed {count} times.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
