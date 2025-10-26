# API REFERENCE GUIDE

## AI-Powered Learning Platform

Complete API documentation for all modules and classes.

---

## Table of Contents

1. [vision_detector](#vision_detector)
2. [mission_generator](#mission_generator)
3. [problem_classifier](#problem_classifier)
4. [integrated_system](#integrated_system)
5. [config](#config)

---

## vision_detector

### CommunityIssueDetector

Main class for detecting community issues in images using GPT-4 Vision.

#### Constructor

```python
detector = CommunityIssueDetector(api_key=None)
```

**Parameters:**

- `api_key` (str, optional): OpenAI API key. If None, uses key from Config.

**Example:**

```python
detector = CommunityIssueDetector()
# or with explicit key
detector = CommunityIssueDetector(api_key="sk-...")
```

---

#### detect_issues()

Detect community issues in an image.

```python
result = detector.detect_issues(image_path, domains=None)
```

**Parameters:**

- `image_path` (str): Path to image file or URL
- `domains` (list, optional): List of domains to focus on. Default: ['Environment', 'Health', 'Education']

**Returns:**
Dictionary with keys:

- `success` (bool): Whether detection succeeded
- `analysis` (str): Detailed analysis text
- `domains_analyzed` (list): Domains that were analyzed
- `error` (str): Error message if failed

**Example:**

```python
# Analyze all domains
result = detector.detect_issues("street.jpg")

# Focus on specific domains
result = detector.detect_issues("street.jpg", domains=['Environment'])

# Use URL
result = detector.detect_issues("https://example.com/image.jpg")

if result['success']:
    print(result['analysis'])
else:
    print(f"Error: {result['error']}")
```

---

#### detect_multiple_images()

Detect issues in multiple images.

```python
results = detector.detect_multiple_images(image_paths, domains=None)
```

**Parameters:**

- `image_paths` (list): List of image paths or URLs
- `domains` (list, optional): Domains to focus on

**Returns:**
List of result dictionaries (same format as detect_issues)

**Example:**

```python
images = ["img1.jpg", "img2.jpg", "img3.jpg"]
results = detector.detect_multiple_images(images)

for result in results:
    print(f"Image: {result['image_path']}")
    print(f"Analysis: {result['analysis']}\n")
```

---

#### Convenience Function

```python
from vision_detector import detect_community_issue

result = detect_community_issue(image_path, domains=None)
```

Quick one-line detection without instantiating class.

---

## mission_generator

### MissionStatementGenerator

Converts problem descriptions into formalized mission statements.

#### Constructor

```python
generator = MissionStatementGenerator(api_key=None)
```

**Parameters:**

- `api_key` (str, optional): OpenAI API key

**Example:**

```python
generator = MissionStatementGenerator()
```

---

#### generate_mission_statement()

Generate a mission statement from a problem description.

```python
result = generator.generate_mission_statement(problem_description, context=None)
```

**Parameters:**

- `problem_description` (str): User's description of the problem
- `context` (str, optional): Additional context about the problem

**Returns:**
Dictionary with keys:

- `success` (bool): Whether generation succeeded
- `original_description` (str): Input description
- `mission_statement` (str): Generated mission statement
- `problem_definition` (str): Precise problem definition
- `goal` (str): Specific, measurable goal
- `expected_impact` (str): Community benefits
- `action_steps` (list): List of action steps
- `full_response` (str): Complete API response
- `error` (str): Error message if failed

**Example:**

```python
result = generator.generate_mission_statement(
    "our street is always flooded when it rains",
    context="This happens every rainy season for 5 years"
)

if result['success']:
    print(f"Mission: {result['mission_statement']}")
    print(f"\nGoal: {result['goal']}")
    print(f"\nAction Steps:")
    for step in result['action_steps']:
        print(f"  - {step}")
```

---

#### generate_batch_missions()

Generate mission statements for multiple problems.

```python
results = generator.generate_batch_missions(problem_descriptions)
```

**Parameters:**

- `problem_descriptions` (list): List of problem description strings

**Returns:**
List of result dictionaries

**Example:**

```python
problems = [
    "street flooding",
    "broken school desks",
    "overcrowded clinic"
]
results = generator.generate_batch_missions(problems)
```

---

#### Convenience Function

```python
from mission_generator import create_mission_statement

result = create_mission_statement(problem_description, context=None)
```

Quick mission generation without instantiating class.

---

## problem_classifier

### ProblemClassifier

Classifies community problems into predefined categories.

#### Constructor

```python
classifier = ProblemClassifier(api_key=None)
```

**Parameters:**

- `api_key` (str, optional): OpenAI API key

**Example:**

```python
classifier = ProblemClassifier()
```

---

#### classify_problem()

Classify a problem into one of three categories.

```python
result = classifier.classify_problem(problem_description, use_reasoning=True)
```

**Parameters:**

- `problem_description` (str): Description of the problem
- `use_reasoning` (bool): Whether to include reasoning. Default: True

**Returns:**
Dictionary with keys:

- `success` (bool): Whether classification succeeded
- `problem_description` (str): Input description
- `category` (str): Classification result ('Environment', 'Health', or 'Education')
- `confidence` (str): Confidence level ('High', 'Medium', or 'Low')
- `reasoning` (str): Explanation for classification
- `all_categories` (list): List of all possible categories
- `full_response` (str): Complete API response
- `error` (str): Error message if failed

**Example:**

```python
result = classifier.classify_problem(
    "The streets are filled with plastic waste"
)

if result['success']:
    print(f"Category: {result['category']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Reasoning: {result['reasoning']}")
```

---

#### classify_with_vision_analysis()

Classify based on vision analysis output.

```python
result = classifier.classify_with_vision_analysis(vision_analysis)
```

**Parameters:**

- `vision_analysis` (str): Output from vision detector

**Returns:**
Dictionary with classification results

**Example:**

```python
# After running vision detection
vision_result = detector.detect_issues("image.jpg")
classification = classifier.classify_with_vision_analysis(
    vision_result['analysis']
)
print(f"Category: {classification['category']}")
```

---

#### classify_batch()

Classify multiple problems at once.

```python
results = classifier.classify_batch(problem_descriptions)
```

**Parameters:**

- `problem_descriptions` (list): List of problem descriptions

**Returns:**
List of classification result dictionaries

**Example:**

```python
problems = [
    "littered streets",
    "broken school furniture",
    "overcrowded hospital"
]
results = classifier.classify_batch(problems)

for result in results:
    print(f"{result['problem_description']}: {result['category']}")
```

---

#### Convenience Function

```python
from problem_classifier import classify_community_problem

result = classify_community_problem(problem_description)
```

Quick classification without instantiating class.

---

## integrated_system

### AILearningPlatform

Complete integrated platform combining all three tasks.

#### Constructor

```python
platform = AILearningPlatform(api_key=None)
```

**Parameters:**

- `api_key` (str, optional): OpenAI API key

**Example:**

```python
platform = AILearningPlatform()
```

---

#### process_image()

Complete workflow: Detect, classify, and generate mission from image.

```python
result = platform.process_image(image_path, domains=None)
```

**Parameters:**

- `image_path` (str): Path to image or URL
- `domains` (list, optional): Specific domains to analyze

**Returns:**
Dictionary with keys:

- `success` (bool): Whether processing succeeded
- `image_path` (str): Input image path
- `vision_analysis` (str): Vision detection results
- `classification` (dict): Classification results
- `mission_statement` (dict): Mission statement results
- `summary` (str): Formatted summary of all results
- `error` (str): Error message if failed
- `step` (str): Which step failed (if error)

**Example:**

```python
result = platform.process_image("community_issue.jpg")

if result['success']:
    print(result['summary'])

    # Access individual components
    print(f"\nCategory: {result['classification']['category']}")
    print(f"Mission: {result['mission_statement']['mission_statement']}")
else:
    print(f"Error at {result['step']}: {result['error']}")
```

---

#### process_text_description()

Process text description: Classify and generate mission.

```python
result = platform.process_text_description(problem_description)
```

**Parameters:**

- `problem_description` (str): User's problem description

**Returns:**
Dictionary with keys:

- `success` (bool): Whether processing succeeded
- `original_description` (str): Input description
- `classification` (dict): Classification results
- `mission_statement` (dict): Mission statement results
- `summary` (str): Formatted summary
- `error` (str): Error message if failed
- `step` (str): Which step failed (if error)

**Example:**

```python
result = platform.process_text_description(
    "our street is always flooded when it rains"
)

if result['success']:
    print(result['summary'])
else:
    print(f"Error: {result['error']}")
```

---

#### process_multiple_images()

Process multiple images in batch.

```python
results = platform.process_multiple_images(image_paths)
```

**Parameters:**

- `image_paths` (list): List of image paths or URLs

**Returns:**
List of result dictionaries

**Example:**

```python
images = ["issue1.jpg", "issue2.jpg", "issue3.jpg"]
results = platform.process_multiple_images(images)

for i, result in enumerate(results, 1):
    print(f"\n{'='*50}")
    print(f"Image {i}")
    print('='*50)
    if result['success']:
        print(result['summary'])
```

---

#### Convenience Function

```python
from integrated_system import analyze_community_issue

result = analyze_community_issue(source, source_type='auto')
```

**Parameters:**

- `source` (str): Image path/URL or text description
- `source_type` (str): 'image', 'text', or 'auto' (auto-detect)

**Example:**

```python
# Auto-detect type
result = analyze_community_issue("path/to/image.jpg")
result = analyze_community_issue("problem description text")

# Explicit type
result = analyze_community_issue("source", source_type='image')
```

---

## config

### Config Class

Configuration settings for the platform.

#### Class Attributes

```python
# API Configuration
Config.OPENAI_API_KEY      # OpenAI API key from environment

# Model Settings
Config.VISION_MODEL        # GPT-4 Vision model name
Config.TEXT_MODEL          # GPT-4 text model name

# Categories
Config.CATEGORIES          # ['Environment', 'Health', 'Education']

# Domain Issues
Config.DOMAIN_ISSUES       # Dictionary of domain-specific issues

# Image Settings
Config.MAX_IMAGE_SIZE      # Maximum image size (20MB)
Config.ALLOWED_EXTENSIONS  # Allowed file extensions
```

#### Methods

```python
Config.validate()  # Validate configuration
```

**Example:**

```python
from config import Config

# Access configuration
print(Config.CATEGORIES)  # ['Environment', 'Health', 'Education']
print(Config.DOMAIN_ISSUES['Environment'])  # List of environment issues

# Validate before use
try:
    Config.validate()
    print("Configuration valid")
except ValueError as e:
    print(f"Configuration error: {e}")
```

---

## Complete Example Workflows

### Workflow 1: Image Analysis Pipeline

```python
from integrated_system import AILearningPlatform

platform = AILearningPlatform()

# Process image through complete pipeline
result = platform.process_image("community_issue.jpg")

if result['success']:
    # Extract components
    vision = result['vision_analysis']
    category = result['classification']['category']
    mission = result['mission_statement']['mission_statement']
    steps = result['mission_statement']['action_steps']

    # Use results
    print(f"Detected Issues:\n{vision}\n")
    print(f"Category: {category}\n")
    print(f"Mission: {mission}\n")
    print("Action Steps:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")
```

### Workflow 2: Batch Text Processing

```python
from problem_classifier import ProblemClassifier
from mission_generator import MissionStatementGenerator

classifier = ProblemClassifier()
generator = MissionStatementGenerator()

problems = [
    "street flooding during rain",
    "school lacks textbooks",
    "clinic has no waiting area"
]

for problem in problems:
    # Classify
    classification = classifier.classify_problem(problem)

    # Generate mission
    mission = generator.generate_mission_statement(
        problem,
        context=f"Category: {classification['category']}"
    )

    # Display results
    print(f"\nProblem: {problem}")
    print(f"Category: {classification['category']}")
    print(f"Mission: {mission['mission_statement']}")
```

### Workflow 3: Custom Component Usage

```python
from vision_detector import CommunityIssueDetector
from problem_classifier import ProblemClassifier
from mission_generator import MissionStatementGenerator

# Initialize components
detector = CommunityIssueDetector()
classifier = ProblemClassifier()
generator = MissionStatementGenerator()

# Custom workflow
image_path = "issue.jpg"

# Step 1: Detect
vision_result = detector.detect_issues(image_path)

# Step 2: Classify (using custom logic)
if "waste" in vision_result['analysis'].lower():
    category = "Environment"
else:
    classification = classifier.classify_with_vision_analysis(
        vision_result['analysis']
    )
    category = classification['category']

# Step 3: Generate mission with custom context
mission_result = generator.generate_mission_statement(
    vision_result['analysis'][:200],  # Use first 200 chars
    context=f"Category: {category}, Severity: High"
)

print(f"Custom Analysis:")
print(f"Category: {category}")
print(f"Mission: {mission_result['mission_statement']}")
```

---

## Error Handling

All API methods return dictionaries with a `success` key. Always check this:

```python
result = platform.process_image("image.jpg")

if result['success']:
    # Process successful result
    print(result['summary'])
else:
    # Handle error
    error_step = result.get('step', 'unknown')
    error_message = result.get('error', 'Unknown error')
    print(f"Error at {error_step}: {error_message}")
```

Common errors:

- `insufficient_quota`: API quota exceeded
- `invalid_api_key`: Invalid or missing API key
- `file_not_found`: Image file doesn't exist
- `network_error`: Network connectivity issue

---

## Best Practices

1. **Always check `success` flag**

   ```python
   if result['success']:
       # Use result
   ```

2. **Use context managers for batch processing**

   ```python
   with AILearningPlatform() as platform:
       results = platform.process_multiple_images(images)
   ```

3. **Handle API quota limits**

   ```python
   try:
       result = platform.process_image(image)
   except Exception as e:
       if "quota" in str(e).lower():
           print("API quota exceeded")
   ```

4. **Cache results when possible**

   ```python
   import json

   result = platform.process_image("image.jpg")
   with open('result.json', 'w') as f:
       json.dump(result, f)
   ```

---

## Return Value Reference

### Vision Detection Result

```python
{
    'success': True/False,
    'analysis': str,  # Detailed analysis text
    'domains_analyzed': list,  # ['Environment', 'Health', 'Education']
    'raw_response': object,  # OpenAI response object
    'error': str  # Only if success=False
}
```

### Mission Generation Result

```python
{
    'success': True/False,
    'original_description': str,
    'mission_statement': str,
    'problem_definition': str,
    'goal': str,
    'expected_impact': str,
    'action_steps': list,
    'full_response': str,
    'error': str  # Only if success=False
}
```

### Classification Result

```python
{
    'success': True/False,
    'problem_description': str,
    'category': str,  # 'Environment', 'Health', or 'Education'
    'confidence': str,  # 'High', 'Medium', or 'Low'
    'reasoning': str,
    'all_categories': list,
    'full_response': str,
    'error': str  # Only if success=False
}
```

### Integrated System Result

```python
{
    'success': True/False,
    'image_path': str,  # For image processing
    'original_description': str,  # For text processing
    'vision_analysis': str,  # Vision detection output
    'classification': dict,  # Classification result
    'mission_statement': dict,  # Mission generation result
    'summary': str,  # Formatted summary
    'error': str,  # Only if success=False
    'step': str  # Which step failed (if error)
}
```

---

**API Reference Complete**

For more examples, see:

- `test_example.py` - Basic usage examples
- `demo_outputs.py` - Expected outputs
- `main.py` - CLI implementation
