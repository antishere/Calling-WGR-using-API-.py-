#need to use http.client
import http.client

#creates a connection to rapidapi
conn = http.client.HTTPSConnection("live-golf-data.p.rapidapi.com")

headers = {
    # input personal key 
    'X-RapidAPI-Key': "your_key_generated_from_rapidapi",
    'X-RapidAPI-Host': "live-golf-data.p.rapidapi.com"
}

conn.request("GET", "/stats?year=2023&statId=186", headers=headers) #change year and statID to get different week
res = conn.getresponse()
data = res.read()

#we get a dictionary but in string form
wgr=(data.decode("utf-8"))
#need to use eval() to convert it from a string to a data item (lists and dictionaries)
wgr=eval(wgr)


#----we can now refer to wgr as a dictionary and call upon each aspect------#
# the live golf data api has 5 main sections, the hardest one to undestand and reference is the rankings
# this is due to the rankings having 300 players in a list format eg.  wgr["rankings"][0] would return a dictionary about scottie scheffler
#the format of said dictionary is this {"lastname":"Scheffler", firstname:"Scottie","rank":{"$numberInt":"1"}, etc:etc}


#if we wanted to return the name of world number 2 we would do
print(wgr["rankings"][1]['lastName'])
#this is the same for firstName
#for the other attributes they would return another dictionary
print(wgr["rankings"][1]['avgPoints'])
#above would return {'$numberDouble:'8.63'} we could get the number on it's own by adding ['$numberDouble'] after ['avgPoints']

#the other attributes for each player are : rank, previousRank, events, totalPoints, pointsLost, pointsGained


#below is an example displaying the top 10 golfers as of this week
i=0
print("-----WGR top 10------")
for _ in range(10):
    print(i+1,".",wgr["rankings"][i]["firstName"],wgr["rankings"][i]["lastName"])
    i=i+1









