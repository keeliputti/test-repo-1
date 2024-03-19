from typing import Optional
from pydantic import BaseModel

class Class1(BaseModel):
    flag: str

class Class2(BaseModel):
    data1: str
    data2: int
    data3: Optional[str] = None


from typing import Union

class CombinedSchema(BaseModel):
    class1: Class1
    class2: Union[Class2, None]

    @classmethod
    def __get_validators__(cls):
        yield from super().__get_validators__()
        yield cls.validate_flag

    @classmethod
    def validate_flag(cls, value):
        if value == "internal":
            yield {"class2": {"__config__": {"validate_all": True}}}
        else:
            yield value



schema = CombinedSchema(class1=Class1(flag="internal"), class2=Class2(data1="abc", data2="xyz"))
# Valid, no validation for Class2 fields

schema = CombinedSchema(class1=Class1(flag="external"), class2=Class2(data1="123", data2="invalid"))  # Validation error for data2
