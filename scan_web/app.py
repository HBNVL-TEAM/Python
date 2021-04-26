from flask import Flask,render_template,request,send_file
import requests as rq
import json
import os
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
    os.system('wafw00f '+url+' -o /home/phuctruong2k/'+url+'.json')
    #rp=rq.get('https://sonar.omnisint.io/subdomains/'+url)
    rp=rq.get('https://api.hackertarget.com/hostsearch/?q='+url)
    sum=0
    s=''
    for i in rp.text.split('\n'):
        s+='<tr><td>{0}. {1}</td><tr>'.format(sum+1,i.replace(',',' IP: '))+"\n"
        sum+=1
    table_1='''
    <h2> Scan subdomain</h2>
    <div class="table-wrapper-scroll-y my-custom-scrollbar">
    <table class="table table-dark table-hover table-striped mb-0">   
        <thead>
            <tr>
                <th colspan="2" style="background-color: green;">Total subdomain: {0}</th>
            </tr>
        </thead>
    '''.format(sum)

    data={'remoteAddress':url,'key':''}
    reip=rq.post('https://domains.yougetsignal.com/domains.php',data)
    c=json.loads(reip.text)
    s2=''
    sum2=0
    if c['status']=='Fail':
        s2='<tr><td>Không tìm thấy dữ liệu</tr></td>'
    elif c['domainArray']!='':
        for j in c['domainArray']:
            s2+='<tr><td>{0}. {1}</td><tr>'.format(sum2+1,j[0])+"\n"
            #print(j[0])
            sum2+=1
    
    table_2='''
    <h2> Reverse ip </h2>
    <div class="table-wrapper-scroll-y my-custom-scrollbar">
    <table class="table table-dark table-hover table-striped mb-0">   
        <thead>
            <tr>
                <th colspan="2" style="background-color: green;">Total Reverse IP: {0}</th>
            </tr>
        </thead>
    '''.format(sum2)

    sub=table_1+s+'</tbody></table></div>'
    reip_t=table_2+s2+'</tbody></table></div>'
    return sub  + reip_t
if __name__ =="__main__":
    app.run(host="127.0.0.1",port=8083)
    