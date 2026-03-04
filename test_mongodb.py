from pymongo.mongo_client import MongoClient
import certifi

uri = "mongodb+srv://maadhavmanoj21_db_user:Admin123@cluster0.fk4ozyq.mongodb.net/?appName=Cluster0"

ca = certifi.where()

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)