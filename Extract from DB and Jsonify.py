#!/usr/bin/env python
# coding: utf-8

# In[1]:


##dependencies
import psycopg2
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template
import json


# In[2]:


##pull data from postgres db
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "Health Insurance MarketPlace")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT * from public.clean_rate")
    records = cursor.fetchall()

    clean_rate_df = pd.DataFrame(records)


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# In[3]:


#drop records with values that can't be converted to int, rename columns
clean_rate_df = clean_rate_df[clean_rate_df[3] != '65 and over']
clean_rate_df = clean_rate_df[clean_rate_df[3] != 'Family Option']
clean_rate_df = clean_rate_df[clean_rate_df[3] != '0-20']
clean_rate_df.columns = ['State','IssuerID','PlanID','Age','IndividualRate']

clean_rate_df.head()


# In[4]:


## Find how many records were dropped
print(f" {100000 -clean_rate_df['Age'].count()} records were dropped")
print(f" {4568/10000}% of all records")


# In[5]:


## cast age as int to do math
clean_rate_df['Age'] = clean_rate_df['Age'].astype(int)


# In[6]:


## groupby state and find avg age
clean_rate_avg_age_df = clean_rate_df.groupby('State').mean()
clean_rate_avg_age_df = clean_rate_avg_age_df.reset_index()


# In[7]:


## create dictionaries to jsonify and hand off to js
clean_rate_avg_age = []
counter = 0
for plan in clean_rate_avg_age_df.iterrows():
    clean_rate_avg_age.append({'State':clean_rate_avg_age_df.iloc[counter,0],'Age':clean_rate_avg_age_df.iloc[counter,-1]})
    counter = counter +1


# In[8]:


##pull data from postgres db
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "Health Insurance MarketPlace")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    
    ##right now this points at new_healthsop 2018, it should either repeat for each year or target a combined db and add a year column
    cursor.execute("SELECT * from public.new_healthshop2018")
    records = cursor.fetchall()

    clean_rate_df = pd.DataFrame(records)


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# In[9]:


## drop unecessary columns and then label remaining columns
healthshop_2018_df = pd.DataFrame(records)
healthshop_2018_df = healthshop_2018_df.drop(columns= [2,5,6,7,9,10,11])
healthshop_2018_df.columns = ['State','FIPS','Metal','Issuer','Type']
healthshop_2018_df.head()


# In[10]:


##create groupbys to operate on
state_groupby = healthshop_2018_df.groupby('State')
FIPS_groupby = healthshop_2018_df.groupby('FIPS')
state_metal_groupby = healthshop_2018_df.groupby(['Metal','State'])
fips_metal_groupby = healthshop_2018_df.groupby(['Metal','FIPS'])
state_issuer_groupby = healthshop_2018_df.groupby(['Issuer','State'])
fips_issuer_groupby = healthshop_2018_df.groupby(['Issuer','FIPS'])
state_type_groupby = healthshop_2018_df.groupby(['Type','State'])
fips_type_groupby = healthshop_2018_df.groupby(['Type','FIPS'])


# In[23]:


#get count for each state and FIPS
state_count = state_groupby[['FIPS']].count()
#right now this is cast to a string because jsonify didn't like numpy results??
state_count['FIPS'] = state_count['FIPS'].astype(str) 
state_count = state_count.reset_index(drop=False)
state_count.columns = ['State','Count']

fips_count = FIPS_groupby[['Type']].count()
fips_count['Type'] = fips_count['Type'].astype(str)
fips_count = fips_count.reset_index(drop=False)
fips_count.columns = ['FIPS','Count']


# In[12]:


#get count for each metal type by state and FIPS
state_metal_count = state_metal_groupby[['FIPS']].count()
state_metal_count['FIPS'] = state_metal_count['FIPS'].astype(str)
state_metal_count = state_metal_count.reset_index(drop=False)
state_metal_count.columns = ['Metal','State','Count']

fips_metal_count = fips_metal_groupby[['State']].count()
fips_metal_count['State'] = fips_metal_count['State'].astype(str)
fips_metal_count = fips_metal_count.reset_index(drop=False)
fips_metal_count.columns = 'Metal','FIPS','Count'


# In[21]:


#get count for each issuer by state and FIPS
state_issuer_count = state_issuer_groupby[['FIPS']].count()
state_issuer_count[['FIPS']] = state_issuer_count[['FIPS']].astype(str)
state_issuer_count = state_issuer_count.reset_index(drop=False)
state_issuer_count.columns = ['Issuer','State','Count']

fips_issuer_count = fips_issuer_groupby[['State']].count()
fips_issuer_count[['State']] = fips_issuer_count[['State']].astype(str)
fips_issuer_count = fips_issuer_count.reset_index(drop=False)
fips_issuer_count.columns = ['Issuer','FIPS','Count']


# In[27]:


#get count of plan type for each state and FIPS
state_type_count = state_type_groupby[['FIPS']].count()
state_type_count['FIPS'] = state_type_count['FIPS'].astype(str)
state_type_count = state_type_count.reset_index(drop=False)
state_type_count.columns = ['Type','State','Count']

fips_type_count = fips_type_groupby[['State']].count()
fips_type_count['State'] = fips_type_count['State'].astype(str)
fips_type_count = fips_type_count.reset_index(drop=False)
fips_type_count.columns = ['Type','FIPS','Count']


# In[15]:


#turn dfs into dicts for jsonification
state_count_obs = []
counter = 0
for plan in state_count.iterrows():
    state_count_obs.append({'State':state_count.iloc[counter,0],'Count':state_count.iloc[counter,-1]})
    counter = counter +1

fips_count_obs = []
counter = 0
for plan in fips_count.iterrows():
    fips_count_obs.append({'FIPS':fips_count.iloc[counter,0],'Count':fips_count.iloc[counter,-1]})
    counter = counter +1

state_metal_obs = []
counter = 0
for plan in state_metal_count.iterrows():
    state_metal_obs.append({'State':state_metal_count.iloc[counter,1],'Metal':state_metal_count.iloc[counter,0],'Count':state_metal_count.iloc[counter,-1]})
    counter = counter +1
    
fips_metal_obs = []
counter = 0
for plan in fips_metal_count.iterrows():
    fips_metal_obs.append({'FIPS':fips_metal_count.iloc[counter,1],'Metal':fips_metal_count.iloc[counter,0],'Count':fips_metal_count.iloc[counter,-1]})
    counter = counter +1

state_issuer_obs = []
counter = 0
for plan in state_issuer_count.iterrows():
    state_issuer_obs.append({'State':state_issuer_count.iloc[counter,1],'Count':state_issuer_count.iloc[counter,-1], 'Issuer':state_issuer_count.iloc[counter,0]})
    counter = counter +1
    
fips_issuer_obs = []
counter = 0
for plan in fips_issuer_count.iterrows():
    fips_issuer_obs.append({'FIPS':fips_issuer_count.iloc[counter,1],'Count':fips_issuer_count.iloc[counter,-1], 'Issuer':fips_issuer_count.iloc[counter,0]})
    counter = counter +1
    
state_type_obs = []
counter = 0
for plan in state_type_count.iterrows():
    state_type_obs.append({'State':state_type_count.iloc[counter,1],'Count':state_type_count.iloc[counter,-1], 'Type':state_type_count.iloc[counter,0]})
    counter = counter +1
    
fips_type_obs = []
counter = 0
for plan in fips_type_count.iterrows():
    fips_type_obs.append({'FIPS':fips_type_count.iloc[counter,1],'Count':fips_type_count.iloc[counter,-1], 'Type':fips_type_count.iloc[counter,0]})
    counter = counter +1


# In[18]:


clean_rate_avg_age


# In[17]:


state_count_obs


# In[ ]:


app = Flask(__name__)

@app.route("/")
def welcome():
    return 'Available routes: /avg_age, /state_count, /fips_count, /state_metal, /fips_metal, /state_issuer, /state_type, /fips_type'

@app.route("/avg_age")
def avgAge():
    return jsonify(clean_rate_avg_age)

@app.route("/state_count")
def stateCount():
    return jsonify(state_count_obs)

@app.route("/fips_count")
def fipsCount():
    return jsonify(fips_count_obs)

@app.route("/state_metal")
def stateMetal():
    return jsonify(state_metal_obs)

@app.route("/fips_metal")
def fipsMetal():
    return jsonify(fips_metal_obs)

@app.route("/state_issuer")
def stateIssuer():
    return jsonify(state_issuer_obs)

@app.route("/fips_issuer")
def fipsIssuer():
    return jsonify(fips_issuer_obs)

@app.route("/state_type")
def stateType():
    return jsonify(state_type_obs)

@app.route("/fips_type")
def fipsType():
    return jsonify(fips_type_obs)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




