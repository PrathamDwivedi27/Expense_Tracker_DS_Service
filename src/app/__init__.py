from flask import Flask
from flask import request,jsonify
from service.messageService import MessageService
from kafka import KafkaProducer
import json

app=Flask(__name__)
app.config.from_pyfile('config.py')

messageService= MessageService()
producer=KafkaProducer(bootstrap_servers=['localhost:9092'],
                       value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/v1/ds/message', methods=['POST'])
def handle_message():
    message=request.json.get('message')     # humein jo info aayegi wo aise aayegi {"message": "you have spent 1000 with your credit card bill"}
    result=messageService.process_message(message)
    if result:
        producer.send('ExpenseServiceTopic', result.model_dump())  # python stringify kar de rha hai json ko bhi
        return jsonify(result.model_dump()),200
    else:
        return jsonify({"error": "Message is not a bank SMS"}), 400

@app.route('/',methods=['GET'])
def handle_endpoint():
    print("My DS Service is working")
    return jsonify({"message": "My DS Service is working"}), 200

if __name__ == '__main__':
    app.run(host="localhost", port=3003, debug=True)
