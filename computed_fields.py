from pydantic import BaseModel, EmailStr, Field, field_validator,computed_field
from typing import List, Dict, Optional, Annotated

##Suppose we want to calculate BMI and it can't enter by user so we calculate it by height and weight


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height:float
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
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    

def update_patient_record(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.bmi)
    
    
record = {
    "name": "aafaq",
    "email": "aafaq@hdfc.com",  
    "age": 20,
    "weight":90,
    "height":1.72,
    "allergies": ["Pollen"],
    "contact_details": {"phone": "098076765"} 
}

patient_1=Patient(**record)
update_patient_record(patient_1)