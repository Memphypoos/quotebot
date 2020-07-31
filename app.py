import requests
import json
import random
from flask import Flask, render_template, request, Response

#SLACK_WEBHOOK_SECRET = 'https://hooks.slack.com/services/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'

## This will append a new quote to the end of Quotes.txt
def addQuote(newQuote):
  f = open("quotes.txt", "a+")
  f.write(newQuote + "\n")
  print("Quote Added")
  f.close()
addQuote(input("Whats the quote?" + "\n"))

## This will pull a random quote from Quotes.txt
def getQuote():
  f = open("quotes.txt", "r")
  count = len(open("quotes.txt").readlines(  ))
  random_number = random.randint(0, count -1)
  lines = f.readlines()
  random_quote = lines[random_number]
  return(random_quote)

## This will post to #h0s_it as QuoteBot app via webhook
def postHook():
  url = 'https://hooks.slack.com/services/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'
  data = {"text": "I am posting as the app"}
  r = requests.post(url, json=data)
  print(r)
#postHook()

## This will post to #h0s_it as QuoteBot user
def postQuote():
  url = 'https://slack.com/api/chat.postMessage'
  payload = '{"channel": "#h0s_it", "text": "Matt: The Notebook is in my top 10"}'
  headers = {'User-Agent':"QuoteBot",'Authorization':'Bearer '+ "xoxb-43069909811-1245594843351-zbpcsgvbyAcSn7YcYpJ2hONs", 'Content-Type': "application/json; charset=utf-8"}
  r = requests.post(url, data=payload, headers=headers)
  print(r)
#postQuote()


app = Flask (
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/')
def index():
  return render_template(
    'index.html',
    quote = getQuote()
  )
@app.route('/slack')
def slack():
  return render_template(
    'slack.html' 
  )

'''
@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200

@app.route('/', methods=['GET'])
def test():
    return Response('It works!')
'''


if __name__ == "__main__":
  app.run(
    host='0.0.0.0',
    port=random.randint(2000, 9000)
  )



