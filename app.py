'''
 Making webpage for HR Analytics project using streamlit
 
 @author: sahil shaikh
 
'''
 
 
import streamlit as st
import pandas as pd 
import numpy as np 
import time
import pickle
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

pickle_in = open("DecisionTree22.pkl","rb")
dec_cl = pickle.load(pickle_in)


# adding title
st.title('HR Analytics')

# adding image 
st.image("HR-Analytics.jpg",width = 800)


# adding sidebar

nav = st.sidebar.radio("NAVIGATION",["Home","Prediction"])

if nav == "Home":
    
    data = pd.read_excel('HR Analytics F3.xlsx')
    if st.checkbox("Show Table"):
        st.dataframe(data)

    if st.checkbox("Show data_dictionary Table"):      
        st.image("data_dictionary.png",width = 800)     
         
    
if nav == "Prediction":
    
    st.header("Know employe attrition")
    Age  = st.slider("enter your age ",0,100)
    MonthlyIncome = st.number_input("Enter your MonthlyIncome",0.00,1000000.00,step = 2000.0)
    YearsAtCompany = st.slider("YearsAtCompany",0,80)
    JobInvolvement = st.selectbox('JobInvolvement', ['1','2','3','4'])
    JobSatisfaction = st.selectbox('JobSatisfaction', ['1','2','3','4'])
    mean_time = st.number_input("Enter your working hours in a day",0.00,20.00,step = 1.00)
    
    BusinessTravel = ['Travel_Rarely', 'Travel_Frequently']
    BusinessTravel1 = st.selectbox('Business Travel', BusinessTravel)
    
    Department = ['Research & Development','Sales']
    Department1 = st.selectbox('Department', Department)
    
    MaritalStatus = ['Married','Single']
    MaritalStatus1 = st.selectbox('Marital Status', MaritalStatus)
    
    
    cat_list = ['b_t_r','b_t_f','nont', 'dep', 'dept_rd', 'm_s_s', 'm_s_m']         
    for i in cat_list:
           exec("%s = %d" % (i,0))
    
    if BusinessTravel == 'Travel_Rarely':
        b_t_r = 1
    elif BusinessTravel == 'Travel_Frequently':
        b_t_f = 1
    else:
        pass
    
    if Department == 'Research & Development':
            dep = 1
    elif Department =='Sales':
            dept_rd = 1
    else:
        pass
    
    if MaritalStatus == 'Married':
        m_s_s = 1
    elif MaritalStatus == 'Single':
        m_s_m = 1
    else:
        pass  
    
    
    
    
    
    
   
    
    val = np.asarray([Age,MonthlyIncome,YearsAtCompany,JobInvolvement,JobSatisfaction,mean_time,b_t_r,b_t_f,dep,m_s_s,m_s_m]).reshape(1,-1)
    
#    std_data = scaler.fit_transform(val)
#    print(std_data)
    
    pred = dec_cl.predict(val)
    
    if st.button("Predict"):
        
        progress = st.progress(0)    # this is for progress bar
        for i in range(100):
            time.sleep(0.001)
            progress.progress(i+1)
            
        st.success('The output is {}'.format(pred))
        
        if pred == 0:
            st.write('***The output is No***')
        else:
            st.write('***The output is Yes***')
            
    