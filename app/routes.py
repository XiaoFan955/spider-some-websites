from app import app
from flask import Flask, request, render_template
import re

from app.dataSpider import get_data_list


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/bilibili/series', methods=['GET', 'POST'])
def getData():
    data = request.form
    uid = data["uid"]
    if not checkUid(uid):
        res_dic = {
            "total_list": None,
            "haveData": False,
            "info": "not a uid, check your input!"
        }
        return res_dic
    total_list = get_data_list(uid)
    if not total_list:
        res_dict = {
            "total_list": None,
            "haveData": False,
            "info": "no more data"
        }
        return res_dict
    res_dict = {
        "total_list": total_list,
        "haveData": True,
        "info": "success"
    }
    return res_dict


def checkUid(uid):
    reg = r"\d+"
    if re.fullmatch(reg, uid) is None:
        return False
    return True
