from app import app
from flask import Flask, request, render_template
import urllib.request
import json


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/bilibili/series', methods=['GET', 'POST'])
def getData():
    data = request.form
    uid = data["uid"]
    url = f'https://api.bilibili.com/x/polymer/space/seasons_series_list?mid={uid}&page_num=1&page_size=20'
    r = urllib.request.urlopen(url)
    datas = r.read().decode('utf-8')
    datas = json.loads(datas)
    seasons_list = datas["data"]["items_lists"]["seasons_list"]
    series_list = datas["data"]["items_lists"]["series_list"]
    total_list = seasons_list + series_list
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
