# AI Job Agent

An AI-powered job application assistant that helps analyze job descriptions, optimize resumes, and track applications.

## 🚀 Quick Start

### Prerequisites
- **Python 3.9+** (for backend)
- **Node.js 18+** (for frontend)
- **Git**

### 🔧 Backend Setup (Python/FastAPI)

1. **Clone and navigate to the project:**
```bash
git clone <your-repo-url>
cd AIJobAgent/backend
```

2. **Create and activate virtual environment:**
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

3. **Install dependencies:**
```bash
# Recommended: Install exact versions for reproducible environment
pip install -r requirements.txt

# Alternative: Install main packages only (more flexible)
pip install -r requirements.in
```

4. **Set up environment variables:**
```bash
# Copy .env template and add your API keys
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

5. **Run the backend server:**
```bash
uvicorn main:app --reload
```
Backend will be available at: **http://localhost:8000**

### 🎨 Frontend Setup (Next.js/React)

1. **Navigate to frontend directory:**
```bash
cd ../frontend
```

2. **Install dependencies:**
```bash
npm install
# or
yarn install
```

3. **Set up environment variables:**
```bash
# Copy environment template
cp .env.local.example .env.local
# Edit .env.local if needed (API URL should point to backend)
```

4. **Run the development server:**
```bash
npm run dev
# or
yarn dev
```
Frontend will be available at: **http://localhost:3000**

## 📦 Project Structure

```
AIJobAgent/
├── backend/                 # Python FastAPI backend
│   ├── agents/             # AI agents (job analyzer, resume editor)
│   ├── database/           # Database models and schema
│   ├── scraping/           # Web scraping utilities
│   ├── main.py            # FastAPI application entry point
│   ├── config.py          # Configuration settings
│   ├── requirements.txt    # Python dependencies (exact versions)
│   ├── requirements.in     # Main dependencies (curated list)
│   └── REQUIREMENTS.md     # Dependency management explanation
├── frontend/               # Next.js React frontend
│   ├── src/
│   │   ├── app/           # Next.js app router pages
│   │   ├── components/    # React components
│   │   └── lib/          # Utilities and API client
│   ├── package.json       # Node.js dependencies
│   └── tailwind.config.ts # Tailwind CSS configuration
└── README.md              # This file
```

## 🔑 Environment Variables

### Backend (.env)
```bash
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./jobs.db
```

### Frontend (.env.local)
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🛠️ Development Commands

### Backend
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install new packages and update requirements
pip install <package-name>
echo "<package-name>==<version>" >> requirements.in  # Add to main list
pip freeze > requirements.txt  # Update full dependency tree

# Run server with auto-reload
uvicorn main:app --reload

# Run server in production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend
```bash
# Development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Lint code
npm run lint
```

## 🚀 Features

- **Job Analysis**: AI-powered analysis of job descriptions using LangChain and OpenAI
- **Resume Optimization**: Automatically optimize resumes for specific job applications
- **Job Scraping**: Find and scrape job opportunities from various sources
- **Application Tracking**: Track job applications and their status
- **Modern UI**: Responsive design with Tailwind CSS and TypeScript

## 📋 API Endpoints

- `GET /` - Health check
- `POST /analyze` - Analyze job description
- `GET /jobs` - Get all jobs
- `POST /scrape` - Scrape jobs from sources

## 🐳 Docker Support (Coming Soon)

```bash
# Build and run with Docker Compose
docker-compose up --build
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Backend Issues
- **Import errors**: Make sure virtual environment is activated
- **Missing packages**: Run `pip install -r requirements.txt`
- **API key errors**: Check your `.env` file has valid `OPENAI_API_KEY`

### Frontend Issues
- **Module not found**: Run `npm install` to install dependencies
- **Build errors**: Check Node.js version (requires 18+)
- **API connection**: Verify backend is running on `http://localhost:8000`

## 📞 Support

If you encounter any issues, please:
1. Check the troubleshooting section above
2. Search existing GitHub issues
3. Create a new issue with detailed error information