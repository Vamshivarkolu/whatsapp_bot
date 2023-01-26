from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import datetime as dt
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    cur = dt.datetime.now()
    if(cur.minute == 47):
        msg.body(cur.strftime('%H:%M'))
        responded = True
    if(incoming_msg == "date"):
        msg.body(cur.strftime('%d-%m-%Y'))
        responded = True
    if(incoming_msg == "time"):
        msg.body(cur.strftime('%H:%M'))
        responded = True
    if 'hi' in incoming_msg:
        msg.body('how are you Vijay krishna')
        responded = True
    if not responded:
        msg.body('sorry! I am still on development stage')
    return str(resp)

if __name__ =="__main__":
    app.run(port=4000,debug=True)
