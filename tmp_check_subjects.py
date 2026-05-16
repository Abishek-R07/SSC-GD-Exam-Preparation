
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def check_subjects():
    uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/ssc_gd_exam')
    print(f"Connecting to: {uri}")
    client = MongoClient(uri)
    db = client.get_database()
    
    collections = db.list_collection_names()
    print(f"Collections: {collections}")
    
    if 'Questions' in collections:
        subjects = db['Questions'].distinct('subject')
        print("Existing subjects:", subjects)
        
        for subject in subjects:
            topics = db['Questions'].distinct('topic', {'subject': subject})
            print(f"Topics for {subject}:", topics)
            count = db['Questions'].count_documents({'subject': subject})
            print(f"Count for {subject}: {count}")
    else:
        print("Questions collection not found!")

if __name__ == "__main__":
    check_subjects()
