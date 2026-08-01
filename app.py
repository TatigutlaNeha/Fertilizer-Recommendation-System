import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl","rb"))
fert_encoder = pickle.load(open("fertilizer_encoder.pkl","rb"))

st.title("Fertilizer Recommendation System")

temperature = st.number_input("Temperature")
moisture = st.number_input("Moisture")
rainfall = st.number_input("Rainfall")
ph = st.number_input("PH")
nitrogen = st.number_input("Nitrogen")
phosphorous = st.number_input("Phosphorous")
potassium = st.number_input("Potassium")
carbon = st.number_input("Carbon")
soil = st.number_input("Soil")
crop = st.number_input("Crop")

if st.button("Predict Fertilizer"):

    data = pd.DataFrame([[temperature,moisture,rainfall,ph,nitrogen,
                          phosphorous,potassium,carbon,soil,crop]],
                        columns=["Temperature","Moisture","Rainfall","PH",
                                 "Nitrogen","Phosphorous","Potassium",
                                 "Carbon","Soil","Crop"])

    pred = model.predict(data)

    fertilizer_name = fert_encoder.inverse_transform(pred)

    st.success(f"Recommended Fertilizer: {fertilizer_name[0]}")

#py -m streamlit run app.py to run it
