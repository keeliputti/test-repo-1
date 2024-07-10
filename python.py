import json
import numpy as np
from qpython.qcollection import qlist
from qpython.qtype import QSYMBOL_LIST

# Create a QList object
Column = qlist(np.array(['col name']), qtype=QSYMBOL_LIST)

# Custom serialization method for QList
def serialize_qlist(qlist_obj):
    return json.dumps({
        'data': qlist_obj.data.tolist(),  # Convert numpy array to list
        'qtype': qlist_obj.meta.qtype     # Include qtype for proper deserialization
    })

# Serialize the QList object
serialized_column = serialize_qlist(Column)
print(serialized_column)


import json
import numpy as np
from qpython.qcollection import qlist
from qpython.qtype import QSYMBOL_LIST

# Custom deserialization method for QList
def deserialize_qlist(serialized_str):
    data = json.loads(serialized_str)
    return qlist(np.array(data['data']), qtype=data['qtype'])

# Simulate receiving serialized QList
serialized_column = '{"data": ["col name"], "qtype": -11}'

# Deserialize the QList object
Column = deserialize_qlist(serialized_column)
print(Column)
