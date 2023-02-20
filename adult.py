import pymongo
import pandas as pd

hn=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','captial-loss','hours-per-week','native-country']
df = pd.read_csv("Adult.csv", index_col=False, names=hn)

data = df.to_dict(orient='records')

#Url to connect with MongoDB Server
client = pymongo.MongoClient("mongodb+srv://cibisaran:Omnamashiv55@cluster0.utbhaiw.mongodb.net/?retryWrites=true&w=majority")

#Create your Database
db = client["Census_Income"]

#Create a collection 
#coll = db["Adult"]
db.Adult.insert_many(data)

