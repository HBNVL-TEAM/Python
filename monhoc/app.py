from flask import Flask,render_template,request
import requests as rq
app = Flask(__name__)
def scan(url):
    a=['admin','cpanel','administrator']
    d={}
    for i in a:
        found=rq.get(url+i)
        d.update({url+i:found.status_code})
    return d
@app.route('/',methods=['POST','GET'])
def index():
    kq=None
    td=None
    tb=None
    hello=None
    if request.method=='GET':
        kq=td=tb=hello=None
    elif request.method=='POST':
        if 'scan' in request.form.values():
            td=["Web","Status",'']
            url=request.form['url']
            kq=scan(url)
        elif 'hello' in request.form.values():
            td=kq=None
            hello=request.form['chao']
    return render_template('index.html',kq=kq,td=td,hello=hello)
if __name__ =="__main__":
    app.run(host="127.0.0.1",port=80)
