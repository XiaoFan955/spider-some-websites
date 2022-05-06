from app import app
from flask import Flask, request, render_template
import urllib.request
import json

from app.dataSpider import get_data_list


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/bilibili/series', methods=['GET', 'POST'])
def getData():
    data = request.form
    uid = data["uid"]
    total_list = get_data_list(uid)
    if not total_list:
        res_dict = {
            "total_list": None,
            "haveData": False,
            "info": "failed to load data, check your uid!"
        }
        return res_dict
    res_dict = {
        "total_list": total_list,
        "haveData": True,
        "info": "success"
    }
    return res_dict
