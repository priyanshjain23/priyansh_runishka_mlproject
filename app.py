import streamlit as st
import numpy as np
import pickle


#Importing our pickle file
model = pickle.load(open('mlproject.pkl', 'rb'))

#Title of app
st.title('Will the User Churn or Not ') 

#Range of paramenters
TotalCharges  = st.slider("TotalCharges ",0,2800)
tenure = st.slider("tenure",0,100,format="%.3f")
MonthlyCharges = st.slider("MonthlyCharges",0,2500)
Contract = st.slider("Contract",0,100)
# PaymentMethod = st.slider("PaymentMethod",0.00,10.00)
# ProductRelated = st.slider("ProductRelated",0,200)

#Pridiction function
def predict():
    float_features = [float(X) for X in [TotalCharges, tenure, MonthlyCharges,Contract]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)

#Printing the output 
    if(int(label)==1):
        st.success('Hureyyyy!! The user will not churn '  + ' :thumbsup:')
    else:
        st.success('Ohhh The user will churn '  + ' :thumbsup:')

trigger = st.button('Predict', on_click=predict)

