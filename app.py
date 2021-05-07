#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries:
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# In[2]:


app=Flask(__name__)


# In[3]:


model=pickle.load(open('linear.pkl','rb'))


# In[4]:


@app.route('/')
def home():
    return render_template('home.html')

#%%
venue={0:'Barabati Stadium', 1:'Brabourne Stadium', 2:'Buffalo Park',3: 'De Beers Diamond Oval', 
       4:'Dr DY Patil Sports Academy', 5:'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 
       6:'Dubai International Cricket Stadium',7: 'Eden Gardens', 8:'Feroz Shah Kotla', 
       9:'Himachal Pradesh Cricket Association Stadium',10: 'Holkar Cricket Stadium', 
       11:'JSCA International Stadium Complex', 12:'Kingsmead', 13:'M Chinnaswamy Stadium', 
       14:'MA Chidambaram Stadium, Chepauk', 15:'Maharashtra Cricket Association Stadium', 16:'New Wanderers Stadium', 
       17:'Newlands', 18:'OUTsurance Oval', 19:'Punjab Cricket Association IS Bindra Stadium, Mohali', 
       20:'Punjab Cricket Association Stadium, Mohali', 21:'Rajiv Gandhi International Stadium, Uppal', 
       22:'Sardar Patel Stadium, Motera',23:'Sawai Mansingh Stadium', 
       24:'Shaheed Veer Narayan Singh International Stadium', 25:'Sharjah Cricket Stadium', 26:'Sheikh Zayed Stadium', 
       27:"St George's Park", 28:'Subrata Roy Sahara Stadium',29: 'SuperSport Park', 30:'Wankhede Stadium'}

batting={0:'Chennai Super Kings',1: 'Delhi Daredevils', 2:'Kings XI Punjab',3: 'Kolkata Knight Riders', 
         4:'Mumbai Indians', 5:'Rajasthan Royals',6: 'Royal Challengers Bangalore', 7:'Sunrisers Hyderabad'}

bowling={0:'Chennai Super Kings',1: 'Delhi Daredevils', 2:'Kings XI Punjab',3: 'Kolkata Knight Riders', 
         4:'Mumbai Indians', 5:'Rajasthan Royals',6: 'Royal Challengers Bangalore', 7:'Sunrisers Hyderabad'}


# In[5]:

@app.route("/predict", methods=['POST'])
def predict():
    if request.method =='POST':
        data1=int(request.form["venue"])
        data2=int(request.form["bat_team"])
        data3=int(request.form["bowl_team"])
        data4=int(request.form["runs"])
        data5=int(request.form["wickets"])
        data6=float(request.form["overs"])
        data7=int(request.form["runs_last_5"])
        data8=int(request.form["wickets_last_5"])
        
        
        arr=np.array([[data1,data2,data3,data4,data5,data6,data7,data8]])
        pred=model.predict(arr)
    
    
        #create original output dict
        output_dict= dict()
        output_dict['Venue']=venue[int(data1)]
        output_dict['Batting Teams']=batting[int(data2)]
        output_dict['Bowling Teams']=bowling[int(data3)]
        output_dict['Runs']=data4
        output_dict['Wickets']=data5
        output_dict['Overs']=data6
        output_dict['Runs scored in previous 5 Overs']=data7
        output_dict['Wickets taken in previous 5 Overs']=data8

        return render_template('result.html',original_input=output_dict,lower_limit = int(pred-5), 
                               upper_limit = int(pred+5))
# In[7]:


if __name__=='__main__':
    app.run(debug=True)


# In[ ]:






# In[ ]:




