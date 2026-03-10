from pydantic import BaseModel, computed_field

## Computed field: It is the filed which can be calculated with the help of other fields

class Patient(BaseModel):
    weight: float # in kgs
    height: float # in meters

    @computed_field()
    @property
    def bmi(self) ->float:
        return round(self.weight/self.height**2,2)   


def update_weight(patient: Patient):
    print(patient.bmi)

patient_info = {'weight': 50, 'height': 3}
patient1 = Patient(**patient_info)
update_weight(patient=patient1)
