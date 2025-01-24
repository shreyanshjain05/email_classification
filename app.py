import streamlit as st
import pickle

def predictive_system(input_mail):
    input_mail_vectorized = vectorizer.transform([input_mail])
    prediction = model.predict(input_mail_vectorized)
    if prediction[0] == 1:
        return 'Spam'
    else:
        return 'Ham'



model = pickle.load(open('email_classification.pkl' , 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl' , 'rb'))
st.title("Email Spam vs Ham classification")
st.write("Enter the mail text")
input_mail = st.text_area("Enter the mail content")
if st.button('Classify'):
    if input_mail:
        result = predictive_system(input_mail)
        st.write(f"The mail is classified as: {result}")
    else:
        st.write("Please enter the content to classify")


