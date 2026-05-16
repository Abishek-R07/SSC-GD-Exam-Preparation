
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

def seed_gk_questions():
    uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/ssc_gd_exam')
    print(f"Connecting to: {uri}")
    client = MongoClient(uri)
    db = client.get_database()
    collection = db['Questions']
    
    questions = [
        {
            'subject': 'General Knowledge',
            'topic': 'Indian Polity',
            'questionText': 'Who was the Chairman of the Drafting Committee of the Indian Constitution?',
            'options': ['Dr. Rajendra Prasad', 'Jawaharlal Nehru', 'Dr. B.R. Ambedkar', 'Sardar Patel'],
            'correctAnswer': 2,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Geography',
            'questionText': 'Which is the longest river in India?',
            'options': ['Godavari', 'Ganga', 'Brahmaputra', 'Yamuna'],
            'correctAnswer': 1,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Indian History',
            'questionText': 'The Quit India Movement was started by Mahatma Gandhi in which year?',
            'options': ['1930', '1940', '1942', '1945'],
            'correctAnswer': 2,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'General Science',
            'questionText': 'What is the chemical symbol for Gold?',
            'options': ['Ag', 'Gd', 'Fe', 'Au'],
            'correctAnswer': 3,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Static GK',
            'questionText': 'Which is the largest planet in our solar system?',
            'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
            'correctAnswer': 2,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Indian History',
            'questionText': 'Who was the founder of the Maurya Empire?',
            'options': ['Ashoka', 'Chandragupta Maurya', 'Bindusara', 'Chanakya'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Geography',
            'questionText': 'Which state in India is known as the "Spice Garden of India"?',
            'options': ['Karnataka', 'Kerala', 'Tamil Nadu', 'Andhra Pradesh'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Indian Polity',
            'questionText': 'The President of India can be removed from office through impeachment for violation of the Constitution under which Article?',
            'options': ['Article 52', 'Article 61', 'Article 72', 'Article 74'],
            'correctAnswer': 1,
            'difficulty': 'Hard',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'General Science',
            'questionText': 'Which vitamin is synthesized in the human body with the help of sunlight?',
            'options': ['Vitamin A', 'Vitamin B', 'Vitamin C', 'Vitamin D'],
            'correctAnswer': 3,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Static GK',
            'questionText': 'Where is the headquarters of the World Health Organization (WHO) located?',
            'options': ['New York', 'Paris', 'Geneva', 'London'],
            'correctAnswer': 2,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Indian Economy',
            'questionText': 'Which organization in India regulates the monetary policy?',
            'options': ['SEBI', 'NABARD', 'RBI', 'Ministry of Finance'],
            'correctAnswer': 2,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Geography',
            'questionText': 'The "Mount Everest" is located in which mountain range?',
            'options': ['Alps', 'Himalayas', 'Andes', 'Rockies'],
            'correctAnswer': 1,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Indian History',
            'questionText': 'Who was the first female ruler of the Delhi Sultanate?',
            'options': ['Nur Jahan', 'Razia Sultan', 'Chand Bibi', 'Rani Lakshmibai'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'General Science',
            'questionText': 'Which instrument is used to measure humidity?',
            'options': ['Barometer', 'Thermometer', 'Hygrometer', 'Anemometer'],
            'correctAnswer': 2,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Static GK',
            'questionText': 'When is "World Environment Day" celebrated annually?',
            'options': ['June 5', 'July 11', 'September 16', 'October 24'],
            'correctAnswer': 0,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Indian Polity',
            'questionText': 'The Minimum age required for a person to become the Prime Minister of India if he is a member of Lok Sabha is?',
            'options': ['25 years', '30 years', '35 years', '21 years'],
            'correctAnswer': 0,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'General Science',
            'questionText': 'Which blood group is known as the "Universal Donor"?',
            'options': ['Group AB', 'Group A', 'Group B', 'Group O'],
            'correctAnswer': 3,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Geography',
            'questionText': 'Which Indian state has the longest coastline?',
            'options': ['Maharashtra', 'Gujarat', 'Tamil Nadu', 'Andhrra Pradesh'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Indian History',
            'questionText': 'Who was the first Governor-General of India?',
            'options': ['Lord Canning', 'Warren Hastings', 'Lord Mountbatten', 'Lord Dalhousie'],
            'correctAnswer': 1,
            'difficulty': 'Hard',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'General Knowledge',
            'topic': 'Current Affairs',
            'questionText': 'Which country hosted the G20 Summit in 2023?',
            'options': ['Indonesia', 'India', 'Brazil', 'USA'],
            'correctAnswer': 1,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        }
    ]
    
    result = collection.insert_many(questions)
    print(f"Successfully inserted {len(result.inserted_ids)} questions into General Knowledge module.")

if __name__ == "__main__":
    seed_gk_questions()
