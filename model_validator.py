from pydantic import BaseModel, EmailStr, model_validator
from typing import Dict

## model validator is used to perform complex data transformation and data validation when one field depend upon another (here we have access all the field(model))

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    contact_detail: Dict[str,str]

    ## Patient older than 60 should always have an emergency number of their family member
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_detail:
            raise ValueError('Patient older than 60 must have emergency number')
        return model

    

def update_patient(patient:Patient):
    print(patient.name)
    print(patient.email)

patient_info = {'name': 'Harshit', 'age': '65', 'email': 'hg@hdfc.com', 'contact_detail': {'no': '987', 'emergency':'98765'}}
patient1=Patient(**patient_info) ## validation -> type coercion

update_patient(patient=patient1)