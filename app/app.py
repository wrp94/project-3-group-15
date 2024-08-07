from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql = SQLHelper()

#################################################
# Flask Routes
#################################################


# HTML ROUTES
@app.route("/")
def index():
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/map")
def map():
    return render_template("map.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


# SQL Queries
@app.route("/api/v1.0/get_bar/<gender>/<marital_status>")
def get_bar(gender, marital_status):
    data = sql.get_bar(gender, marital_status)

    return jsonify(data)


@app.route("/api/v1.0/get_map/<occupation>")
def get_map(occupation):
    data = sql.get_map(occupation)

    return jsonify(data)


@app.route("/api/v1.0/get_donut/<gender>/<marital_status>")
def get_donut(gender, marital_status):
    data = sql.get_donut(gender, marital_status)

    return jsonify(data)


@app.route("/api/v1.0/get_violin/<gender>/<marital_status>")
def get_violin(gender, marital_status):
    data = sql.get_violin(gender, marital_status)

    return jsonify(data)
