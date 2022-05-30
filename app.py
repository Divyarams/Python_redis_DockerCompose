import logging
import redis
from flask import Flask

client = redis.Redis(host='cache_store', port = 6379)
count = client.get('value')
app = Flask(__name__)
@app.route("/")
def index():
    global count
    count+=1
    app.logger.warning('testing info')
    return str(count)
if __name__ =="__main__":
    app.run(host='localhost',port=5000)