import riot_api_class
from flask import Flask, render_template, request
import requests
import json


api_key="RGAPI-e057b103-1f67-423e-9928-fb517970f613"


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Homepage.html")

@app.route('/summoner')
def summoner():
    return render_template("Summoner_Profile.html")

@app.route('/returnSummoner',methods=['POST'])
def my_form_get():
    ign = request.form['sname']
    if(ign == ""):
        return render_template("Summoner_Profile.html")
    else:
        region = request.form['rname']

        input_region="na1"
        if(region == "EUNE"):
            input_region="eun1"
        if(region == "EUW"):
            input_region="euw1"
        
        currAPI = riot_api_class.Riot_API(api_key,input_region)
        currSumm = currAPI.get_summoner(ign)#returns a Summoner Object
        if(currSumm != None):
            temp_sd="Unranked"
            temp_fl="Unranked"
            temp_tt="Unranked"

            sd_check=False
            fl_check=False
            tt_check=False
            for i in currSumm.getRank():
                if("RANKED_SOLO_5x5" in i):
                    temp_sd=i.replace("RANKED_SOLO_5x5","")
                    sd_check=True
                if("RANKED_FLEX_SR" in i):
                    temp_fl=i.replace("RANKED_FLEX_SR","")
                    fl_check=True
                if("RANKED_FLEX_TT" in i):
                    temp_tt=i.replace("RANKED_FLEX_TT","")
                    tt_check=True

            temp_count_sd="NaN"
            temp_count_fl="NaN"
            temp_count_tt="NaN"

            splitS = ["0","0","0"]
            splitF = ["0","0","0"]
            splitT = ["0","0","0"]

            spercent = 0
            fpercent = 0
            tpercent = 0
            for i in currSumm.getCounts():
                if("RANKED_SOLO_5x5_" in i):
                    temp_count_sd=i.replace("RANKED_SOLO_5x5_","")
                    splitS = temp_count_sd.split("_")
                    spercent = round((int(splitS[0])/(int(splitS[0])+int(splitS[1])))*100)
                
                if("RANKED_FLEX_SR_" in i):
                    temp_count_fl=i.replace("RANKED_FLEX_SR_","")
                    splitF = temp_count_fl.split("_")
                    fpercent = round((int(splitF[0])/(int(splitF[0])+int(splitF[1])))*100)
                
                if("RANKED_FLEX_TT_" in i):
                    temp_count_tt=i.replace("RANKED_FLEX_TT_","")
                    splitT = temp_count_tt.split("_")
                    tpercent = round((int(splitT[0])/(int(splitT[0])+int(splitT[1])))*100)
                
            
            
            
            

                    
            
           
                
            return render_template("returnSummoner.html",
                                   sname=currSumm.ign,
                                   region_name=region,
                                   div_rank1=temp_sd,
                                   div_rank2=temp_fl,
                                   div_rank3=temp_tt,
                                   count_solo_percent=spercent,
                                   count_solo_win=splitS[0],
                                   count_solo_loss=splitS[1],
                                   count_fl_percent=fpercent,
                                   count_fl_win=splitF[0],
                                   count_fl_loss=splitF[1],
                                   count_tt_percent=tpercent,
                                   count_tt_win=splitT[0],
                                   count_tt_loss=splitT[1])
        else:
            return render_template("Summoner_Profile.html")
    
   
#@app.errorhandler(Exception)
#def exception_handler(error):
    #if(str(error)=="'name'" or str(error)=="list index out of range"):
        #return "Summoner Name Doesn't Exist"
    #else:
        #return str(error)

#app.run(host="127.0.0.1",port=5000,debug=True)
if __name__=="__main__":
    app.run(debug=True)



