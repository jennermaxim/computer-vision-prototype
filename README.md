# AI-Powered Learning Platform

An intelligent system that recognizes and translates real-world community challenges into structured learning missions using OpenAI's GPT-4 Vision and Language APIs.

## 🎯 Project Overview

This system demonstrates three core capabilities:

### Task (a): Computer Vision Prototype

Detects visible community issues across multiple domains:

- **Environment**: littered streets, blocked drainage, deforestation, poor waste disposal
- **Health**: overcrowded clinics, lack of safety gear, unsanitary public spaces
- **Education**: overcrowded classrooms, damaged infrastructure, lack of learning materials

### Task (b): Mission Statement Generation

Converts user-written problem descriptions into formalized, project-oriented mission statements using NLP/LLM.

**Example:**

- Input: "our street is always flooded when it rains"
- Output: A comprehensive mission statement with goals, impact, and action steps

### Task (c): Problem Classification Engine

Automatically categorizes identified problems into one of three categories:

- Environment
- Health
- Education

## 🚀 Features

- **Image Analysis**: Upload images or provide URLs for community issue detection
- **Text Processing**: Convert informal problem descriptions into structured missions
- **Smart Classification**: AI-powered categorization with confidence scoring
- **Integrated Workflow**: Seamless pipeline from detection to mission creation
- **Interactive Mode**: User-friendly CLI for testing all features

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Dependencies (see requirements.txt)

## 🔧 Installation

1. **Clone or navigate to the project directory**

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set up your OpenAI API key**:

   Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## 💻 Usage

### Run All Demonstrations

```bash
python main.py demo-all
```

### Task-Specific Demos

**Task (a) - Vision Detection:**

```bash
python main.py demo-vision
```

**Task (b) - Mission Statement Generation:**

```bash
python main.py demo-text
```

**Task (c) - Problem Classification:**

```bash
python main.py demo-classification
```

### Interactive Mode

```bash
python main.py interactive
```

## 📚 API Usage Examples

### 1. Computer Vision Detection

```python
from vision_detector import CommunityIssueDetector

detector = CommunityIssueDetector()

# Analyze an image
result = detector.detect_issues("path/to/image.jpg")

print(result['analysis'])
```

### 2. Mission Statement Generation

```python
from mission_generator import MissionStatementGenerator

generator = MissionStatementGenerator()

# Generate a mission statement
result = generator.generate_mission_statement(
    "our street is always flooded when it rains"
)

print(result['mission_statement'])
print(result['action_steps'])
```

### 3. Problem Classification

```python
from problem_classifier import ProblemClassifier

classifier = ProblemClassifier()

# Classify a problem
result = classifier.classify_problem(
    "The streets are filled with plastic waste"
)

print(f"Category: {result['category']}")
print(f"Confidence: {result['confidence']}")
```

### 4. Integrated System

```python
from integrated_system import AILearningPlatform

platform = AILearningPlatform()

# Process an image (complete workflow)
result = platform.process_image("path/to/image.jpg")
print(result['summary'])

# Process a text description
result = platform.process_text_description(
    "our school has broken desks"
)
print(result['summary'])
```

## 🏗️ Project Structure

```
computer-vision-prototype/
├── config.py                 # Configuration and settings
├── vision_detector.py        # Task (a): Computer vision module
├── mission_generator.py      # Task (b): Mission statement generator
├── problem_classifier.py     # Task (c): Problem classifier
├── integrated_system.py      # Integrated platform combining all tasks
├── main.py                   # Main demo and interactive interface
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🔑 Key Components

### `CommunityIssueDetector`

Uses GPT-4 Vision to analyze images and detect community issues across multiple domains.

### `MissionStatementGenerator`

Leverages GPT-4 to transform informal problem descriptions into structured, actionable mission statements.

### `ProblemClassifier`

Employs GPT-4 to categorize problems into Environment, Health, or Education with confidence scoring.

### `AILearningPlatform`

Integrates all components into a seamless workflow for complete problem analysis.

## 📊 Example Output

```
======================================================================
                    COMMUNITY ISSUE ANALYSIS SUMMARY
======================================================================

🔍 VISION ANALYSIS:
----------------------------------------------------------------------
DETECTED ISSUES:
1. Environment - Severe littering on streets (High severity)
   Visual Evidence: Multiple plastic bottles, food wrappers, and
   debris scattered across the road and sidewalk...

📊 CLASSIFICATION:
----------------------------------------------------------------------
Category: Environment
Confidence: High

🎯 MISSION STATEMENT:
----------------------------------------------------------------------
To transform our community streets from polluted areas into clean,
sustainable spaces by implementing a comprehensive waste management
system that engages local residents and reduces environmental impact.

📝 PROBLEM DEFINITION:
Excessive littering and inadequate waste disposal systems have created
unsanitary conditions affecting community health and environment.

🎁 EXPECTED IMPACT:
Improved public health, enhanced community pride, reduced environmental
pollution, and creation of a sustainable waste management model.

======================================================================
```

## 🛠️ Configuration

Edit `config.py` to customize:

- Model selection (GPT-4, GPT-4 Vision)
- Problem categories and domain issues
- API parameters
- Image upload settings

## 🔒 Security Notes

- Never commit your `.env` file with API keys
- Keep your OpenAI API key secure
- Monitor API usage to control costs
- Use environment variables for sensitive data

## 🤝 Contributing

This is a prototype demonstration project. Feel free to extend it with:

- Additional problem domains
- Multi-language support
- Database integration
- Web interface
- Batch processing capabilities

## 📝 License

This project is for educational and demonstration purposes.

## 🙏 Acknowledgments

- Built with OpenAI's GPT-4 and GPT-4 Vision APIs
- Designed for community impact and learning

## 📧 Support

For issues or questions about this implementation, please refer to:

- OpenAI API Documentation: https://platform.openai.com/docs
- Python documentation: https://docs.python.org/

---

**Note**: This system requires an active OpenAI API key. API usage will incur costs based on OpenAI's pricing.
