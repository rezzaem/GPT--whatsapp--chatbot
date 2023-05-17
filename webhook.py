from flask import Flask,request,jsonify
import json

app=Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    # do something with the data
    return jsonify({'status': 'ok'})

if __name__=='__main__':
    app.run()