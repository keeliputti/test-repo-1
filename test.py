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




## Drafted Goals for Performance and Impact:

**1. Data Framework: Automating Access and Client Onboarding**

* **Goal:** Implement a configuration service to automate access deployments for clients, eliminating manual intervention and associated delays. This will standardize the onboarding process, improve efficiency, and allow for faster response times to client inquiries.
* **Metrics:**  
    *  Reduction in manual access deployment time by X%.
    *  Decrease in client onboarding delays by Y%.

**2. dzclients: Parity and Efficiency**

* **Goal 1:** Achieve and maintain feature parity between dpy (Python) and djava (Java) libraries within dzclients. This will ensure consistent functionality for all clients regardless of programming language preference.
* **Goal 2:** Develop and integrate serialization capabilities using Arrow for storing Java POJOs. This will enable faster data transfer from clients to the server and eliminate data type (dtype) inconsistencies.
* **Metrics:**
    *  Maintain 100% feature parity between dpy and djava libraries.
    *  Reduce data transfer time by Z% through Arrow serialization.

**3. User Engagement: Knowledge, Support, and Continuous Improvement**

* **Goal 1:**  Continuously ensure effective communication of new developments to clients, keeping them informed and maximizing utilization of dz's offerings. 
* **Goal 2:**  Maintain a high level of client satisfaction by providing ongoing support and addressing their requirements. This includes assisting non-technical clients in understanding and utilizing dz's functionalities.
* **Metrics:**
    *  Conduct X client satisfaction surveys per quarter.
    *  Maintain a Y% positive client satisfaction rating.

**Additional Tips:**

* Feel free to adjust these goals further to better reflect your specific role and responsibilities. 
*  Quantify your goals whenever possible using metrics to demonstrate the impact of your work.
* Be sure to align these goals with your firm's overall objectives for the year.

