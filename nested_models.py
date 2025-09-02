from pydantic import BaseModel,Field

class Address (BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name : str = Field(max_length=20)
    gender: str
    age : int
    address : Address
    
    
address_dict = {'city': 'Karachi', 'state': 'sindh', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Aman', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1.address.city)

    