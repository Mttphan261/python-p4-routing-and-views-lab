#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str>')
def print_string(str):
    print(str)
    return f'{str}'

@app.route('/count/<int:num>')
def count(num):
    # int_range = range(int(num))
    # count_strings = [f'{each}\n' for each in int_range]
    # return ''.join(count_strings)
    count = f''
    for n in range(num):
        count += f'{n}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = int
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2   
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    
    return str(result)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

