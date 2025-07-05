from pydantic import BaseModel, Field, AnyUrl, EmailStr
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str = Annotated[str, Field(max_length=50, description="Give the name of the patient")]
    email: EmailStr
    age: int
    linkdein_url: AnyUrl
    weight:Annotated[float,Field(description="Give the weight in float",strict=True)]
    alergies: Optional[List[str]] = Field(default=None, description="Allergies of the patient")
    married: Optional[bool] = Field(default=None, description="Is the patient married?")
    contact_details: Dict[str, str]

def update_patient_record(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.linkdein_url)
    print(patient.weight)
    print(patient.alergies)
    print(patient.contact_details)

record = {
    "name": "aafaq",
    "email": "aafaq@example.com",  
    "age": 20,
    "linkdein_url": "http://www.linkdein.com/234",
    "weight":33.4,
    "alergies": ["Pollen"],
    "contact_details": {"phone": "098076765"} 
}

patient_1 = Patient(**record)
update_patient_record(patient_1)
