from pydantic import BaseModel,Field,EmailStr
from typing import List,Dict,Optional,Annotated

class Patient_info(BaseModel):
    name:Annotated[str,Field(max_length=20,title='name of the patient',description='give patient name')]
    email:EmailStr
    age:int = Field(gt=0,lt=120)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:Optional[bool]=None
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details:Annotated[Optional[Dict[str,str]],Field(default=None)]


patient_1 = {'name':'amaan','email':'amaaniqbal0011@gmail.com','age':12,'weight':45}

validate_info = Patient_info(**patient_1)

print(validate_info)    