import sys
import firebase_admin
from firebase_admin import credentials, firestore

if len(sys.argv) != 5:
    raise("Must provide four arguments 1) indicating which device to use 2) version number 3) storage bucket endpoint 4) serviceAccountKey.json path")

device_type = sys.argv[1]
version = sys.argv[2]
endpoint = sys.argv[3]
serviceAccountKeyPath = sys.argv[4]

cred = credentials.Certificate(serviceAccountKeyPath)
firebase_admin.initialize_app(cred)

print(device_type)
if device_type == "fertigation-system" or device_type == "climate-controller":
    firestore_db = firestore.client()
    firestore_db.collection(u'deviceVersions').document(device_type).set({
        u'endpoint': endpoint,
        u'version': version
    })
else:
    raise("Invalid device type specified. Device type must either be climate-controller or fertigation-system")


