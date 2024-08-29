from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Connect to Redis
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return jsonify(message="Hello, Docker!"), 200

@app.route('/visits')
def visits():
    count = cache.incr('visits')
    return jsonify(visits=count), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
