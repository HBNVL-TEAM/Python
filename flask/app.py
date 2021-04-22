from flask import Flask,render_template,request,send_file
import requests as rq
import json
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/home/home.html')
def show_home():
    return send_file('templates/home.html')

@app.route('/dashboard/dashboard.html')
def show_dashboard():
    return send_file('templates/dashboard.html')

@app.route('/contact/contact.html')
def show_contact():
    return send_file('templates/contact.html')

@app.route('/subdomain/<url>',methods=['GET'])
def subdomain(url):
    rp=rq.get('https://sonar.omnisint.io/subdomains/'+url)
    sum=0
    s=''
    for i in json.loads(rp.text):
        s+='<tr><td>{0}. {1}</td><tr>'.format(sum+1,i)+"\n";
        sum+=1
    table='''
    <div class="table-wrapper-scroll-y my-custom-scrollbar">
    <table class="table table-dark table-hover table-striped mb-0">   
        <thead>
            <tr>
                <th colspan="2" style="background-color: green;">Total subdomain: {0}</th>
            </tr>
        </thead>
    '''.format(sum)
    index=table+s+'</tbody></table></div>'
    return index
if __name__ =="__main__":
    app.run(host="127.0.0.1",port=80)
    