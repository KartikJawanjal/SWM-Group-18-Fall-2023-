import pandas as pd
import datetime
print("Reading Amazon chart")
applechart=pd.read_csv("/home/kjawanja/Semantic_Web_Mining/CHARTS/CHARTS/AMAZON60.csv",header=None)
print("Reading Amazon Charts")
amazonchart=pd.read_csv("/home/kjawanja/Semantic_Web_Mining/CHARTS/CHARTS/AMAZON60.csv",header=None)
print("Reading Data")
appledata=pd.read_csv("/home/kjawanja/Semantic_Web_Mining/NewAmazondata.csv")
print("Done")
applechart[0]=pd.to_datetime(applechart[0], format="%Y.%m.%d")
print(type(applechart[0][0]))
def timeConvert(time):
  value=datetime.datetime.strptime(time,'%H:%M').time()
  return value
def timeConvert1(time):
  value=datetime.datetime.strptime(time,'%H:%M:%S').time()
  return value
def dateConvert(date):
  value=datetime.datetime.strptime(date,"%Y-%m-%d").date()
  return value

applechart[1]=applechart[1].apply(timeConvert)
print(type(applechart[1][0]))
applechart.columns=['Date',"Time","Open","High","Low","Close","Volume"]
for i in range(len(appledata)):
  appledataTime= timeConvert1(appledata.loc[i].Time)
  appledataDate=dateConvert(appledata.loc[i].Date)
 
  
  for j in range(len(applechart)):
    if applechart.loc[j].Date.date()==appledataDate:
      k=j
      break

  if appledataTime<timeConvert("13:30"):
    if applechart.loc[k-1].Open<applechart.loc[k].Open and k<=4173:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
  elif timeConvert1(appledata.loc[i].Time)>timeConvert("13:30") and timeConvert1(appledata.loc[i].Time)<timeConvert("14:30") and k<=4172:
    
    if applechart.loc[k].Open<applechart.loc[k+1].Open:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
  elif timeConvert1(appledata.loc[i].Time)>timeConvert("14:30") and timeConvert1(appledata.loc[i].Time)<timeConvert("15:30") and k<=4171:
    if applechart.loc[k+1].Open<applechart.loc[k+2].Open:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
  elif timeConvert1(appledata.loc[i].Time)>timeConvert("15:30") and timeConvert1(appledata.loc[i].Time)<timeConvert("16:30") and k<=4170:
    if applechart.loc[k+2].Open<applechart.loc[k+3].Open:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
  elif timeConvert1(appledata.loc[i].Time)>timeConvert("16:30") and timeConvert1(appledata.loc[i].Time)<timeConvert("17:30") and k<=4169:
    if applechart.loc[k+3].Open<applechart.loc[k+4].Open:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
  elif timeConvert1(appledata.loc[i].Time)>timeConvert("17:30") and timeConvert1(appledata.loc[i].Time)<timeConvert("18:30") and k<=4168:
    if applechart.loc[k+4].Open<applechart.loc[k+5].Open:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
  elif timeConvert1(appledata.loc[i].Time)>timeConvert("18:30") and timeConvert1(appledata.loc[i].Time)<timeConvert("19:30") and k<=4167:
    if applechart.loc[k+5].Open<applechart.loc[k+6].Open:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
  elif timeConvert1(appledata.loc[i].Time)>timeConvert("19:30") and timeConvert1(appledata.loc[i].Time)<timeConvert("20:30") and k<=4166:
    if applechart.loc[k+6].Open<applechart.loc[k+7].Open:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
  elif timeConvert1(appledata.loc[i].Time)>timeConvert("20:30") and timeConvert1(appledata.loc[i].Time)<timeConvert("21:30") and k<=4165:
    if applechart.loc[k+7].Open<applechart.loc[k+8].Open:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
  elif timeConvert1(appledata.loc[i].Time)>timeConvert("21:30") and timeConvert1(appledata.loc[i].Time)<timeConvert("22:30") and k<=4164:
    if applechart.loc[k+8].Open<applechart.loc[k+9].Open:
      appledata.loc[appledata.index[i],'Label']=1
    else:
      appledata.loc[appledata.index[i],'Label']=0
      
appledata.to_csv("Amazon(Hourly).csv")