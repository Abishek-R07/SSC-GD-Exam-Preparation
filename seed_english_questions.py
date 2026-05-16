
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

def seed_english_questions():
    uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/ssc_gd_exam')
    print(f"Connecting to: {uri}")
    client = MongoClient(uri)
    db = client.get_database()
    collection = db['Questions']
    
    questions = [
        {
            'subject': 'English',
            'topic': 'Synonyms & Antonyms',
            'questionText': 'Select the most appropriate SYNONYM of the given word: "ABANDON"',
            'options': ['Keep', 'Forsake', 'Support', 'Adopt'],
            'correctAnswer': 1,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Synonyms & Antonyms',
            'questionText': 'Select the most appropriate ANTONYM of the given word: "BRIGHT"',
            'options': ['Shining', 'Luminous', 'Dull', 'Vibrant'],
            'correctAnswer': 2,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'One Word Substitution',
            'questionText': 'A person who is unable to pay his debts:',
            'options': ['Solvent', 'Bankrupt', 'Lent', 'Borrower'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Idioms & Phrases',
            'questionText': 'Select the meaning of the given idiom: "A piece of cake"',
            'options': ['Something very difficult', 'Something very easy', 'A tasty food item', 'To celebrate a victory'],
            'correctAnswer': 1,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Spotting Errors',
            'questionText': 'Identify the segment that contains a grammatical error: "The children/ is playing/ in the garden."',
            'options': ['The children', 'is playing', 'in the', 'garden.'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Fill in the Blanks',
            'questionText': 'She is _____ than her sister.',
            'options': ['tall', 'taller', 'tallest', 'more tall'],
            'correctAnswer': 1,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Sentence Improvement',
            'questionText': 'Improve the underlined part: "He **do not** like coffee."',
            'options': ['does not like', 'did not liked', 'do not likes', 'No improvement'],
            'correctAnswer': 0,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Spelling Errors',
            'questionText': 'Select the correctly spelled word:',
            'options': ['Accommodeate', 'Accomodate', 'Accommodate', 'Acommodate'],
            'correctAnswer': 2,
            'difficulty': 'Hard',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'One Word Substitution',
            'questionText': 'A place where birds are kept:',
            'options': ['Zoo', 'Apiary', 'Aviary', 'Aquarium'],
            'correctAnswer': 2,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Idioms & Phrases',
            'questionText': 'What is the meaning of "Once in a blue moon"?',
            'options': ['Frequently', 'Very rarely', 'Every month', 'At night'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Fill in the Blanks',
            'questionText': 'The train _____ before I reached the station.',
            'options': ['left', 'has left', 'had left', 'leaves'],
            'correctAnswer': 2,
            'difficulty': 'Hard',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Synonyms & Antonyms',
            'questionText': 'Select the ANTONYM of "GENEROUS":',
            'options': ['Kind', 'Stingy', 'Brave', 'Noble'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Spotting Errors',
            'questionText': 'If I was you,/ I would have/ accepted the offer.',
            'options': ['If I was you,', 'I would have', 'accepted the offer.', 'No error'],
            'correctAnswer': 0,
            'difficulty': 'Hard',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'One Word Substitution',
            'questionText': 'A person who loves books:',
            'options': ['Philanthropist', 'Bibliophile', 'Optimist', 'Polyglot'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Spelling Errors',
            'questionText': 'Which of the following is correctly spelled?',
            'options': ['Recieve', 'Receive', 'Receve', 'Recieve'],
            'correctAnswer': 1,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Fill in the Blanks',
            'questionText': 'He is afraid _____ dogs.',
            'options': ['from', 'of', 'with', 'to'],
            'correctAnswer': 1,
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Sentence Improvement',
            'questionText': 'Improve the underlined part: "Neither Ram nor his friends **is** present."',
            'options': ['are', 'were', 'am', 'No improvement'],
            'correctAnswer': 0,
            'difficulty': 'Hard',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Idioms & Phrases',
            'questionText': '"To bell the cat" means:',
            'options': ['To play with a cat', 'To take a great risk', 'To face defeat', 'To be very happy'],
            'correctAnswer': 1,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Synonyms & Antonyms',
            'questionText': 'Find the SYNONYM of "CANDID":',
            'options': ['Frank', 'Secretive', 'Dishonest', 'Vague'],
            'correctAnswer': 0,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'English',
            'topic': 'Spotting Errors',
            'questionText': 'Each of the students/ have finished/ their homework.',
            'options': ['Each of the students', 'have finished', 'their homework.', 'No error'],
            'correctAnswer': 1,
            'difficulty': 'Hard',
            'createdAt': datetime.utcnow()
        }
    ]
    
    result = collection.insert_many(questions)
    print(f"Successfully inserted {len(result.inserted_ids)} questions into English module.")

if __name__ == "__main__":
    seed_english_questions()
