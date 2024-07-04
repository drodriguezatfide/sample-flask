from flask import Flask
import redis 

app = Flask(__name__)

@app.route("/")
def hello():
    print("hola")

    client = redis.StrictRedis(host='redis-cluster', port=6379, decode_responses=True)
    try: 
        client.ping()
        print("Connected to Redis")

    except Exception:
        print("Error connecting to Redis")

    return "Hello from Python!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')