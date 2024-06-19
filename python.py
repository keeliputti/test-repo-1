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



import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define the positions of the client, KDC, and server
client_pos = (1, 1)
kdc_pos = (5, 1)
server_pos = (9, 1)

# Draw the components
ax.text(client_pos[0], client_pos[1], "Client", fontsize=12, ha='center', bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5'))
ax.text(kdc_pos[0], kdc_pos[1], "KDC", fontsize=12, ha='center', bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='round,pad=0.5'))
ax.text(server_pos[0], server_pos[1], "Server", fontsize=12, ha='center', bbox=dict(facecolor='lightcoral', edgecolor='black', boxstyle='round,pad=0.5'))

# Draw the arrows and labels
arrowprops = dict(facecolor='black', arrowstyle='->')

# Initial Client Authentication Request
ax.annotate('', xy=(kdc_pos[0], kdc_pos[1] - 0.3), xytext=(client_pos[0], client_pos[1] - 0.3), arrowprops=arrowprops)
ax.text((client_pos[0] + kdc_pos[0]) / 2, client_pos[1] - 0.4, "1. Request TGT", fontsize=10, ha='center')

# KDC Verification and TGT Issuance
ax.annotate('', xy=(client_pos[0], client_pos[1] - 0.6), xytext=(kdc_pos[0], kdc_pos[1] - 0.6), arrowprops=arrowprops)
ax.text((client_pos[0] + kdc_pos[0]) / 2, client_pos[1] - 0.7, "2. TGT & Session Key", fontsize=10, ha='center')

# Client Decrypts Message
ax.text(client_pos[0], client_pos[1] - 0.9, "3. Decrypt TGT & Session Key", fontsize=10, ha='center')

# TGT to Request Access
ax.annotate('', xy=(kdc_pos[0], kdc_pos[1] - 1.2), xytext=(client_pos[0], client_pos[1] - 1.2), arrowprops=arrowprops)
ax.text((client_pos[0] + kdc_pos[0]) / 2, client_pos[1] - 1.3, "4. Request Service Ticket", fontsize=10, ha='center')

# KDC Creates Service Ticket
ax.annotate('', xy=(client_pos[0], client_pos[1] - 1.5), xytext=(kdc_pos[0], kdc_pos[1] - 1.5), arrowprops=arrowprops)
ax.text((client_pos[0] + kdc_pos[0]) / 2, client_pos[1] - 1.6, "5. Service Ticket", fontsize=10, ha='center')

# Client Uses Service Ticket
ax.annotate('', xy=(server_pos[0], server_pos[1] - 1.8), xytext=(client_pos[0], client_pos[1] - 1.8), arrowprops=arrowprops)
ax.text((client_pos[0] + server_pos[0]) / 2, client_pos[1] - 1.9, "6. Access Request", fontsize=10, ha='center')

# Target Server Authentication
ax.annotate('', xy=(client_pos[0], client_pos[1] - 2.1), xytext=(server_pos[0], server_pos[1] - 2.1), arrowprops=arrowprops)
ax.text((client_pos[0] + server_pos[0]) / 2, client_pos[1] - 2.2, "7. Access Granted", fontsize=10, ha='center')

# Remove axis
ax.axis('off')

# Show the diagram
plt.show()
