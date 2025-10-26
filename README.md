# 🌍 AI-Powered Learning Platform

An intelligent web application that recognizes and translates real-world community challenges into structured learning missions using Google's Gemini Vision and Language APIs.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![Gemini](https://img.shields.io/badge/gemini-1.5--flash-green.svg)

## 🎯 Features

### 🔍 Computer Vision Detection (Task a)

Detects community issues in images across three domains:

- **🌱 Environment**: littered streets, blocked drainage, deforestation, waste disposal
- **�� Health**: overcrowded clinics, lack of safety gear, unsanitary spaces
- **📚 Education**: overcrowded classrooms, damaged infrastructure, lack of materials

### 📝 Mission Statement Generation (Task b)

Converts informal problem descriptions into formal, actionable mission statements:

- Clear mission statement
- Problem definition
- Specific goals
- Expected community impact
- Action steps

### �� Problem Classification (Task c)

Automatically categorizes problems into:

- Environment
- Health
- Education

With confidence scoring and reasoning.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

**Get your free Gemini API key**: https://aistudio.google.com/app/apikey

### 3. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 💻 Usage

### Upload Image Mode

1. Click "📸 Upload Image"
2. Upload a photo showing a community problem
3. Select analysis domains (Environment, Health, Education)
4. Click "🔍 Analyze Image"
5. View results in Detection, Classification, and Mission Statement tabs

### Text Description Mode

1. Click "✍️ Describe Problem"
2. Write a description of the community issue
3. Click "📝 Analyze Description"
4. View the generated mission statement and classification

### Example Inputs

**Image**: Photos of littered streets, overcrowded clinics, damaged schools

**Text**:

- "Our street is always flooded when it rains"
- "The clinic has no proper waiting area"
- "Our school has broken desks and students share textbooks"

## 📊 System Architecture

```
User Input (Image/Text)
        ↓
Vision Detector → Analyzes images, identifies issues
        ↓
Classifier → Categorizes into Environment/Health/Education
        ↓
Mission Generator → Creates structured mission statement
        ↓
Results Display → Interactive web interface
```

## 📁 Project Structure

```
computer-vision-prototype/
├── app.py                    # Streamlit web application
├── config.py                 # Configuration and settings
├── vision_detector.py        # Image analysis module
├── mission_generator.py      # Mission statement generator
├── problem_classifier.py     # Problem classifier
├── integrated_system.py      # Integrated workflow
├── requirements.txt          # Dependencies
├── .env                      # API key (create this)
├── .env.example             # Template
└── README.md                # This file
```

## 🔑 Core Components

| Component               | Purpose                      | Technology       |
| ----------------------- | ---------------------------- | ---------------- |
| `vision_detector.py`    | Detects issues in images     | GPT-4 Vision API |
| `mission_generator.py`  | Generates mission statements | GPT-4 API        |
| `problem_classifier.py` | Classifies problems          | GPT-4 API        |
| `integrated_system.py`  | Orchestrates workflow        | Python           |
| `app.py`                | Web interface                | Streamlit        |

## 🎨 Web Interface Features

- **📸 Image Upload**: Drag-and-drop or click to upload
- **✍️ Text Input**: Rich text area with examples
- **🎯 Domain Selection**: Choose specific domains to analyze
- **📊 Interactive Results**: Tabbed view for clear presentation
- **📥 Download Report**: Export analysis as text file
- **🎨 Modern UI**: Clean, responsive design

## 📈 Example Output

### Input

**Text**: "Our street is always flooded when it rains"

### Output

**Classification**:

- Category: 🌱 Environment
- Confidence: High

**Mission Statement**:

> To eliminate recurring flood hazards in our community by designing and implementing a sustainable drainage system that protects residents, property, and infrastructure while creating a model for urban water management.

**Goal**:
Implement a comprehensive drainage solution that prevents 95% of flooding incidents within one year.

**Action Steps**:

1. Conduct drainage survey and hydrological assessment
2. Design community-appropriate drainage system
3. Secure funding through grants
4. Implement improvements with local labor
5. Establish maintenance protocol

## ⚙️ Configuration

Edit `config.py` to customize:

- AI models (GPT-4, GPT-4 Vision)
- Domain-specific issues
- API parameters
- Image settings

## 💡 Python API Usage

You can also use the components programmatically:

```python
from integrated_system import AILearningPlatform

# Initialize platform
platform = AILearningPlatform()

# Analyze image
result = platform.process_image("path/to/image.jpg")
print(result['summary'])

# Analyze text
result = platform.process_text_description("problem description")
print(result['mission_statement'])
```

## 🔒 Security

- ✅ API keys stored in `.env` (not committed)
- ✅ Environment variable configuration
- ✅ Temporary file handling for uploads
- ⚠️ Monitor OpenAI API usage to control costs

## 📊 API Costs

Estimated costs per request:

- Vision analysis: ~$0.01-0.03
- Text processing: ~$0.01-0.02
- Classification: ~$0.005-0.01

## 🛠️ Development

### Requirements

- Python 3.8+
- OpenAI API key with GPT-4 Vision access
- Internet connection

### Running in Development

```bash
# Install in editable mode
pip install -e .

# Run with hot reload
streamlit run app.py --server.runOnSave true
```

## 🐛 Troubleshooting

### API Key Not Found

```bash
# Check .env file exists
ls -la .env

# Verify content
cat .env
```

### Module Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Streamlit Not Starting

```bash
# Check Streamlit installation
streamlit --version

# Try specifying port
streamlit run app.py --server.port 8502
```

## 📝 License

This project is for educational and demonstration purposes.

## 🙏 Acknowledgments

- Built with [OpenAI GPT-4](https://openai.com/) Vision and Language APIs
- Web interface powered by [Streamlit](https://streamlit.io/)
- Designed for community impact and learning

## 📧 Support

- OpenAI API Documentation: https://platform.openai.com/docs
- Streamlit Documentation: https://docs.streamlit.io/
- Python Documentation: https://docs.python.org/

---

**🌟 Ready to transform community challenges into actionable missions!**

Built with ❤️ for community impact
