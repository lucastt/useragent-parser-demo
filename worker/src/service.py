import os
import random
from rabbit import consume

queue_id = random.randint(1, int(os.environ['SCALE']))


def main():
    consume(str(queue_id), callback)


def callback(ch, method, properties, body):
    message = str(body)

    parsed_user_agent = parse(message)

    print('========================')
    print(str(body))  
    print('------------------------')
    print(parsed_user_agent)
    print('========================')


def parse(message):
    user_agent = {
        'os': None,
        'browser': None
    }

    oses = ['Windows', 'Macintosh', 'Linux', 'Android', 'iPhone']
    browsers = ['Firefox', 'Opera', 'Chrome', 'Chromium']

    for os in oses:
        if os in message:
            user_agent['os'] = os
            break

    for browser in browsers:
        if browser in message:
            user_agent['browser'] = browser
            break

    if user_agent.get('os') is None:
        user_agent['os'] = 'Other'
        
    
    if user_agent.get('browser') is None:
        user_agent['browser'] = 'Other'

    return user_agent


if __name__ == "__main__":
    main()
