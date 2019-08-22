#!/usr/bin/env python
# coding: utf-8

# In[45]:


#dependencies
import pandas as pd
import requests


# In[46]:


#read in geoJSON and state codes
states = pd.read_json('./static/geoJson/us_states.json')
state_codes = pd.read_csv('./CSVs/state_codes.csv')


# In[47]:


#Drop territories
state_list = state_codes[['State/District','Postal Code']][:51]

counter = 0

#Add state codes to geoJSON for easier lookups
for state in state_list.iterrows():
    state_code = state_list['Postal Code'][counter]
    states['features'][counter]['properties']['state_code'] = state_code
    counter = counter + 1
    
#PR gets a code so the program doesn't bomb later
states['features'][51]['properties']['state_code'] = 'PR'


# In[48]:


#JSON requests to api endpoint to get attributes to write to geoJSON
state_count15 = requests.get('http://localhost:5000/state_count15')
state_metal15 = requests.get('http://localhost:5000/state_metal15')
state_issuer15 = requests.get('http://localhost:5000/state_issuer15')
state_type15 = requests.get('http://localhost:5000/state_type15')

state_count16 = requests.get('http://localhost:5000/state_count16')
state_metal16 = requests.get('http://localhost:5000/state_metal16')
state_issuer16 = requests.get('http://localhost:5000/state_issuer16')
state_type16 = requests.get('http://localhost:5000/state_type16')

state_count17 = requests.get('http://localhost:5000/state_count17')
state_metal17 = requests.get('http://localhost:5000/state_metal17')
state_issuer17 = requests.get('http://localhost:5000/state_issuer17')
state_type17 = requests.get('http://localhost:5000/state_type17')

state_count18 = requests.get('http://localhost:5000/state_count18')
state_metal18 = requests.get('http://localhost:5000/state_metal18')
state_issuer18 = requests.get('http://localhost:5000/state_issuer18')
state_type18 = requests.get('http://localhost:5000/state_type18')


# In[49]:


#read the JSONs
state_count15 = state_count15.json()
state_metal15 = state_metal15.json()
state_issuer15 = state_issuer15.json()
state_type15 = state_type15.json()

state_count16 = state_count16.json()
state_metal16 = state_metal16.json()
state_issuer16 = state_issuer16.json()
state_type16 = state_type16.json()

state_count17 = state_count17.json()
state_metal17 = state_metal17.json()
state_issuer17 = state_issuer17.json()
state_type17 = state_type17.json()

state_count18 = state_count18.json()
state_metal18 = state_metal18.json()
state_issuer18 = state_issuer18.json()
state_type18 = state_type18.json()


# In[50]:


#turn Count back into an int
for dicts in state_count15: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#turn Count back into an int
for dicts in state_type15: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#turn Count back into an int
for dicts in state_issuer15: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#next year

#turn Count back into an int
for dicts in state_count16: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#turn Count back into an int
for dicts in state_type16: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#turn Count back into an int
for dicts in state_issuer16: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#next year

#turn Count back into an int
for dicts in state_count17: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#turn Count back into an int
for dicts in state_type17: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#turn Count back into an int
for dicts in state_issuer17: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#next year


#turn Count back into an int
for dicts in state_count18: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#turn Count back into an int
for dicts in state_type18: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#turn Count back into an int
for dicts in state_issuer18: 
    for keys in dicts: 
        dicts['Count'] = int(dicts['Count']) 
        
#next year


# In[51]:


#lookup the states that we have data for count data to the geoJSON

counter1=0
counter2=0

while counter1 < len(state_count15):
    lookup_state = state_count15[counter1]['State']
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties']['state_count15'] = state_count15[counter1]['Count']
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0

while counter1 < len(state_count16):
    lookup_state = state_count16[counter1]['State']
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties']['state_count16'] = state_count16[counter1]['Count']
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0

while counter1 < len(state_count17):
    lookup_state = state_count17[counter1]['State']
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties']['state_count17'] = state_count17[counter1]['Count']
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0

while counter1 < len(state_count18):
    lookup_state = state_count18[counter1]['State']
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties']['state_count18'] = state_count18[counter1]['Count']
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1


# In[52]:


#cast Count to int and break metal up into each type

source_var = state_metal15

year_data = pd.DataFrame(source_var)
year_data['Count'] = year_data['Count'].astype(int)
bronze15 = year_data.loc[year_data['Metal'] == 'Bronze'].reset_index(drop=True)
expanded_bronze15 = year_data.loc[year_data['Metal'] == 'Expanded Bronze'].reset_index(drop=True)
silver15=year_data.loc[year_data['Metal'] == 'Silver'].reset_index(drop=True)
gold15=year_data.loc[year_data['Metal'] == 'Gold'].reset_index(drop=True)
platinum15=year_data.loc[year_data['Metal'] == 'Platinum'].reset_index(drop=True)

source_var = state_metal16

year_data = pd.DataFrame(source_var)
year_data['Count'] = year_data['Count'].astype(int)
bronze16 = year_data.loc[year_data['Metal'] == 'Bronze'].reset_index(drop=True)
expanded_bronze16 = year_data.loc[year_data['Metal'] == 'Expanded Bronze'].reset_index(drop=True)
silver16=year_data.loc[year_data['Metal'] == 'Silver'].reset_index(drop=True)
gold16=year_data.loc[year_data['Metal'] == 'Gold'].reset_index(drop=True)
platinum16=year_data.loc[year_data['Metal'] == 'Platinum'].reset_index(drop=True)

source_var = state_metal17

year_data = pd.DataFrame(source_var)
year_data['Count'] = year_data['Count'].astype(int)
bronze17 = year_data.loc[year_data['Metal'] == 'Bronze'].reset_index(drop=True)
expanded_bronze17 = year_data.loc[year_data['Metal'] == 'Expanded Bronze'].reset_index(drop=True)
silver17=year_data.loc[year_data['Metal'] == 'Silver'].reset_index(drop=True)
gold17=year_data.loc[year_data['Metal'] == 'Gold'].reset_index(drop=True)
platinum17=year_data.loc[year_data['Metal'] == 'Platinum'].reset_index(drop=True)

source_var = state_metal18

year_data = pd.DataFrame(source_var)
year_data['Count'] = year_data['Count'].astype(int)
bronze18 = year_data.loc[year_data['Metal'] == 'Bronze'].reset_index(drop=True)
expanded_bronze18 = year_data.loc[year_data['Metal'] == 'Expanded Bronze'].reset_index(drop=True)
silver18=year_data.loc[year_data['Metal'] == 'Silver'].reset_index(drop=True)
gold18=year_data.loc[year_data['Metal'] == 'Gold'].reset_index(drop=True)
platinum18=year_data.loc[year_data['Metal'] == 'Platinum'].reset_index(drop=True)


# In[53]:


#write metal data to geoJSON

counter1=0
counter2=0

pointer = bronze15
field = 'bronze_state15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0

pointer = expanded_bronze15
field = 'expanded_bronze_15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1

counter1=0
counter2=0
        
pointer = silver15
field = 'silver_state15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1

counter1=0
counter2=0        

pointer = gold15
field = 'gold_state15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0        

pointer = platinum15
field = 'platinum_state15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
#next year

#write metal data to geoJSON

counter1=0
counter2=0

pointer = bronze16
field = 'bronze_state16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0

pointer = expanded_bronze16
field = 'expanded_bronze_16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1

counter1=0
counter2=0
        
pointer = silver16
field = 'silver_state16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1

counter1=0
counter2=0        

pointer = gold16
field = 'gold_state16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0        

pointer = platinum16
field = 'platinum_state16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
#next year

#write metal data to geoJSON

counter1=0
counter2=0

pointer = bronze17
field = 'bronze_state17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0

pointer = expanded_bronze17
field = 'expanded_bronze_17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1

counter1=0
counter2=0
        
pointer = silver17
field = 'silver_state17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1

counter1=0
counter2=0        

pointer = gold17
field = 'gold_state17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0        

pointer = platinum17
field = 'platinum_state17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
#next year

#write metal data to geoJSON

counter1=0
counter2=0

pointer = bronze18
field = 'bronze_state18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0

pointer = expanded_bronze18
field = 'expanded_bronze_18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1

counter1=0
counter2=0
        
pointer = silver18
field = 'silver_state18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1

counter1=0
counter2=0        

pointer = gold18
field = 'gold_state18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1=0
counter2=0        

pointer = platinum18
field = 'platinum_state18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
#next year


# In[54]:


#add issuer count to each state object for better naming in next step
for state in states.iterrows():
    state[1]['features']['properties']['issuer15_count'] = 0
    state[1]['features']['properties']['issuer16_count'] = 0
    state[1]['features']['properties']['issuer17_count'] = 0
    state[1]['features']['properties']['issuer18_count'] = 0


# In[55]:


#write out issuers and the number of plans by each issuer ot the geoJSON
counter1 = 0
counter2 = 0
counter3 = 0
pointer = state_issuer15
year = 15
issuer = pointer[counter1]['Issuer']


while counter1 < len(pointer):
    if pointer[counter1]['State'] == states['features'][counter2]['properties']['state_code']:
            issuer_count = states['features'][counter2]['properties'][f'issuer{year}_count']
            states['features'][counter2]['properties'][f'issuer{year}_{issuer_count}'] = pointer[counter1]['Count']
            states['features'][counter2]['properties'][f'issuer{year}_{issuer_count}_name'] = pointer[counter1]['Issuer']
            states['features'][counter2]['properties'][f'issuer{year}_count'] = states['features'][counter2]['properties'][f'issuer{year}_count'] + 1
            state_reference1 = pointer[counter1]['State']
            state_reference2 = pointer[counter1]['State']         
            counter2 = 0
            counter1 = counter1 + 1
            counter3 = counter3 + 1
            
    else:
        counter2 = counter2 + 1
        
#write out issuers and the number of plans by each issuer ot the geoJSON
counter1 = 0
counter2 = 0
counter3 = 0
pointer = state_issuer16
year = 16
issuer = pointer[counter1]['Issuer']


while counter1 < len(pointer):
    if pointer[counter1]['State'] == states['features'][counter2]['properties']['state_code']:
            issuer_count = states['features'][counter2]['properties'][f'issuer{year}_count']
            states['features'][counter2]['properties'][f'issuer{year}_{issuer_count}'] = pointer[counter1]['Count']
            states['features'][counter2]['properties'][f'issuer{year}_{issuer_count}_name'] = pointer[counter1]['Issuer']
            states['features'][counter2]['properties'][f'issuer{year}_count'] = states['features'][counter2]['properties'][f'issuer{year}_count'] + 1
            state_reference1 = pointer[counter1]['State']
            state_reference2 = pointer[counter1]['State']         
            counter2 = 0
            counter1 = counter1 + 1
            counter3 = counter3 + 1
            
    else:
        counter2 = counter2 + 1
        
#write out issuers and the number of plans by each issuer ot the geoJSON
counter1 = 0
counter2 = 0
counter3 = 0
pointer = state_issuer17
year = 17
issuer = pointer[counter1]['Issuer']


while counter1 < len(pointer):
    if pointer[counter1]['State'] == states['features'][counter2]['properties']['state_code']:
            issuer_count = states['features'][counter2]['properties'][f'issuer{year}_count']
            states['features'][counter2]['properties'][f'issuer{year}_{issuer_count}'] = pointer[counter1]['Count']
            states['features'][counter2]['properties'][f'issuer{year}_{issuer_count}_name'] = pointer[counter1]['Issuer']
            states['features'][counter2]['properties'][f'issuer{year}_count'] = states['features'][counter2]['properties'][f'issuer{year}_count'] + 1
            state_reference1 = pointer[counter1]['State']
            state_reference2 = pointer[counter1]['State']         
            counter2 = 0
            counter1 = counter1 + 1
            counter3 = counter3 + 1
            
    else:
        counter2 = counter2 + 1
        
#write out issuers and the number of plans by each issuer ot the geoJSON
counter1 = 0
counter2 = 0
counter3 = 0
pointer = state_issuer18
year = 18
issuer = pointer[counter1]['Issuer']


while counter1 < len(pointer):
    if pointer[counter1]['State'] == states['features'][counter2]['properties']['state_code']:
            issuer_count = states['features'][counter2]['properties'][f'issuer{year}_count']
            states['features'][counter2]['properties'][f'issuer{year}_{issuer_count}'] = pointer[counter1]['Count']
            states['features'][counter2]['properties'][f'issuer{year}_{issuer_count}_name'] = pointer[counter1]['Issuer']
            states['features'][counter2]['properties'][f'issuer{year}_count'] = states['features'][counter2]['properties'][f'issuer{year}_count'] + 1
            state_reference1 = pointer[counter1]['State']
            state_reference2 = pointer[counter1]['State']         
            counter2 = 0
            counter1 = counter1 + 1
            counter3 = counter3 + 1
            
    else:
        counter2 = counter2 + 1
        


# In[56]:


#split out each plan type
type15_df = pd.DataFrame(state_type15)
EPO15 = type15_df.loc[type15_df['Type'] == 'EPO'].reset_index(drop=True)
PPO15 = type15_df.loc[type15_df['Type'] == 'PPO'].reset_index(drop=True)
HMO15 = type15_df.loc[type15_df['Type'] == 'HMO'].reset_index(drop=True)
POS15 = type15_df.loc[type15_df['Type'] == 'POS'].reset_index(drop=True)
Indemnity15 = type15_df.loc[type15_df['Type'] == 'Indemnity'].reset_index(drop=True)

type16_df = pd.DataFrame(state_type15)
EPO16 = type15_df.loc[type16_df['Type'] == 'EPO'].reset_index(drop=True)
PPO16 = type15_df.loc[type16_df['Type'] == 'PPO'].reset_index(drop=True)
HMO16 = type15_df.loc[type16_df['Type'] == 'HMO'].reset_index(drop=True)
POS16 = type15_df.loc[type16_df['Type'] == 'POS'].reset_index(drop=True)
Indemnity16 = type16_df.loc[type16_df['Type'] == 'Indemnity'].reset_index(drop=True)

type17_df = pd.DataFrame(state_type17)
EPO17 = type17_df.loc[type17_df['Type'] == 'EPO'].reset_index(drop=True)
PPO17 = type17_df.loc[type17_df['Type'] == 'PPO'].reset_index(drop=True)
HMO17 = type17_df.loc[type17_df['Type'] == 'HMO'].reset_index(drop=True)
POS17 = type17_df.loc[type17_df['Type'] == 'POS'].reset_index(drop=True)
Indemnity17 = type17_df.loc[type17_df['Type'] == 'Indemnity'].reset_index(drop=True)

type18_df = pd.DataFrame(state_type18)
EPO18 = type18_df.loc[type18_df['Type'] == 'EPO'].reset_index(drop=True)
PPO18 = type18_df.loc[type18_df['Type'] == 'PPO'].reset_index(drop=True)
HMO18 = type18_df.loc[type18_df['Type'] == 'HMO'].reset_index(drop=True)
POS18 = type18_df.loc[type18_df['Type'] == 'POS'].reset_index(drop=True)
Indemnity18 = type18_df.loc[type18_df['Type'] == 'Indemnity'].reset_index(drop=True)


# In[57]:


#write out each plan type

counter1 = 0
counter2 = 0

pointer = EPO15
field = 'EPO15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0
        
pointer = PPO15
field = 'PPO15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
  
counter1 = 0
counter2 = 0

pointer = HMO15
field = 'HMO15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0

pointer = POS15
field = 'POS15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0

pointer = Indemnity15
field = 'Indemnity15'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
#next year

#write out each plan type

counter1 = 0
counter2 = 0

pointer = EPO16
field = 'EPO16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0
        
pointer = PPO16
field = 'PPO16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
  
counter1 = 0
counter2 = 0

pointer = HMO16
field = 'HMO16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0

pointer = POS16
field = 'POS16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0

pointer = Indemnity16
field = 'Indemnity16'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
#next year

#write out each plan type

counter1 = 0
counter2 = 0

pointer = EPO17
field = 'EPO17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0
        
pointer = PPO17
field = 'PPO17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
  
counter1 = 0
counter2 = 0

pointer = HMO17
field = 'HMO17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0

pointer = POS17
field = 'POS17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0

pointer = Indemnity17
field = 'Indemnity17'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
#next year

#write out each plan type

counter1 = 0
counter2 = 0

pointer = EPO18
field = 'EPO18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0
        
pointer = PPO18
field = 'PPO18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
  
counter1 = 0
counter2 = 0

pointer = HMO18
field = 'HMO18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0

pointer = POS18
field = 'POS18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
counter1 = 0
counter2 = 0

pointer = Indemnity18
field = 'Indemnity18'

while counter1 < len(pointer):
    lookup_state = pointer['State'][counter1]
    count_state = states['features'][counter2]['properties']['state_code']
    if lookup_state == count_state:
        states['features'][counter2]['properties'][field] = pointer.loc[pointer['State'] == lookup_state]['Count'][counter1]
        counter2 = 0
        counter1 = counter1 +1
    else:
        counter2 = counter2 +1
        
#next year


# In[58]:


states.to_json('./static/geoJson/modifiedStates.json',orient='records')


# In[ ]:




