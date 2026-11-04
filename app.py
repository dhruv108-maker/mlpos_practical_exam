import fastapi
import pickle
import uvicorn
import streamlit as st

app = fastapi.FastAPI()

#get the model
model = pickle.load(open('TrainedModels/model.pkl', 'rb'))
encoders = pickle.load(open('TrainedModels/encoder.pkl', 'rb'))


@app.get("/")
def read_root():
    return {"message": "Welcome to the Placement Classification API"}

@app.post("/predict")
def predict_placement(
    gender: str, ssc_p: float, ssc_b: str, hsc_p: float, hsc_b: str, hsc_s: str, 
    degree_p: float, degree_t: str, workex: str, etest_p: float, specialisation: str, mba_p: float ):
    
    # encoding  categorical variables into numerical variables
    gender_encoded = encoders['gender'].transform([gender])[0]
    ssc_b_encoded = encoders['ssc_b'].transform([ssc_b])[0]

    hsc_b_encoded = encoders['hsc_b'].transform([hsc_b])[0]

    hsc_s_encoded = encoders['hsc_s'].transform([hsc_s])[0]
    degree_t_encoded = encoders['degree_t'].transform([degree_t])[0]
    workex_encoded = encoders['workex'].transform([workex])[0]
    specialisation_encoded = encoders['specialisation'].transform([specialisation])[0]

    # Create feature vector
    features = [
            [
            gender_encoded, 
            ssc_p, ssc_b_encoded, 
            hsc_p, hsc_b_encoded, 
            hsc_s_encoded, 
            degree_p, 
            degree_t_encoded, 
            workex_encoded, 
            etest_p, 
            specialisation_encoded, 
            mba_p

            ]
        ]


    prediction = model.predict(features)

    return {"predicted_status": prediction[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.", port=8000)

