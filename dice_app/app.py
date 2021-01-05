from flask import Flask, jsonify, render_template, request, make_response
import requests

from dice_app.dice import dice_calc


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index/select-dice", methods=["POST", "GET"])
def select_dice():
    num_dice = request.get_json()
    print(num_dice)
    print(type(num_dice))

    response = dice_calc(num_dice)

    return response
    





