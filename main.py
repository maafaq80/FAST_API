from fastapi import FastAPI
import json

app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data
    


# @app.get("/view")
# async def view():
#     return load_data()

@app.get("/patient/{patient_id}")
async def patient_record(patient_id):
    data=load_data()
    if patient_id in data:
        return data['patient_id']
    return {'error':"Record Not found"}    