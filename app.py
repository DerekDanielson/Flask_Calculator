from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add_it():
    """Add A and B parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)


@app.route('/sub')
def subtract_it():
    """Subtract A and B parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)


@app.route('/mult')
def multiply_it():
    """Multiply A and B parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return str(result)


@app.route('/div')
def divide_it():
    """Divide A and B parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)










