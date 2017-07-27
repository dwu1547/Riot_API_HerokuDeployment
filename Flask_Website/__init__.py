import riot_api_class
from flask import Flask, render_template, request
import requests
import json


api_key="RGAPI-46dbc255-eda0-4cde-a8d7-65b28fb2a319"


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
            temp_sd="No Rank In This Queue Yet"
            temp_fl="No Rank In This Queue Yet"
            temp_tt="No Rank In This Queue Yet"
            for i in currSumm.getRank():
                if("_SOLO_" in i):
                    temp_sd=i.replace("RANKED_SOLO_5x5","")
                if("_FLEX_" in i and "_FLEX_TT" not in i):
                    temp_fl=i.replace("RANKED_FLEX_SR","")
                if("FLEX_TT" in i):
                    temp_tt=i.replace("RANKED_FLEX_TT","")
                    
            
           
                
            return render_template("returnSummoner.html",
                                   sname=currSumm.ign,
                                   region_name=region,
                                   div_rank1=temp_sd,
                                   div_rank2=temp_fl,
                                   div_rank3=temp_tt)
        else:
            return render_template("Summoner_Profile.html")
    
   
#@app.errorhandler(Exception)
#def exception_handler(error):
    #if(str(error)=="'name'" or str(error)=="list index out of range"):
        #return "Summoner Name Doesn't Exist"
    #else:
        #return str(error)


if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)



