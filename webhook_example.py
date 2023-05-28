from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    sender = request.form.get('From')
    receiver = request.form.get('To')
    message = request.form.get('Body')
    print("print hello world for test :/")
    print(f'Message from {sender} to {receiver}: {message}')
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ['PORT']))
    
