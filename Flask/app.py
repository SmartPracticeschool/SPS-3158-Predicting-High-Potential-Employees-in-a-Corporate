import numpy as np
from flask import Flask, request, jsonify, render_template
import json
import requests

app = Flask(__name__)
URL = "https://jjyhrpmbd5.execute-api.us-east-1.amazonaws.com/test/employee"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict', methods = ['POST'])
def y_predict():
    req = request.form
    age = req.get('age')
    att = req.get('attradio')
    dRate = req.get('dRate')
    dist = req.get('dist')
    edu = req.get('edu')
    envradio = req.get('envradio')
    Genderradio = req.get('Genderradio')
    hrr = req.get('hrr')
    JIradio = req.get('JIradio')
    JLradio = req.get('JLradio')
    JSradio = req.get('JSradio')
    MI = req.get('MI')
    Mrate = req.get('Mrate')
    NumComp = req.get('NumComp')
    Overtimeradio = req.get('Overtimeradio')
    PercentHike = req.get('PercentHike')
    PerfRateradio = req.get('PerfRateradio')
    RSradio = req.get('RSradio')
    StockOLradio = req.get('StockOLradio')
    WorkingYrs = req.get('WorkingYrs')
    TTLY = req.get('TTLY')
    WLbalanceradio = req.get('WLbalanceradio')
    YrsComp = req.get('YrsComp')
    YrsCurrent = req.get('YrsCurrent')
    YrsPromotion = req.get('YrsPromotion')
    YrsCurrManager = req.get('YrsCurrManager')
    Bradio = req.get('Bradio')
    if(int(Bradio) == 1):
        Non_travel = 1
        travel_freq = 0
        travel_r = 0
    elif(int(Bradio) == 2):
        Non_travel = 0
        travel_freq = 1
        travel_r = 0
    else:
        Non_travel = 0
        travel_freq = 0
        travel_r = 1
    Deptradio = req.get('Deptradio')
    if(int(Deptradio) == 1):
        hRes = 1
        RnD = 0
        sales = 0
    elif(int(Deptradio) == 2):
        hRes = 0
        RnD = 1
        sales = 0
    else:
        hRes = 0
        RnD = 0
        sales = 1
    EduField = req.get('EduField')
    if(int(EduField) == 1):
        hr_field = 1
        ls_field = 0
        fm_field = 0
        med_field = 0
        td_field = 0
        o_field =0
    elif(int(EduField) == 2):
        hr_field = 0
        ls_field = 1
        fm_field = 0
        med_field = 0
        td_field = 0
        o_field =0
    elif(int(EduField) == 3):
        hr_field = 0
        ls_field = 0
        fm_field = 1
        med_field = 0
        td_field = 0
        o_field =0
    elif(int(EduField) == 4):
        hr_field = 0
        ls_field = 0
        fm_field = 0
        med_field = 1
        td_field = 0
        o_field =0
    elif(int(EduField) == 5):
        hr_field = 0
        ls_field = 0
        fm_field = 0
        med_field = 0
        td_field = 1
        o_field =0
    else:
        hr_field = 0
        ls_field = 0
        fm_field = 0
        med_field = 0
        td_field = 0
        o_field = 1
    JobRole = req.get('JobRole')
    if(int(JobRole) == 1):
        health_jr = 1
        hr_jr = 0
        lt_jr =0
        man_jr = 0
        md_jr = 0
        rd_jr = 0
        rs_jr = 0
        se_jr = 0
        sr_jr = 0
    elif(int(JobRole) == 2):
        health_jr = 0
        hr_jr = 1
        lt_jr =0
        man_jr = 0
        md_jr = 0
        rd_jr = 0
        rs_jr = 0
        se_jr = 0
        sr_jr = 0
    elif(int(JobRole) == 3):
        health_jr = 0
        hr_jr = 0
        lt_jr =1
        man_jr = 0
        md_jr = 0
        rd_jr = 0
        rs_jr = 0
        se_jr = 0
        sr_jr = 0
    elif(int(JobRole) == 4):
        health_jr = 0
        hr_jr = 0
        lt_jr =0
        man_jr = 1
        md_jr = 0
        rd_jr = 0
        rs_jr = 0
        se_jr = 0
        sr_jr = 0
    elif(int(JobRole) == 5):
        health_jr = 0
        hr_jr = 0
        lt_jr =0
        man_jr = 0
        md_jr = 1
        rd_jr = 0
        rs_jr = 0
        se_jr = 0
        sr_jr = 0
    elif(int(JobRole) == 6):
        health_jr = 0
        hr_jr = 0
        lt_jr =0
        man_jr = 0
        md_jr = 0
        rd_jr = 1
        rs_jr = 0
        se_jr = 0
        sr_jr = 0
    elif(int(JobRole) == 7):
        health_jr = 0
        hr_jr = 0
        lt_jr =0
        man_jr = 0
        md_jr = 0
        rd_jr = 0
        rs_jr = 1
        se_jr = 0
        sr_jr = 0
    elif(int(JobRole) == 8):
        health_jr = 0
        hr_jr = 0
        lt_jr =0
        man_jr = 0
        md_jr = 0
        rd_jr = 0
        rs_jr = 0
        se_jr = 1
        sr_jr = 0
    else:
        health_jr = 0
        hr_jr = 0
        lt_jr =0
        man_jr = 0
        md_jr = 0
        rd_jr = 0
        rs_jr = 0
        se_jr = 0
        sr_jr = 1
    MaritalStatusradio = req.get('MaritalStatusradio')
    if(int(MaritalStatusradio) == 1):
        div = 1
        mar = 0
        sing = 0
    elif(int(MaritalStatusradio) ==2):
        div = 0
        mar = 1
        sing = 0
    else:
        div = 0
        mar = 0
        sing = 1
    print(age,att,dRate,dist,edu,envradio,Genderradio,hrr,JIradio,JLradio,JSradio,
          MI,Mrate,NumComp,Overtimeradio,PercentHike,RSradio,StockOLradio,
          WorkingYrs,TTLY,WLbalanceradio,YrsComp,YrsCurrent,YrsPromotion,YrsCurrManager,
          travel_r,travel_freq,Non_travel,sales,RnD,hRes,ls_field,med_field,fm_field,
          td_field,hr_field,o_field,rs_jr,lt_jr,se_jr,md_jr,health_jr,sr_jr,rd_jr,
          man_jr,hr_jr,sing,mar,div)
    body_list = [age,att,dRate,dist,edu,envradio,Genderradio,hrr,JIradio,JLradio,JSradio,
          MI,Mrate,NumComp,Overtimeradio,PercentHike,RSradio,StockOLradio,
          WorkingYrs,TTLY,WLbalanceradio,YrsComp,YrsCurrent,YrsPromotion,YrsCurrManager,
          travel_r,travel_freq,Non_travel,sales,RnD,hRes,ls_field,med_field,fm_field,
          td_field,hr_field,o_field,rs_jr,lt_jr,se_jr,md_jr,health_jr,sr_jr,rd_jr,
          man_jr,hr_jr,sing,mar,div]
    body_string = ",".join([str(body) for body in body_list])
    print(body_string)
    data_body = json.dumps({"body": body_string})
    print(type(body_string),type(data_body))
    print(data_body)
    r = requests.post(url = URL, data = data_body)
    print(r)
    print(r.status_code, r.reason, r.text)
    r_text  = r.text.strip('\"')
    if(r_text == "Bad"):
        final_text = 'Rating : {}.Needs to improve a lot.'.format(r_text)
    elif(r_text == "Not Satisfactory"):
        final_text = 'Rating : {}. A lot of room for improvement.'.format(r_text)
    elif(r_text == "Satisfactory"):
        final_text = 'Rating : {}.There is still room for improvement.'.format(r_text)
    elif(r_text == "Good!"):
        final_text = 'Rating : {} Performance is above average!'.format(r_text)
    elif(r_text == "Great!"):
        final_text = 'Rating : {} Outstanding Performance!'.format(r_text)
    return render_template('index.html',final_text = final_text)

if __name__ == '__main__':
    app.run(debug =True)
    
