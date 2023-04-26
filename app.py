import streamlit as st
import numpy as np
import pickle


#Importing our pickle file
model = pickle.load(open('mlproject.pkl', 'rb'))

#Title of app
st.title('Will the user churn or not ') 

#Range of paramenters
TotalCharges  = st.slider("TotalCharges ",0.00,2800.76)
tenure = st.slider("tenure",0.000,100.01,step=0.0001,format="%.3f")
MonthlyCharges = st.slider("MonthlyCharges",0,2500)
Contract = st.slider("Contract",0,100.00)
PaymentMethod = st.slider("PaymentMethod",0,10.00)
# ProductRelated = st.slider("ProductRelated",0,200)

#Pridiction function
def predict():
    float_features = [float(X) for X in [TotalCharges, tenure, MonthlyCharges]]
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

