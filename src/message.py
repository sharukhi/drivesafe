from  pushbullet import Pushbullet



API_KEY = 'api-key'
file = 'alert.txt'


with open(file, mode='r') as f:
    text = f.read()

    pb = Pushbullet(API_KEY)
    push = pb.push_note('Alert!!!' , text)