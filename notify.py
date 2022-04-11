!pip install pushbullet.py
from pushbullet import Pushbullet
API_KEY = "YOUR_API_KEY"

with open('/res.txt', mode='r') as f:
    text = f.read()
pb= Pushbullet(API_KEY)
push = pb.push_note("Greeting", text)
