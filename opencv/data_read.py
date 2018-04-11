import os


def run():
    os.system('python camera_test_2.py')
    f = open('data.txt', 'r').read()
    return f

count = 10
while(count):
    count = count - 1
    print count
    value = run()
    print value
    
