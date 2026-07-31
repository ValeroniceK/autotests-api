from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
    address: Address

user = User(id=1, name="Alice", address={"city": "New York", "zip_code": "10001"})
print(user.address.city)
print(user.model_dump_json())
