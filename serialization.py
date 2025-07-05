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


# temp=patient_1.model_dump_json()
# temp=patient_1.model_dump()
temp=patient_1.model_dump(include=['name'])
temp=patient_1.model_dump(exclude={'address':['state']})
 
 #exclude unset parameter is also involve 

print(temp)
print(type(temp))

