# 🚀 Quick Start Guide

## Running the Application

### Step 1: Activate Virtual Environment

```bash
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

### Step 2: Start Streamlit App

```bash
streamlit run app.py
```

### Step 3: Open Browser

The app will automatically open at: `http://localhost:8501`

## Features

### 📸 Image Analysis

1. Select "Upload Image" mode
2. Drag & drop or click to upload an image
3. Choose analysis domains (Environment/Health/Education)
4. Click "Analyze Image"
5. View results in tabs

### ✍️ Text Analysis

1. Select "Describe Problem" mode
2. Type your problem description
3. Click "Analyze Description"
4. View classification and mission statement

## Example Descriptions

**Environment:**

- "Our street is always flooded when it rains"
- "The park is filled with plastic waste"

**Health:**

- "The clinic has no waiting area"
- "Community health center lacks supplies"

**Education:**

- "School has broken desks"
- "Classrooms are overcrowded"

## Troubleshooting

**App won't start:**

```bash
pip install streamlit --upgrade
```

**API key error:**
Check `.env` file contains:

```
OPENAI_API_KEY=your_key_here
```

**Module not found:**

```bash
pip install -r requirements.txt --force-reinstall
```

## Key Features

✅ Interactive web interface  
✅ Image upload & analysis  
✅ Text description processing  
✅ Real-time classification  
✅ Mission statement generation  
✅ Download reports  
✅ Domain filtering

---

**Ready to transform communities! 🌟**
