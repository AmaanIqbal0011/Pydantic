from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('name')
    @classmethod
    def name_validator(cls,value):
        valid_names = ['aman','saad','fehar','naveen']
        if value not in valid_names:
             raise ValueError("Not a Valid Patient")
        return value.upper() 
    
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_email=['abc.com','xyz.com','gmail.com','hotmail.com']
        emails = value.split('@')[-1]
        
        if emails not in valid_email:
            raise ValueError("Please  give corrected email")
        return value
    


    
    
patient_info = {'name':'aman', 'email':'abc@gmail.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}
patient1 = Patient(**patient_info) # validation -> type coercion

print(patient1)    