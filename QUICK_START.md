# QUICK START GUIDE

## AI-Powered Learning Platform

---

## 🚀 Quick Setup (5 minutes)

### 1. Install Dependencies

```bash
cd /run/media/jennermaxim/Projects/projects/artificial-intelligence/computer-vision-prototype
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Edit .env file and add your OpenAI API key
echo "OPENAI_API_KEY=your_key_here" > .env
```

### 3. Run Demo

```bash
# See example outputs (no API calls)
python demo_outputs.py

# Or run interactive mode (requires valid API key)
python main.py interactive
```

---

## 📖 Three Main Tasks

### Task (a): Computer Vision Detection

**What it does:** Analyzes images to detect community issues

```python
from vision_detector import CommunityIssueDetector

detector = CommunityIssueDetector()
result = detector.detect_issues("path/to/image.jpg")
print(result['analysis'])
```

**Detects issues in:**

- 🌍 Environment (litter, drainage, waste)
- 🏥 Health (clinics, safety, sanitation)
- 📚 Education (classrooms, materials, infrastructure)

---

### Task (b): Mission Statement Generation

**What it does:** Converts informal problem descriptions into formal mission statements

```python
from mission_generator import MissionStatementGenerator

generator = MissionStatementGenerator()
result = generator.generate_mission_statement(
    "our street is always flooded when it rains"
)
print(result['mission_statement'])
```

**Generates:**

- Mission statement
- Problem definition
- Goals and expected impact
- Action steps

---

### Task (c): Problem Classification

**What it does:** Automatically categorizes problems into domains

```python
from problem_classifier import ProblemClassifier

classifier = ProblemClassifier()
result = classifier.classify_problem(
    "The streets are filled with plastic waste"
)
print(f"Category: {result['category']}")  # Output: Environment
```

**Categories:**

- Environment
- Health
- Education

---

## 🎯 Complete Workflow

Use the integrated system for end-to-end processing:

```python
from integrated_system import AILearningPlatform

platform = AILearningPlatform()

# Process an image
result = platform.process_image("image.jpg")
print(result['summary'])

# Process text description
result = platform.process_text_description(
    "our school has broken desks"
)
print(result['summary'])
```

---

## 🖥️ Command Line Interface

```bash
# Run all demonstrations
python main.py demo-all

# Individual task demos
python main.py demo-vision        # Task (a)
python main.py demo-text          # Task (b)
python main.py demo-classification # Task (c)

# Interactive mode
python main.py interactive

# Example outputs (no API required)
python demo_outputs.py
```

---

## 📋 Common Use Cases

### Use Case 1: Analyze Community Photo

```python
platform = AILearningPlatform()
result = platform.process_image("community_issue.jpg")
# Get detection + classification + mission statement
```

### Use Case 2: Convert Problem to Mission

```python
from mission_generator import create_mission_statement
result = create_mission_statement("problem description here")
```

### Use Case 3: Classify Multiple Problems

```python
from problem_classifier import ProblemClassifier
classifier = ProblemClassifier()
problems = ["problem1", "problem2", "problem3"]
results = classifier.classify_batch(problems)
```

---

## ⚠️ Troubleshooting

### Issue: API Quota Error

**Error:** `Error code: 429 - insufficient_quota`

**Solutions:**

1. Check your OpenAI account billing
2. Verify API key has available quota
3. Visit: https://platform.openai.com/account/usage
4. Run demo_outputs.py to see example results without API calls

### Issue: Import Errors

**Error:** `ModuleNotFoundError: No module named 'openai'`

**Solution:**

```bash
source venv/bin/activate  # Activate virtual environment
pip install -r requirements.txt
```

### Issue: Missing API Key

**Error:** `OPENAI_API_KEY not found in environment variables`

**Solution:**

```bash
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=your_key_here
```

---

## 📁 Key Files

| File                    | Purpose                       |
| ----------------------- | ----------------------------- |
| `vision_detector.py`    | Task (a) - Computer vision    |
| `mission_generator.py`  | Task (b) - Mission statements |
| `problem_classifier.py` | Task (c) - Classification     |
| `integrated_system.py`  | Complete workflow             |
| `main.py`               | CLI interface                 |
| `demo_outputs.py`       | Example outputs               |
| `config.py`             | Configuration                 |

---

## 🎓 Example Input/Output

### Input (Text)

```
"our street is always flooded when it rains"
```

### Output

```
Classification: Environment (High confidence)

Mission Statement:
"To eliminate recurring flood hazards in our community by designing
and implementing a sustainable drainage system that protects residents,
property, and infrastructure while creating a model for urban water
management."

Action Steps:
1. Conduct drainage survey
2. Design drainage system
3. Secure funding
4. Implement improvements
5. Establish maintenance protocol
```

---

## 🔗 Quick Links

- **Full Documentation:** `PROJECT_DOCUMENTATION.md`
- **User Guide:** `README.md`
- **OpenAI Docs:** https://platform.openai.com/docs
- **API Usage:** https://platform.openai.com/account/usage

---

## ✅ Checklist

Before running the system:

- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] API key configured in .env
- [ ] OpenAI account has available quota

---

## 💡 Tips

1. **Start with demo_outputs.py** to see what the system produces
2. **Use interactive mode** for testing: `python main.py interactive`
3. **Check API usage** regularly to manage costs
4. **Process images in batches** for efficiency
5. **Save results** to files for later analysis

---

## 🎯 Success Criteria Met

✅ Task (a): Computer vision detection working  
✅ Task (b): Mission statement generation working  
✅ Task (c): Problem classification working  
✅ All three tasks integrated  
✅ CLI interface available  
✅ Documentation complete

---

**Ready to use!** Start with `python demo_outputs.py` to see example results.
