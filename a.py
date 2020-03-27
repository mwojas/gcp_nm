import firebase_admin
from firebase_admin import credentials

import random

# cred = credentials.Cert('path/to/serviceKey.json')
cred = firebase_admin.credentials.Certificate('path/to/serviceKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://qwiklabs-gcp-03-5addf9d90e77.firebaseio.com'
})

from firebase_admin import db

root = db.reference()
# Add a new user under /users.


for i in range(1000):
    print(str(i))

    new_user = root.child('users').push({
        'name' : str(i), 
        'since' : 1700
    })

# Update a child attribute of the new user.
new_user.update({'since' : 1799})

# Obtain a new reference to the user, and retrieve child data.
# Result will be made available as a Python dict.
mary = db.reference('users/{0}'.format(new_user.key)).get()
print('Name:', mary['name'])
print('Since:', mary['since'])

