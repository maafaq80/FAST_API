from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import Field,computed_field,BaseModel
from typing import Annotated,Literal
import json


app=FastAPI()
@app.get("/")
def default():
    return "Working API"

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data

def save_data(data):
    with open('patients.json','w')as f:
        json.dump(data,f)

class Patient(BaseModel):
    id: Annotated[str,Field(...,description="ID of the Patient",examples=['P001'])]
    name: Annotated[str,Field(...,description="Name of the Patient")]
    city: Annotated[str,Field(...,description="Present City of Patient ")]
    age: Annotated[int,Field(...,description="Age of the Patient",gt=0,lt=120)]
    gender: Annotated[Literal['male','Female','Others'],Field(...,description="Gender of the Patient")]
    height: Annotated[float,Field(...,gt=0,description="Height of the Patient")]
    weight: Annotated[float,Field(...,gt=0,description="Weight of the patient ")]
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return "Underweight"
        
        elif self.bmi<30:
            return "Normal"
        
        else:
            return "Obese"
        
        

@app.post("/create")
def create_patient(patient:Patient):
    data=load_data()
    
    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient Already Exist")

    data[patient.id]=patient.model_dump(exclude=['id'])
    
    save_data(data)
    
    return JSONResponse(status_code=201,content={'message':'Patient Created Successfully'})
    
    