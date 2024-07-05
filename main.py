from flask import Flask
import redis 
import sys 
import logging
import pulsar
import uuid

logging.basicConfig(level=logging.INFO)



app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("hola")

    client = redis.StrictRedis(host='10.43.239.42', port=6379, decode_responses=True)


    try: 
        client.ping()
        app.logger.info("Connected to Redis")

    except Exception as e:
        app.logger.info("Error connecting to Redis")
        app.logger.error(str(e))


    try:
        client = pulsar.Client('pulsar://localhost:6650')
        topic = 'persistent://fidelizador/relay/test'

        producer = client.create_producer(topic)
        for i in range(20):
            text = "{}".format(uuid.uuid4())
            producer.send(text.encode('utf-8'))
            logging.info("Message: %s sent to %s", text, topic)


    except Exception as e:
        app.logger.info("Error connecting to Pulsar")
        app.logger.error(str(e))

    return "Hello from Python! 3"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

