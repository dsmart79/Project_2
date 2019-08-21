#!/usr/bin/env python
# coding: utf-8

<<<<<<< HEAD
# In[1]:
=======
# In[87]:
>>>>>>> master


# Imports
import pandas as pd
import os
import sqlite3
from sqlite3 import Error
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import sqlalchemy as db


# ## CSV to DataFrame

<<<<<<< HEAD
# In[2]:
=======
# In[88]:
>>>>>>> master


# import CSVs 
health15_df = pd.read_csv('./CSVs/Health_Ins_2015.csv')
health16_df = pd.read_csv('./CSVs/Health_Ins_2016.csv')
health17_df = pd.read_csv('./CSVs/Health_Ins_2017.csv')
health18_df = pd.read_csv('./CSVs/Health_Ins_2018.csv')
iowa_counties = pd.read_csv('./CSVs/IA_counties.csv')
<<<<<<< HEAD


# In[3]:
=======
ky_counties = pd.read_csv('./CSVs/KY_FIPS.csv')


# In[89]:
>>>>>>> master


# rename columns
health15_df = health15_df[['State Code','County Name','Metal Level','Issuer Name','Plan Type']]
health16_df = health16_df[['State Code','County Name','Metal Level','Issuer Name','Plan Type']]


<<<<<<< HEAD
# In[4]:
=======
# In[90]:
>>>>>>> master


#lowercase county names for lookups
health15_df['County Name'] = health15_df['County Name'].str.lower()
health16_df['County Name'] = health16_df['County Name'].str.lower()
health17_df['County Name'] = health17_df['County Name'].str.lower()
health18_df['County Name'] = health18_df['County Name'].str.lower()


<<<<<<< HEAD
# In[5]:
=======
# In[91]:


ky_counties['County'] = ky_counties['County'].str.lower()
ky_counties['County'] = ky_counties['County'].str.replace('-','')
ky_counties['County'] = ky_counties['County'].str.replace(' ','')
ky_counties['Lookup'] = (ky_counties['County'] + ky_counties['State'])
ky_counties = ky_counties[['Lookup','FIPS']]
ky_counties.columns = ['Lookup','fips']


# In[92]:
>>>>>>> master


#combine state codes and county names for lookups
health15_df['Lookup'] = (health15_df['State Code'] + health15_df['County Name']).astype(str)
health15_df['Lookup'] = health15_df['Lookup'].str.replace('-','')
health15_df['Lookup'] = health15_df['Lookup'].str.replace(' ','')
health16_df['Lookup'] = (health16_df['State Code'] + health16_df['County Name']).astype(str)
health16_df['Lookup'] = health16_df['Lookup'].str.replace('-','')
health16_df['Lookup'] = health16_df['Lookup'].str.replace(' ','')
health17_df['Lookup'] = (health17_df['State Code'] + health17_df['County Name']).astype(str)
health17_df['Lookup'] = health17_df['Lookup'].str.replace('-','')
health17_df['Lookup'] = health17_df['Lookup'].str.replace(' ','')
health18_df['Lookup'] = (health18_df['State Code'] + health18_df['County Name']).astype(str)
health18_df['Lookup'] = health18_df['Lookup'].str.replace('-','')
health18_df['Lookup'] = health18_df['Lookup'].str.replace(' ','')


<<<<<<< HEAD
# In[6]:
=======
# In[93]:
>>>>>>> master


lookup17 = health17_df[['Lookup','FIPS County Code']]
lookup17.columns = ['Lookup', 'fips']


<<<<<<< HEAD
# In[7]:
=======
# In[94]:
>>>>>>> master


#build lookup table from 2017 fips info
unique_lookup = lookup17.Lookup.unique()
unique_fips = lookup17.fips.unique()
lookup_table = []

counter = 0
while counter < len(unique_lookup):
    fips_lookups = {'fips':unique_fips[counter],'Lookup':unique_lookup[counter]}
    lookup_table.append(fips_lookups)
    counter = counter + 1
    
lookup_table = pd.DataFrame(lookup_table)


<<<<<<< HEAD
# In[8]:
=======
# In[95]:
>>>>>>> master


#add missing counties to lookup table
lookup_table = lookup_table.append({'Lookup':'IAclinton','fips':'19045'},ignore_index=True)
lookup_table = lookup_table.append({'Lookup':'IAclark','fips':'19039'},ignore_index=True)
lookup_table = lookup_table.append({'Lookup':'IAchickasaw','fips':'19037'},ignore_index=True)
lookup_table = lookup_table.append({'Lookup':'IAcherokee','fips':'19035'},ignore_index=True)
lookup_table = lookup_table.append({'Lookup':'IAcerrogordo','fips':'19033'},ignore_index=True)
lookup_table = lookup_table.append({'Lookup':'IAcedar','fips':'19031'},ignore_index=True)
lookup_table = lookup_table.append({'Lookup':'IAcass','fips':'19029'},ignore_index=True)
lookup_table = lookup_table.append(iowa_counties)
<<<<<<< HEAD


# In[9]:
=======
lookup_table = lookup_table.append(ky_counties)


# In[96]:
>>>>>>> master


#merge in lookup table to 15 and 16 data to add fips column
l_15 = health15_df.merge(lookup_table,on='Lookup',how='left')
l_16 = health16_df.merge(lookup_table,on='Lookup',how='left')
<<<<<<< HEAD


# In[10]:
=======
l_17 = health17_df.merge(lookup_table,on='Lookup',how='left')
l_18 = health18_df.merge(lookup_table,on='Lookup',how='left')


# In[97]:
>>>>>>> master


#remove lookup column and standardize order and names
health15_df = l_15[['State Code','County Name','Metal Level','Issuer Name','Plan Type','fips']]
health15_df.columns = ['State Code','County Name','Metal Level','Issuer Name','Plan Type','Fips']
health16_df = l_16[['State Code','County Name','Metal Level','Issuer Name','Plan Type','fips']]
health16_df.columns = ['State Code','County Name','Metal Level','Issuer Name','Plan Type','Fips']
<<<<<<< HEAD
health17_df = health17_df[['State Code','County Name','Metal Level','Issuer Name','Plan Type','FIPS County Code']]
health17_df.columns = ['State Code','County Name','Metal Level','Issuer Name','Plan Type','Fips']
health18_df = health18_df[['State Code','County Name','Metal Level','Issuer Name','Plan Type','FIPS County Code']]
health18_df.columns = ['State Code','County Name','Metal Level','Issuer Name','Plan Type','Fips']


# In[11]:
=======
health17_df = l_17[['State Code','County Name','Metal Level','Issuer Name','Plan Type','fips']]
health17_df.columns = ['State Code','County Name','Metal Level','Issuer Name','Plan Type','Fips']
health18_df = l_18[['State Code','County Name','Metal Level','Issuer Name','Plan Type','fips']]
health18_df.columns = ['State Code','County Name','Metal Level','Issuer Name','Plan Type','Fips']


# In[98]:
>>>>>>> master


#Write dfs out as objects to add to db
pointer = health15_df
counter = 0
values_list15 = []
for record in pointer.iterrows():
    values_list15.append({'State Code':pointer['State Code'][counter], 'County Name':pointer['County Name'][counter], 'Metal Level':pointer['Metal Level'][counter],'Issuer Name':pointer['Issuer Name'][counter],'Plan Type':pointer['Plan Type'][counter],'FIPS':pointer['Fips'][counter]})
    counter = counter + 1
    
pointer = health16_df
counter = 0
values_list16 = []
for record in pointer.iterrows():
    values_list16.append({'State Code':pointer['State Code'][counter], 'County Name':pointer['County Name'][counter], 'Metal Level':pointer['Metal Level'][counter],'Issuer Name':pointer['Issuer Name'][counter],'Plan Type':pointer['Plan Type'][counter],'FIPS':pointer['Fips'][counter]})
    counter = counter + 1
    
pointer = health17_df
counter = 0
values_list17 = []
for record in pointer.iterrows():
    values_list17.append({'State Code':pointer['State Code'][counter], 'County Name':pointer['County Name'][counter], 'Metal Level':pointer['Metal Level'][counter],'Issuer Name':pointer['Issuer Name'][counter],'Plan Type':pointer['Plan Type'][counter],'FIPS':pointer['Fips'][counter]})
    counter = counter + 1
    
pointer = health18_df
counter = 0
values_list18 = []
for record in pointer.iterrows():
    values_list18.append({'State Code':pointer['State Code'][counter], 'County Name':pointer['County Name'][counter], 'Metal Level':pointer['Metal Level'][counter],'Issuer Name':pointer['Issuer Name'][counter],'Plan Type':pointer['Plan Type'][counter],'FIPS':pointer['Fips'][counter]})
    counter = counter + 1


<<<<<<< HEAD
# In[12]:
=======
# In[99]:
>>>>>>> master


#Create sqlite DB
engine = create_engine('sqlite:///static/health_plans.sqlite')

connection = engine.connect()
metadata = db.MetaData()

h15 = db.Table('h15', metadata,
               db.Column('State Code', db.String(255)),
               db.Column('County Name', db.String(255)),
               db.Column('Metal Level', db.String(255)),
               db.Column('Issuer Name',db.String(255)),
               db.Column('Plan Type',db.String(255)),
               db.Column('FIPS',db.Integer())
              )

h16 = db.Table('h16', metadata,
               db.Column('State Code', db.String(255)),
               db.Column('County Name', db.String(255)),
               db.Column('Metal Level', db.String(255)),
               db.Column('Issuer Name',db.String(255)),
               db.Column('Plan Type',db.String(255)),
               db.Column('FIPS',db.Integer())
              )

h17 = db.Table('h17', metadata,
               db.Column('State Code', db.String(255)),
               db.Column('County Name', db.String(255)),
               db.Column('Metal Level', db.String(255)),
               db.Column('Issuer Name',db.String(255)),
               db.Column('Plan Type',db.String(255)),
               db.Column('FIPS',db.Integer())
              )

h18 = db.Table('h18', metadata,
               db.Column('State Code', db.String(255)),
               db.Column('County Name', db.String(255)),
               db.Column('Metal Level', db.String(255)),
               db.Column('Plan Type',db.String(255)),
               db.Column('Issuer Name',db.String(255)),
               db.Column('FIPS',db.Integer())
              )

metadata.create_all(engine)


<<<<<<< HEAD
# In[13]:
=======
# In[100]:
>>>>>>> master


#make db connections and write in objects for each year
engine = db.create_engine('sqlite:///static/health_plans.sqlite')
connection = engine.connect()
metadata = db.MetaData()
h15 = db.Table('h15', metadata, autoload=True,autoload_with=engine)

query = db.insert(h15)
ResultProxy = connection.execute(query,values_list15)

engine = db.create_engine('sqlite:///static/health_plans.sqlite')
connection = engine.connect()
metadata = db.MetaData()
h16 = db.Table('h16', metadata, autoload=True,autoload_with=engine)

query = db.insert(h16)
ResultProxy = connection.execute(query,values_list16)

engine = db.create_engine('sqlite:///static/health_plans.sqlite')
connection = engine.connect()
metadata = db.MetaData()
h17= db.Table('h17', metadata, autoload=True,autoload_with=engine)

query = db.insert(h17)
ResultProxy = connection.execute(query,values_list17)

engine = db.create_engine('sqlite:///static/health_plans.sqlite')
connection = engine.connect()
metadata = db.MetaData()

h18 = db.Table('h18', metadata, autoload=True,autoload_with=engine)
query = db.insert(h18)
ResultProxy = connection.execute(query,values_list18)


# In[ ]:




