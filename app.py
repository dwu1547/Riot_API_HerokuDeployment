import riot_api_class
from flask import Flask, render_template, request
import requests
import json


api_key="RGAPI-7c7a4fde-7a19-4bc9-8e03-87af9d007f3a"


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
                if("_SOLO_" in i):
                    temp_sd=i.replace("RANKED_SOLO_5x5","")
                    sd_check=True
                if("_FLEX_" in i and "_FLEX_TT" not in i):
                    temp_fl=i.replace("RANKED_FLEX_SR","")
                    fl_check=True
                if("FLEX_TT" in i):
                    temp_tt=i.replace("RANKED_FLEX_TT","")
                    tt_check=True
                    
            
           
                
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

#app.run(host="127.0.0.1",port=5000,debug=True)
if __name__=="__main__":
    app.run(debug=True)



