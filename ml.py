# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:24:14 2023

@author: user
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/user/Downloads/ml/Diabetes_model.sav', 'rb'), encoding='latin1')
heart_disease_model = pickle.load(open('C:/Users/user/Downloads/ml/Heart_model.sav', 'rb'), encoding='latin1')
Breast_Cancer_model = pickle.load(open('C:/Users/user/Downloads/ml/Breast_Cancer_model.sav', 'rb'), encoding='latin1')



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Breast Cancer Classification'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using DL')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using DL')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Breast Cancer's Prediction Page
if (selected == "Breast Cancer Classification"):
    
    # page title
    st.title("Breast Cancer Classification Prediction using DL")
    
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)  
    
    with col1:
        radius_mean = st.text_input('mean radius')
        
    with col2:
        texture_mean = st.text_input('mean texture')
        
    with col3:
        perimeter_mean = st.text_input('mean perimeter')
        
    with col4:
        area_mean = st.text_input('mean area')
        
    with col5:
        smoothness_mean = st.text_input('mean smoothness')
        
    with col6:
        compactness_mean = st.text_input('mean compactness')
        
    with col7:
        concavity_mean = st.text_input('mean_concavity')
        
    with col8:
        concave_points_mean = st.text_input('mean concave points')
        
    with col1:
        symmetry_mean = st.text_input('mean symmetry')
        
    with col2:
        fractal_dimension_mean = st.text_input('mean fractal dimension')
        
    with col3:
        radius_se = st.text_input('radius se')
        
    with col4:
        texture_se = st.text_input('texture se')
        
    with col5:
        perimeter_se = st.text_input('perimeter se')
        
    with col6:
        area_se = st.text_input('area se')
        
    with col7:
        smoothness_se = st.text_input('smoothness_se')
        
    with col8:
        compactness_se = st.text_input('compactness se')
        
        
    with col1:
        concavity_se = st.text_input('concavity se')
        
    with col2:
        concave_points_se = st.text_input('concave points se')
        
    with col3:
        symmetry_se = st.text_input('symmetry se')
        
    with col4:
        fractal_dimension_se = st.text_input('fractal dimension se')
        
    with col5:
        radius_worst = st.text_input('radius_worst')
        
    with col6:
         texture_worst = st.text_input('texture worst')
         
    with col7:
         perimeter_worst = st.text_input('perimeter worst')
         
    with col8:
        area_worst = st.text_input('area worst')
        
    with col1:
        smoothness_worst = st.text_input('smoothness worst')
        
    with col2:
        compactness_worst = st.text_input('compactness worst')
        
    with col3:
        concavity_worst = st.text_input('concavity worst')
        
    with col4:
        concave_points_worst = st.text_input('concave_points_worst')
        
    with col5:
        symmetry_worst = st.text_input('symmetry_worst')
        
    with col6:
         fractal_dimension_worst = st.text_input('fractal_dimension_worst')
         
   
        
    
    
   # code for Prediction
Breast_Cancer_diagnosis = ''

# creating a button for Prediction    
if st.button("Breast Cancer's Test Result"):
    Breast_Cancer_prediction = Breast_Cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])                          
        
    if (Breast_Cancer_prediction[0] == 1):
        Breast_Cancer_diagnosis = "Malignant tumor detected (Can spread from one cell to another)"
    else:
        Breast_Cancer_diagnosis = "Benign tumor detected (Cannot spread from one cell to another)"

    st.success(Breast_Cancer_diagnosis)



