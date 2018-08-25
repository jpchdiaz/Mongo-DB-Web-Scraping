from Flask import Flask, render_template
import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# @TODO: connect to mongo db and collection
db = client.store_inventory
collection = db.produce

# db.produce.drop()

#create some dictionaries
db.collection.insert_many([
  {
      "type": "Apples",
      "cost": .23,
      "stock": 333
  },
  {
      "type": "Bananas",
      "cost": .13,
      "stock": 32
  },
  {
      "type": "Mangos",
      "cost": .89,
      "stock": 1283
  },
  {
      "type": "Tomatos",
      "cost": .78,
      "stock": 474
  },
  {
      "type": "Dragonfruit",
      "cost": .40,
      "stock": 2363
  }
]
)

print('Data Uploaded')
