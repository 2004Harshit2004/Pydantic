from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50,title='What is your name', description='Give name in less than 50 words', examples=['Harshit','hg'])]
    age: int
    email: EmailStr
    linked_url: AnyUrl
    weight: Annotated[float, Field(gt=0,strict=True)]
    married: Annotated[bool, Field(default=False, description='Is patient married or not')]
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_detail: Dict[str,str]



def insert_patient(name: str, age: int):

    print(name)
    print(age)

    print("data is inserted in DB")

def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.email)


patient_info={'name':'Harshit', 'age':'20', 'email':'hg@gmail.com', 'linked_url':'https://github.com/campusx-official/pydantic-crash-course/blob/main/1_pydantic_why.py', 'weight':87, 'allergies': ['x','y','z'], 'contact_detail': {'email':'xyz', 'phone':'43245432'}}

patient1=Patient(**patient_info)

update_patient(patient1)