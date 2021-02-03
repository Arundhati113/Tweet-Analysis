import tweepy

from tweepy.auth import OAuthHandler

from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

ACCESS_TOKEN = '1334228279541161984-z2EEa1hGncOhBIjpcf5JgU3BNz2YOX'
ACCESS_SECRET = 'VBdxTfsgsKrlRepJnd3jEChbUFlab66FekUIH99bR5KhV'
CONSUMER_KEY = 'wGY12mHOm6XTZoxSA1T3O14t4'
CONSUMER_SECRET = 'Phyv0Vag6zEE1CazulnmIzt3VAcQGr8BAR48NvhP2qpsbXzc5R'

class TweetsListener(StreamListener):
  def __init__(self,csocket):
    self.client_socket=csocket
  def on_data(self,data):
    try:
      msg=json.loads(data)
      print(msg['text'].encode('utf-8'))
      self.client_socket.send(msg['text'].encode('utf-8'))
      return True
    except BaseException as e:
      print("Error on_data:%s" % str(e))
    return True
  def on_error(self,status):
    print(status)
    return True

def sendData(c_socket):
  auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
  twitter_stream=Stream(auth,TweetsListener(c_socket))
  twitter_stream.filter(track = ['trending'])

if __name__=="__main__":
 s=socket.socket()
 host="127.0.0.1"
 port=5555
 s.bind((host,port))
 print("Listening on port: %s" % str(port))
 s.listen(5)
 c,addr=s.accept()
 print("Received request from "+ str(addr))
 sendData(c)
