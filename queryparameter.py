from fastapi import FastAPI,Path,HTTPException,Query
import json

app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data
    

@app.get("/")
async def hello():
    return {"message":"hello"}


# @app.get("/about")
# async def about():
#     return {"message":"THis is muhammad aafaq how can i help you "}

# @app.get("/view")
# async def view():
#     return load_data()

@app.get('/patient/{patient_id}')
def patient_record(patient_id:str=Path(...,description="Enter id for patient",examples="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error':"Record Not found"}    
    raise HTTPException(status_code=404,detail="Patient Not Found")


@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description="select one between weight,height,bmi"),
                  order:str=Query(description="Choose asc or desc")):
    valid_sort_by=['weight','height','bmi']
    if sort_by not in valid_sort_by:
        raise HTTPException(status_code=400,detail=f"invalid field select from {valid_sort_by}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="invalid order selection between asc and desc")
    
    data=load_data()
    sort_order=True if order =='desc' else False
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by,0),reverse=sort_order)
    return sorted_data
        
# @app.get('/sort')
# def sort_patients(
#     sort_by: str = Query("weight", description="Select one of: weight, height, bmi"),
#     order: str = Query("asc", description="Choose either asc or desc")
# ):
#     valid_sort_by = ['weight', 'height', 'bmi']
#     if sort_by not in valid_sort_by:
#         raise HTTPException(status_code=400, detail=f"Invalid field. Select from {valid_sort_by}")
    
#     if order not in ['asc', 'desc']:
#         raise HTTPException(status_code=400, detail="Invalid order. Choose asc or desc")
    
#     data = load_data()
#     sort_order = True if order == 'desc' else False
#     sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
#     return sorted_data
