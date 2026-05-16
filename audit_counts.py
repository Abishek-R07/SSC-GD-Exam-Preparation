
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def audit_counts():
    uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/ssc_gd_exam')
    client = MongoClient(uri)
    db = client.get_database()
    
    subjects = db['Questions'].distinct('subject')
    print("Subject Counts:")
    for subject in subjects:
        subj_name = str(subject) if subject is not None else "None"
        count = db['Questions'].count_documents({'subject': subject})
        print(f"| {subj_name:30} | {count:5} |")

if __name__ == "__main__":
    audit_counts()
