import streamlit as st
import requests
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit_lottie as st_lottie
import joblib
import numpy as np
import PIL as Image
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title='Customer Segmentation',
    page_icon=':gem:',
    initial_sidebar_state='collapsed'  # Collapsed sidebar
)

def load_lottie(url): # test url if you want to use your own lottie file 'valid url' or 'invalid url'
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

model = joblib.load(open("Customer_segmentation_model", 'rb'))

def predict_cluster(age, gender, spending_score, annual_income):

    features = np.array([age, gender, spending_score, annual_income]).reshape(1, -1)
    print(features)
    prediction = model.predict(features)
    return prediction


with st.sidebar:
    choose = option_menu(None, ["Home", "Graphs", "About", "Contact"],
                         icons=['house', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": '#E0E0EF', "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )


if choose=='Home':
       st.write('# Customer Segmentation Deployment')
       st.write('---')
       st.subheader('Enter your details to predict your customer segmentation cluster')
       # User input
       age = st.number_input("Enter the age: ",min_value=0)
       gender = st.radio("Select the gender:", ('Male', 'Female'))
       gender_encoding = 0 if gender == 'Male' else 1
       spending_score = st.slider("Enter the spending score (1-100):", min_value=1, max_value=100, value=50, step=1)
       annual_income = st.number_input("Enter the annual income (k$): ",min_value=0)
       # Predict the cluster
       cluster = predict_cluster(age, gender_encoding, spending_score, annual_income)

       if st.button("Predict"):
          if cluster[0]== 'Label A':
             st.warning("Cluster 0: The Explorers")
             st.write("This cluster consists of adults and middle-aged individuals who are mostly upper-middle-income earners and low spenders. They could be individuals who are just starting out in their careers and may not have a lot of disposable income.")
          elif cluster[0]=='Label B':
             st.success("Cluster 1: The Trendsetters")
             st.write("This cluster consists of adults who are mostly upper-middle-income earners and very high spenders. They could be individuals who are established in their careers and have a lot of disposable income.")
          elif cluster[0]=='Label C':
             st.info("Cluster 2: The Moderates")
             st.write("This cluster consists of middle-aged individuals who are mostly middle-income earners and have moderate spending habits. They could be individuals who are in different stages of their careers and may have different financial obligations.")
          elif cluster[0]=='Label D':
              st.error("Cluster 3: The Strugglers")
              st.write("This cluster consists of adults and middle-aged individuals who are mostly low-income earners and low spenders. They could be individuals who are living paycheck to paycheck and may be struggling to make ends meet.")
          elif cluster[0]=='Label E':
              st.info("Cluster 4: The Dreamers")
              st.write("This cluster consists of young adults who are mostly low-income earners and very high spenders. They could be individuals who are living paycheck to paycheck and may be struggling to make ends meet.")




elif choose=='About':
    st.write('# About Page')
    st.write('---')
    st.write("🎯💡 Welcome to Customer Segmentation Deployment! We specialize in providing advanced customer segmentation solutions that help businesses understand and connect with their customers better. Our data-driven approach combines analytics, machine learning, and marketing expertise to create customized segmentation models tailored to your needs. By implementing customer segmentation, you can personalize marketing, improve customer experiences, optimize resource allocation, drive product development, and gain a competitive advantage. ✨🚀 Partner with us to unlock the power of customer segmentation and drive your business's success. Contact us today to learn more. 📞📧")
    st.image("15755-removebg-preview.png")
 

elif choose == "Contact":
    st.write('# Contact Us')
    st.write('---')
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        st.write('## Please help us improve!')
        Name=st.text_input(label='Please Enter Your Name') 
        Email=st.text_input(label='Please Enter Email')
        Message=st.text_input(label='Please Enter Your Message') 
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')



elif choose == 'Graphs':
    st.write('# Customer Segmentation Graphs')
    st.write('---')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write("## Female Vs Male Customers Graph:")
    st.image("Gender.png")
    st.write("## Age Period Graph:")
    st.image("Age Period.png")
    st.write("## Age Vs Gender Graph:")
    st.image("Age vs gender.png")
    st.write("## Age Vs Annual Income:")
    st.image("Age vs income.png")
    st.write("## Age Vs Spending Rate:")
    st.image("Age Vs Send.png")
    st.write("## Annual Income Period:")
    st.image("Income period.png")
    st.write("## Spending Rate Period:")
    st.image("Spenders Period.png")
    
    data = pd.read_csv('Mall_Customers.csv')
    # Create a DataFrame
    df = pd.DataFrame(data)
    
   
