from flask import Flask
from flask import request,jsonify
from service.messageService import MessageService

app=Flask(__name__)
app.config.from_pyfile('config.py')

messageService= MessageService()

@app.route('/v1/ds/message', methods=['POST'])
def handle_message():
    message=request.json.get('message')     # humein jo info aayegi wo aise aayegi {"message": "you have spent 1000 with your credit card bill"}
    result=messageService.process_message(message)
    if result:
        return result
    else:
        return None
    
@app.route('/',methods=['GET'])
def handle_endpoint():
    print("My DS Service is working")

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
