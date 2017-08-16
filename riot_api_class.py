import json
import requests #py -m pip install requests (python 3.6)

class Summoner(object):

    def __init__(self,ign,s_id,api_key,region):
        self.ign = ign
        self.id = s_id
        self.api_key = api_key
        self.region = region
        

    def getRank(self):
        rank_url = "https://" + self.region + ".api.riotgames.com/lol/league/v3/leagues/by-summoner/" + str(self.id) + "?api_key=" + self.api_key
        response = requests.get(rank_url)
        #print(response.json()[0]['queue'])
        #print(response.json()[0]['tier']) ###[0] is solo/duo [1] is flex ***assuming they have ranks in all 3 queues others they move up
        if(bool(response.json())== False):
            return "No Rank Available"
        else:
            rank=[]
            for i in response.json():
                
                for j in i['entries']:
                    if(j['playerOrTeamName'] == self.ign): ###comparision oeprator is case sensitve otherwise rank won't show
                        rank.append(str(i['queue'] + i['tier'] + "_"+ j['rank']))
        return rank
            

class Riot_API(object):

    def __init__(self,api_key,region):
        self.api_key = api_key
        self.region = region
        
    def get_summoner(self,ign):
        summoner_name = ign 
        url = "https://" + self.region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summoner_name + "?api_key=" + self.api_key
        response = requests.get(url)
        if(response.status_code == requests.codes.ok):
            sum_name_input = response.json()['name']
            sum_id_input = response.json()['id']
            entry = Summoner(sum_name_input,sum_id_input,self.api_key,self.region)
            return entry
        else:
            return 
