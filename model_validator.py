from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator,model_validator
from typing import List, Dict, Optional, Annotated


##Defining Model validator if age > 60 check emergency no is present if yes then ok 
class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    allergies: List[str]
    contact_details: Dict[str, str]
    

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain=['hdfc.com','icic.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError("not a valid Domain")
        return value
    
    @field_validator('name',mode="after") #mode before and after related to type coersion
    @classmethod
    def capitalize(cls,value):
        return value.upper()
    
    @model_validator(mode="after")
    def validate_emergency_number(cls,model):
        if(model.age>60 and 'emergency' not in model.contact_details):
            raise ValueError("Patient older than 60 have emergency number")
        return model
    
    

def update_patient_record(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    
    
record = {
    "name": "aafaq",
    "email": "aafaq@hdfc.com",  
    "age": 80, # age greator than 60
    "weight":33.4,
    "allergies": ["Pollen"],
    "contact_details": {"phone": "098076765"} 
}

patient_1=Patient(**record)
update_patient_record(patient_1)


