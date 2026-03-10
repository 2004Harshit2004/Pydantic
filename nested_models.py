from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin_code: int

class Person(BaseModel):
    name: str
    age: int
    address: Address

def update_info(person: Person):
    print(person.address)
    print(person.address.city)

address_info = {'city': 'Bhopal', 'state': 'Madhya Pradesh', 'pin_code': 462024}
address1 = Address(**address_info)

person_info = {'name': 'Harshit Goswami', 'age': 22, 'address':address1}
person1 = Person(**person_info)



update_info(person= person1)