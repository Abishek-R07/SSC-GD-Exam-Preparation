# SSC GD Examination Preparation Web Application

A full-stack web application for SSC GD Constable exam preparation built with Flask and MongoDB.

## Features

- **User Management**: Registration, login, profile management with JWT authentication
- **Study Materials**: Upload, download, and categorize study materials by subject
- **Question Bank**: Topic-wise MCQs with previous year questions
- **Mock Tests**: Timer-based mock tests with automatic scoring
- **Performance Analysis**: Instant results and detailed performance analytics
- **Admin Panel**: Complete system management for users, materials, questions, and tests

## Technology Stack

- **Backend**: Python Flask (RESTful API)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: MongoDB (NoSQL)
- **Authentication**: JWT-based secure authentication

## Installation

### Prerequisites

1. Python 3.8 or higher
2. MongoDB installed and running
3. pip (Python package manager)

### Step 1: Install Dependencies

```bash
cd "c:\Users\abishek R\OneDrive\Desktop\SSC GD"
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables

The `.env` file is already created with default values. Update if needed:

```env
MONGODB_URI=mongodb://localhost:27017/ssc_gd_exam
SECRET_KEY=ssc-gd-exam-secret-key-2024
JWT_SECRET_KEY=jwt-token-secret-key-2024
FLASK_ENV=development
```

### Step 3: Start MongoDB

Make sure MongoDB is running on your system:

**Windows:**
```bash
mongod
```

**Linux/Mac:**
```bash
sudo systemctl start mongod
```

### Step 4: Run the Application

```bash
python run.py
```

The application will start on `http://localhost:5000`

## Project Structure

```
SSC GD/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── config.py                # Configuration settings
│   ├── models/
│   │   ├── user.py              # User model
│   │   ├── question.py          # Question model
│   │   ├── study_material.py    # Study material model
│   │   ├── mock_test.py         # Mock test model
│   │   └── result.py            # Result model
│   ├── routes/
│   │   ├── auth.py              # Authentication routes
│   │   ├── user.py              # User management routes
│   │   ├── study_materials.py   # Study material routes
│   │   ├── questions.py         # Question bank routes
│   │   ├── mock_tests.py        # Mock test routes
│   │   ├── results.py           # Result analysis routes
│   │   └── admin.py             # Admin routes
│   ├── middleware/
│   │   └── auth_middleware.py   # JWT authentication middleware
│   ├── utils/
│   │   └── helpers.py           # Helper functions
│   └── templates/               # HTML templates
├── static/
│   ├── css/                     # Stylesheets
│   └── js/                      # JavaScript files
├── uploads/                     # Uploaded study materials
├── .env                         # Environment variables
├── requirements.txt             # Python dependencies
└── run.py                       # Application entry point
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/verify-token` - Verify JWT token

### User Management
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update profile
- `GET /api/user/dashboard` - Get dashboard data

### Study Materials
- `GET /api/study-materials/` - Get all materials
- `GET /api/study-materials/subjects` - Get subjects
- `GET /api/study-materials/<id>` - Get material by ID
- `POST /api/study-materials/` - Create material (Admin)
- `PUT /api/study-materials/<id>` - Update material (Admin)
- `DELETE /api/study-materials/<id>` - Delete material (Admin)

### Questions
- `GET /api/questions/` - Get questions with filters
- `GET /api/questions/subjects` - Get subjects
- `GET /api/questions/topics` - Get topics
- `GET /api/questions/random` - Get random questions
- `POST /api/questions/` - Create question (Admin)
- `POST /api/questions/bulk` - Bulk upload questions (Admin)
- `PUT /api/questions/<id>` - Update question (Admin)
- `DELETE /api/questions/<id>` - Delete question (Admin)

### Mock Tests
- `GET /api/mock-tests/` - Get all tests
- `GET /api/mock-tests/<id>` - Get test by ID
- `POST /api/mock-tests/<id>/start` - Start test
- `POST /api/mock-tests/submit` - Submit test
- `POST /api/mock-tests/` - Create test (Admin)
- `PUT /api/mock-tests/<id>` - Update test (Admin)
- `DELETE /api/mock-tests/<id>` - Delete test (Admin)

### Results
- `GET /api/results/my-results` - Get user's results
- `GET /api/results/statistics` - Get performance stats
- `GET /api/results/<id>` - Get result by ID
- `GET /api/results/test/<test_id>` - Get test results (Admin)

### Admin
- `GET /api/admin/dashboard` - Admin dashboard
- `GET /api/admin/users` - Get all users
- `PUT /api/admin/users/<id>` - Update user
- `DELETE /api/admin/users/<id>` - Delete user
- `GET /api/admin/system-status` - System status

## Database Collections

### Users
```javascript
{
  _id: ObjectId,
  name: String,
  email: String (unique),
  password: String (hashed),
  role: String (user/admin),
  profile: { phone, age, education, state },
  createdAt: Date,
  updatedAt: Date
}
```

### Questions
```javascript
{
  _id: ObjectId,
  subject: String,
  topic: String,
  questionText: String,
  options: [String],
  correctAnswer: Number (0-3),
  difficulty: String,
  year: Number,
  tags: [String],
  createdBy: ObjectId,
  createdAt: Date
}
```

### StudyMaterials
```javascript
{
  _id: ObjectId,
  title: String,
  subject: String,
  topic: String,
 description: String,
  fileUrl: String,
  fileType: String,
  uploadedBy: ObjectId,
  downloadCount: Number,
  createdAt: Date
}
```

### MockTests
```javascript
{
  _id: ObjectId,
  testName: String,
 description: String,
  duration: Number (minutes),
  totalQuestions: Number,
  subjects: [{ subject, questionCount }],
  difficulty: String,
  isActive: Boolean,
  createdBy: ObjectId,
  createdAt: Date
}
```

### Results
```javascript
{
  _id: ObjectId,
  userId: ObjectId,
  testId: ObjectId,
  answers: [{ questionId, selectedOption, isCorrect }],
  score: Number,
  totalMarks: Number,
  accuracy: Number,
  timeTaken: Number (seconds),
  attempted: Number,
  correct: Number,
  incorrect: Number,
  submittedAt: Date
}
```

## Usage Examples

### Register a New User

```bash
curl -X POST http://localhost:5000/api/auth/register\
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "SecurePass123"
  }'
```

### Login

```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "SecurePass123"
  }'
```

### Get Study Materials

```bash
curl -X GET "http://localhost:5000/api/study-materials?subject=Mathematics"
```

### Start Mock Test

```bash
curl -X POST http://localhost:5000/api/mock-tests/<test_id>/start \
  -H "Authorization: Bearer <your_token>"
```

### Submit Test

```bash
curl -X POST http://localhost:5000/api/mock-tests/submit \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "testId": "<test_id>",
    "answers": [
      {"questionId": "<q1>", "selectedOption": 2},
      {"questionId": "<q2>", "selectedOption": 1}
    ],
    "timeTaken": 1200
  }'
```

## Security Features

- Password hashing with bcrypt
- JWT token-based authentication
- Role-based access control (Admin/User)
- Input validation and sanitization
- CORS enabled for cross-origin requests
- Secure file upload validation

## Development

### Running in Development Mode

The application runs in development mode by default. For production:

```bash
export FLASK_ENV=production
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Testing APIs

You can use Postman or curl to test the API endpoints. All authenticated endpoints require a valid JWT token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## Creating Admin User

To create an admin user, register normally first, then manually update the role in MongoDB:

```javascript
db.Users.updateOne(
  { email: "admin@example.com" },
  { $set: { role: "admin" } }
)
```

Or use the admin panel if you have database access.

## Troubleshooting

### MongoDB Connection Error
- Ensure MongoDB is running
- Check MONGODB_URI in.env file
- Verify MongoDB port (default: 27017)

### Module Not Found Errors
- Run `pip install -r requirements.txt`
- Ensure you're in the project directory

### Port Already in Use
- Change port in run.py: `app.run(port=5001)`
- Or stop the process using port 5000

## Future Enhancements

- Frontend UI implementation
- Email verification for new users
- Password reset functionality
- Advanced analytics dashboard
- Mobile app integration
- Cloud storage for files
- Real-time leaderboards
- Discussion forums

## License

This project is open-source and available for educational purposes.

## Support

For issues or questions, please create an issue in the repository or contact the development team.

---

**Built with ❤️ for SSC GD Aspirants**
