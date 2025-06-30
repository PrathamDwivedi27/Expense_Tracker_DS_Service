from flask import Flask
from flask import request,jsonify

app=Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/v1/ds/message', methods=['POST'])
def handle_message():
    message=request.json.get('message')     # humein jo info aayegi wo aise aayegi {"message": "you have spent 1000 with your credit card bill"}
    