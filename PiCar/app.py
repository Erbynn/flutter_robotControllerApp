#!/usr/bin/python3
from flask import Flask, request, jsonify
from move_car import *
from servo_motor import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'This is the secret key'


@app.route('/forward', methods=['GET'])
def move_forward():
    forward()
    return jsonify({"Success":"True"})


@app.route('/backward', methods=['GET'])
def move_back():
    backward()
    return jsonify({"Success":"True"})


@app.route('/left', methods=['GET'])
def move_Left():
    turnLeft()
    forward()
    return jsonify({"Success":"True"})


@app.route('/right', methods=['GET'])
def move_Right():
    turnRight()
    forward()
    return jsonify({"Success":"True"})


@app.route('/stop', methods=['GET'])
def stp():
    stop()
    return jsonify({"Success":"True"})

@app.route('/servo', methods=['GET'])
def move_servo(): 
    moveServoLeftToRight()
    return jsonify({"Success":"True"})


if __name__ == '__main__':
    app.run(debug=True, host='192.168.6.1', port=5050)
