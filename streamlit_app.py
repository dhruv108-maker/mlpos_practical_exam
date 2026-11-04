import streamlit as st
import requests

st.title("Placement Prediction")

gender = st.selectbox("Gender", ["M", "F"])
ssc_p = st.number_input("SSC Percentage", 0.0, 100.0)
ssc_b = st.selectbox("SSC Board", ["Central", "Others"])
hsc_p = st.number_input("HSC Percentage", 0.0, 100.0)
hsc_b = st.selectbox("HSC Board", ["Central", "Others"])
hsc_s = st.selectbox("HSC Stream", ["Commerce", "Science", "Arts"])
degree_p = st.number_input("Degree Percentage", 0.0, 100.0)
degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
workex = st.selectbox("Work Experience", ["No", "Yes"])
etest_p = st.number_input("Employability Test", 0.0, 100.0)
specialisation = st.selectbox("Specialisation", ["Mkt&HR", "Mkt&Fin"])
mba_p = st.number_input("MBA Percentage", 0.0, 100.0)

if st.button("Predict"):

    data = {
        "gender": gender, "ssc_p": ssc_p, "ssc_b": ssc_b,
        "hsc_p": hsc_p, "hsc_b": hsc_b, "hsc_s": hsc_s,
        "degree_p": degree_p, "degree_t": degree_t,
        "workex": workex, "etest_p": etest_p,
        "specialisation": specialisation, "mba_p": mba_p
    }

    try:
        
        result = requests.post(
            "http://127.0.0.1:8000/predict", params=data
        )

        if result.status_code == 200:
            st.success("Result: " + result.json()["predicted_status"])
        else:
            st.error("Prediction failed!")

    except:

        st.error("Start the FastAPI server first!")
