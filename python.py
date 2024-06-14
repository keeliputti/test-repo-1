from pydantic import BaseModel, Field, root_validator

class MyModel(BaseModel):
    package_id: str
    data_captain_team: str = Field(default_factory=str)
    data_developer_team: str = Field(default_factory=str)

    @root_validator(pre=True)
    def set_team_names(cls, values):
        def set_team_name(field_name, prefix):
            if field_name not in values or values[field_name] is None:
                if '/' in values.get('package_id', ''):
                    parts = values['package_id'].split('/')
                    if len(parts) == 2:
                        provider_id, package_id = parts
                    else:
                        raise ValueError("You must provide package_id='<provider>/<package>'")
                    values[field_name] = f"{prefix}-{provider_id}-{package_id}"
                else:
                    raise ValueError("You must provide package_id='<provider>/<package>'")
        
        set_team_name('data_captain_team', 'dz-captains')
        set_team_name('data_developer_team', 'dz-developers')
        
        return values

# Test cases
if __name__ == "__main__":
    # Example with package_id and without team names
    obj1 = MyModel(package_id='provider1/package1')
    print(obj1.data_captain_team)  # Output: dz-captains-provider1-package1
    print(obj1.data_developer_team)  # Output: dz-developers-provider1-package1

    # Example with package_id and provided team names
    obj2 = MyModel(package_id='provider2/package2', data_captain_team='existing_captain_team', data_developer_team='existing_developer_team')
    print(obj2.data_captain_team)  # Output: existing_captain_team
    print(obj2.data_developer_team)  # Output: existing_developer_team
