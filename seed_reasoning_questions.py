
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

def seed_questions():
    uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/ssc_gd_exam')
    print(f"Connecting to: {uri}")
    client = MongoClient(uri)
    db = client.get_database()
    collection = db['Questions']
    
    questions = [
        {
            'subject': 'Reasoning',
            'topic': 'Series Completion',
            'questionText': 'Find the missing number in the series: 2, 6, 12, 20, ?',
            'options': ['28', '30', '32', '36'],
            'correctAnswer': 1,  # 30
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Alphabet Series',
            'questionText': 'Find the missing term: A, C, F, J, ?',
            'options': ['M', 'N', 'O', 'P'],
            'correctAnswer': 2,  # O
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Coding-Decoding',
            'questionText': 'If CAT is coded as DBU, then how is DOG coded?',
            'options': ['EPH', 'EOH', 'DPH', 'FQI'],
            'correctAnswer': 0,  # EPH
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Blood Relations',
            'questionText': 'A is the brother of B. B is the mother of C. How is A related to C?',
            'options': ['Father', 'Uncle', 'Brother', 'Grandfather'],
            'correctAnswer': 1,  # Uncle
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Direction Sense',
            'questionText': 'A person walks 10m north, then 5m east. In which direction is he now from the starting point?',
            'options': ['North', 'East', 'North-East', 'North-West'],
            'correctAnswer': 2,  # North-East
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Clock & Calendar',
            'questionText': 'How many days are there in a leap year?',
            'options': ['364', '365', '366', '367'],
            'correctAnswer': 2,  # 366
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Analogy',
            'questionText': 'Cow : Milk :: Hen : ?',
            'options': ['Egg', 'Meat', 'Feather', 'Nest'],
            'correctAnswer': 0,  # Egg
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Classification',
            'questionText': 'Find the odd one out from the following options:',
            'options': ['Apple', 'Banana', 'Mango', 'Carrot'],
            'correctAnswer': 3,  # Carrot
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Venn Diagram',
            'questionText': 'Which of the following diagrams correctly represents the relationship among: Students, Boys, Girls?',
            'options': ['All students are boys', 'All boys are girls', 'Both Boys and Girls are inside the Students category', 'Only Boys are students'],
            'correctAnswer': 2,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Non-Verbal Reasoning',
            'questionText': 'Find the mirror image of the letter "P" when the mirror is placed to its right.',
            'options': ['P', 'q', 'b', 'd'],
            'correctAnswer': 1,  # q
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Paper Folding',
            'questionText': 'A square paper is folded twice and a small cut is made in the center. How many holes will be visible when the paper is completely unfolded?',
            'options': ['1', '2', '4', '8'],
            'correctAnswer': 2,  # 4
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Mathematical Operations',
            'questionText': 'If "+" means "×", then what is the value of 2 + 3?',
            'options': ['5', '1', '6', '0'],
            'correctAnswer': 2,  # 6
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Missing Term',
            'questionText': 'Identify the next term in the series: 3, 9, 27, ?',
            'options': ['54', '81', '108', '120'],
            'correctAnswer': 1,  # 81
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Statement & Conclusion',
            'questionText': 'Statement: All cats are animals. Conclusion: All animals are cats.',
            'options': ['Conclusion is True', 'Conclusion is False', 'Partially True', 'Data Inadequate'],
            'correctAnswer': 1,  # False
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Seating Arrangement',
            'questionText': 'A sits to the left of B. B sits to the left of C. Who is sitting in the middle?',
            'options': ['A', 'B', 'C', 'None of these'],
            'correctAnswer': 1,  # B
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Syllogism',
            'questionText': 'Statements: All pens are blue. Some blue are books. Conclusion: Are some pens definitely books?',
            'options': ['Yes', 'No', 'Cannot be determined', 'Partially Yes'],
            'correctAnswer': 2,  # Cannot be determined
            'difficulty': 'Hard',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Word Formation',
            'questionText': 'How many meaningful english words can be formed using the letters of the word "SCHOOL"?',
            'options': ['1', '2', '3', 'More than 3'],
            'correctAnswer': 3,
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Series Completion',
            'questionText': 'Find the next term: 1A, 2B, 3C, ?',
            'options': ['4C', '4D', '5D', '3D'],
            'correctAnswer': 1,  # 4D
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Ranking Test',
            'questionText': 'Ram is 5th from the top and 3rd from the bottom in a merit list. How many total students are there in the list?',
            'options': ['7', '8', '9', '6'],
            'correctAnswer': 0,  # 5+3-1 = 7
            'difficulty': 'Medium',
            'createdAt': datetime.utcnow()
        },
        {
            'subject': 'Reasoning',
            'topic': 'Input-Output',
            'questionText': 'If an Input-Output machine processes strings by reversing them, what will be the output for the input "HELLO"?',
            'options': ['HELLO', 'OLLEH', 'HELOL', 'LHLOE'],
            'correctAnswer': 1,  # OLLEH
            'difficulty': 'Easy',
            'createdAt': datetime.utcnow()
        }
    ]
    
    result = collection.insert_many(questions)
    print(f"Successfully inserted {len(result.inserted_ids)} questions into Reasoning module.")

if __name__ == "__main__":
    seed_questions()
