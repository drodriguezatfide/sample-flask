from flask import Flask
import redis 
import sys 
import logging
logging.basicConfig(level=logging.INFO)



app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("hola")

    client = redis.StrictRedis(host='redis-cluster', port=6379, decode_responses=True)
    try: 
        client.ping()
        app.logger.info("Connected to Redis")

    except Exception:
        app.logger.info("Error connecting to Redis")

    return "Hello from Python! 3"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

