# Querying a NoSQL (MongoDB) collection
# Demonstrating performance tracking for unstructured data retrieval
import pymongo
import time

def query_nosql_collection(collection_name):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["dbms_analysis"]
    collection = db[collection_name]
    
    start_time = time.time()
    # Query optimized for document-based retrieval
    results = collection.find({"category": "optimization"}).hint([("category", 1)]) 
    latency = (time.time() - start_time) * 1000
    
    print(f"NoSQL Query Latency: {latency:.2f} ms")