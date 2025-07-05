from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:int
    
    
    
class Patient(BaseModel):
    
    name:str
    gender:str
    age:int
    address:Address
    
    
address_dict={"city":"Peshawar","state":"Pakistan","pin":"12311"}
address_1=Address(**address_dict)

patient_record={"name":"aafaq","gender":"male","age":45,"address":address_1}
patient_1=Patient(**patient_record)

print(patient_1.name)
print(patient_1.age)
print(patient_1.address.state)
print(patient_1.address.pin)

