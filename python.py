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

# Create a new figure
fig, ax = plt.subplots(figsize=(10, 8))

# Define positions
client_pos = (1, 7)
kdc_pos = (5, 7)
as_pos = (5, 6)
tgs_pos = (5, 4)
server_pos = (9, 7)

# Draw entities
ax.text(*client_pos, "Client", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightblue', edgecolor='black'))
ax.text(*kdc_pos, "Key Distribution Center (KDC)", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightgreen', edgecolor='black'))
ax.text(*as_pos, "Authentication Server (AS)", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightyellow', edgecolor='black'))
ax.text(*tgs_pos, "Ticket Granting Server (TGS)", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightyellow', edgecolor='black'))
ax.text(*server_pos, "Server", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightcoral', edgecolor='black'))

# Draw arrows and labels for protocol flow
flow_steps = [
    (client_pos, as_pos, "Initial Client Authentication Request"),
    (as_pos, client_pos, "AS Issues TGT and SK1"),
    (client_pos, tgs_pos, "Client Uses TGT to Request Service Ticket"),
    (tgs_pos, client_pos, "TGS Issues Service Ticket"),
    (client_pos, server_pos, "Client Sends Service Ticket to Server"),
    (server_pos, client_pos, "Server Verifies Client and Grants Access"),
]

for start_pos, end_pos, text in flow_steps:
    ax.annotate(
        text,
        xy=end_pos, xycoords='data',
        xytext=start_pos, textcoords='data',
        arrowprops=dict(arrowstyle="->", color='black'),
        bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'),
        ha='center',
        va='center',
        fontsize=10
    )

# Set axis limits and hide axes
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Display the diagram
plt.show()
