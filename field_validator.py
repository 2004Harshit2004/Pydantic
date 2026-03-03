from pydantic import BaseModel, EmailStr, field_validator

## field validator is used to perform complex data validation and data transformaion on a particular field

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr

    ## validate email is of hdfc or icici bank employer or not
    @field_validator('email')
    @classmethod
    def validate_email(cls,val):
        valid_mail = ['hdfc.com', 'icici.com']
        domain = val.split('@')[-1]
        if domain not in valid_mail:
            raise ValueError('Not a valid email')
        return val
    
    ## transform name to upper cases
    @field_validator('name')
    @classmethod
    def transform_name(cls,val):
        return val.upper()
    
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls, val):
        if 0<val<100:
            return val
        else:
            raise ValueError('Age should be between 0-100')

def update_patient(patient:Patient):
    print(patient.name)
    print(patient.email)

patient_info = {'name': 'Harshit', 'age': '20', 'email': 'hg@hdfc.com'}
patient1=Patient(**patient_info) ## validation -> type coercion

update_patient(patient=patient1)