from flask import Flask, request
app = Flask(__name__)


from app import routes  # 避免循环引用
