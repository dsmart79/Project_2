#!/usr/bin/env python
# coding: utf-8

# In[38]:


##dependencies
import psycopg2
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template
import json


# In[42]:


##pull data from postgres db
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "Project 2")
    cursor = connection.cursor()

    cursor.execute("SELECT * from public.clean_rate")
    records = cursor.fetchall()

    clean18_rate_df = pd.DataFrame(records)


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()


# In[43]:


#drop records with values that can't be converted to int, rename columns
clean18_rate_df = clean18_rate_df[clean18_rate_df[3] != '65 and over']
clean18_rate_df = clean18_rate_df[clean18_rate_df[3] != 'Family Option']
clean18_rate_df = clean18_rate_df[clean18_rate_df[3] != '0-20']
clean18_rate_df.columns = ['State','IssuerID','PlanID','Age','IndividualRate']

clean18_rate_df.head()


# In[50]:


## Find how many records were dropped
print(f" {100000 - clean18_rate_df['Age'].count()} records were dropped")
print(f" {4568/10000}% of all records")


# In[51]:


## cast age as int to do math
clean18_rate_df['Age'] = clean18_rate_df['Age'].astype(int)


# In[52]:


## groupby state and find avg age
clean18_rate_avg_age_df = clean18_rate_df.groupby('State').mean()
clean18_rate_avg_age_df = clean18_rate_avg_age_df.reset_index()


# In[72]:


## create dictionaries to jsonify and hand off to js
clean18_rate_avg_age = []
counter = 0
for plan in clean18_rate_avg_age_df.iterrows():
    clean18_rate_avg_age.append({'State':clean18_rate_avg_age_df.iloc[counter,0],'Age':clean18_rate_avg_age_df.iloc[counter,-1]})
    counter = counter +1


# In[73]:


##pull data from postgres db
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "Project 2")
    cursor = connection.cursor()

    
    ##right now this points at new_healthsop 2018, it should either repeat for each year or target a combined db and add a year column
    cursor.execute("SELECT * from public.new_healthshop2018")
    records = cursor.fetchall()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()


# In[74]:


## drop unecessary columns and then label remaining columns
healthshop_2018_df = pd.DataFrame(records)
healthshop_2018_df = healthshop_2018_df.drop(columns= [2,5,6,7,9,10,11])
healthshop_2018_df.columns = ['State','FIPS','Metal','Issuer','Type']
healthshop_2018_df.count()


# In[75]:


##create groupbys to operate on
state18_groupby = healthshop_2018_df.groupby('State')
FIPS18_groupby = healthshop_2018_df.groupby('FIPS')
state18_metal_groupby = healthshop_2018_df.groupby(['Metal','State'])
fips18_metal_groupby = healthshop_2018_df.groupby(['Metal','FIPS'])
state18_issuer_groupby = healthshop_2018_df.groupby(['Issuer','State'])
fips18_issuer_groupby = healthshop_2018_df.groupby(['Issuer','FIPS'])
state18_type_groupby = healthshop_2018_df.groupby(['Type','State'])
fips18_type_groupby = healthshop_2018_df.groupby(['Type','FIPS'])


# In[76]:


#get count for each state and FIPS
state18_count = state18_groupby[['FIPS']].count()
#right now this is cast to a string because jsonify didn't like numpy results??
state18_count['FIPS'] = state18_count['FIPS'].astype(str) 
state18_count = state18_count.reset_index(drop=False)
state18_count.columns = ['State','Count']

fips18_count = FIPS18_groupby[['Type']].count()
fips18_count['Type'] = fips18_count['Type'].astype(str)
fips18_count = fips18_count.reset_index(drop=False)
fips18_count.columns = ['FIPS','Count']


# In[77]:


#get count for each metal type by state and FIPS
state18_metal_count = state18_metal_groupby[['FIPS']].count()
state18_metal_count['FIPS'] = state18_metal_count['FIPS'].astype(str)
state18_metal_count = state18_metal_count.reset_index(drop=False)
state18_metal_count.columns = ['Metal','State','Count']

fips18_metal_count = fips18_metal_groupby[['State']].count()
fips18_metal_count['State'] = fips18_metal_count['State'].astype(str)
fips18_metal_count = fips18_metal_count.reset_index(drop=False)
fips18_metal_count.columns = 'Metal','FIPS','Count'


# In[78]:


#get count for each issuer by state and FIPS
state18_issuer_count = state18_issuer_groupby[['FIPS']].count()
state18_issuer_count[['FIPS']] = state18_issuer_count[['FIPS']].astype(str)
state18_issuer_count = state18_issuer_count.reset_index(drop=False)
state18_issuer_count.columns = ['Issuer','State','Count']

fips18_issuer_count = fips18_issuer_groupby[['State']].count()
fips18_issuer_count[['State']] = fips18_issuer_count[['State']].astype(str)
fips18_issuer_count = fips18_issuer_count.reset_index(drop=False)
fips18_issuer_count.columns = ['Issuer','FIPS','Count']


# In[79]:


#get count of plan type for each state and FIPS
state18_type_count = state18_type_groupby[['FIPS']].count()
state18_type_count['FIPS'] = state18_type_count['FIPS'].astype(str)
state18_type_count = state18_type_count.reset_index(drop=False)
state18_type_count.columns = ['Type','State','Count']

fips18_type_count = fips18_type_groupby[['State']].count()
fips18_type_count['State'] = fips18_type_count['State'].astype(str)
fips18_type_count = fips18_type_count.reset_index(drop=False)
fips18_type_count.columns = ['Type','FIPS','Count']


# In[80]:


#turn dfs into dicts for jsonification
state18_count_obs = []
counter = 0
for plan in state18_count.iterrows():
    state18_count_obs.append({'State':state18_count.iloc[counter,0],'Count':state18_count.iloc[counter,-1]})
    counter = counter +1

fips18_count_obs = []
counter = 0
for plan in fips18_count.iterrows():
    fips18_count_obs.append({'FIPS':fips18_count.iloc[counter,0],'Count':fips18_count.iloc[counter,-1]})
    counter = counter +1

state18_metal_obs = []
counter = 0
for plan in state18_metal_count.iterrows():
    state18_metal_obs.append({'State':state18_metal_count.iloc[counter,1],'Metal':state18_metal_count.iloc[counter,0],'Count':state18_metal_count.iloc[counter,-1]})
    counter = counter +1
    
fips18_metal_obs = []
counter = 0
for plan in fips18_metal_count.iterrows():
    fips18_metal_obs.append({'FIPS':fips18_metal_count.iloc[counter,1],'Metal':fips18_metal_count.iloc[counter,0],'Count':fips18_metal_count.iloc[counter,-1]})
    counter = counter +1

state18_issuer_obs = []
counter = 0
for plan in state18_issuer_count.iterrows():
    state18_issuer_obs.append({'State':state18_issuer_count.iloc[counter,1],'Count':state18_issuer_count.iloc[counter,-1], 'Issuer':state18_issuer_count.iloc[counter,0]})
    counter = counter +1
    
fips18_issuer_obs = []
counter = 0
for plan in fips18_issuer_count.iterrows():
    fips18_issuer_obs.append({'FIPS':fips18_issuer_count.iloc[counter,1],'Count':fips18_issuer_count.iloc[counter,-1], 'Issuer':fips18_issuer_count.iloc[counter,0]})
    counter = counter +1
    
state18_type_obs = []
counter = 0
for plan in state18_type_count.iterrows():
    state18_type_obs.append({'State':state18_type_count.iloc[counter,1],'Count':state18_type_count.iloc[counter,-1], 'Type':state18_type_count.iloc[counter,0]})
    counter = counter +1
    
fips18_type_obs = []
counter = 0
for plan in fips18_type_count.iterrows():
    fips18_type_obs.append({'FIPS':fips18_type_count.iloc[counter,1],'Count':fips18_type_count.iloc[counter,-1], 'Type':fips18_type_count.iloc[counter,0]})
    counter = counter +1


# In[81]:


clean18_rate_avg_age


# In[82]:


state18_count_obs


# In[83]:


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/data")
def data():
    return render_template("data.html")
    
@app.route("/conclusions")
def conclusions():
    return render_template("conclusions.html")
    
@app.route("/info")
def welcome():
    return 'Available routes: /avg_age, /state_count, /fips_count, /state_metal, /fips_metal, /state_issuer, /state_type, /fips_type'

@app.route("/avg_age18")
def avgAge():
    return jsonify(clean18_rate_avg_age)

@app.route("/state_count18")
def stateCount():
    return jsonify(state18_count_obs)

@app.route("/fips_count18")
def fipsCount():
    return jsonify(fips18_count_obs)

@app.route("/state18_metal18")
def stateMetal():
    return jsonify(state18_metal_obs)

@app.route("/fips_metal18")
def fipsMetal():
    return jsonify(fips18_metal_obs)

@app.route("/state_issuer18")
def stateIssuer():
    return jsonify(state18_issuer_obs)

@app.route("/fips_issuer18")
def fipsIssuer():
    return jsonify(fips18_issuer_obs)

@app.route("/state_type18")
def stateType():
    return jsonify(state18_type_obs)

@app.route("/fips_type18")
def fipsType():
    return jsonify(fips18_type_obs)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




