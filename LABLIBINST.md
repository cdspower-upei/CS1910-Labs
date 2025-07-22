# Lab Form Library - Complete Instruction Manual v2.0

## 📚 **Quick Start for Creating Interactive Lab Exercises**

Welcome! This guide will teach you how to create interactive forms for lab exercises using our powerful, easy-to-use form library. **No complex widget programming required!**

---

## 🎯 **What You Can Create**

Our library provides **6 types of interactive components**:

1. **📝 Information Forms** - Collect names, emails, group info
2. **❓ Question Forms** - Open-ended questions with model answers  
3. **🔮 Prediction Tables** - Students predict code output
4. **✅ Validation Forms** - Truth tables with correct/incorrect checking
5. **📚 Educational Context** - Structured learning sections
6. **💡 Quick Context** - Simple markdown explanations

---

## 🚀 **Getting Started**

### **Step 1: Ensure Library is Loaded**
Make sure you've run the Lab Setup code block that includes the `LabFormLibrary` class.

### **Step 2: Copy a Template**
Choose the appropriate template below and modify the data.

### **Step 3: Customize Your Data**
Change the arrays/objects to match your exercise content.

### **Step 4: Run and Test**
Execute your code block to see your interactive form!

---

## 📋 **Form Type 1: Information Forms**

**Use for**: Collecting student names, emails, group information, survey data

### **Template:**
```python
#@title Your Form Title Here
#@markdown Add instructions for students here.

# STEP 1: Define your data
title = "Your Form Title"
fields = [
    {
        'name': 'field_variable_name',
        'label': 'What Students See:',
        'placeholder': 'Hint text in the input box'
    },
    # Add more fields as needed
]

# STEP 2: Optional default values (will appear as placeholder text)
default_values = [
    "Optional hint 1",
    "Optional hint 2",
    # One value per field, or use None to skip
]

# STEP 3: Create and display the form
display_form, get_data = forms.create_info_form(title, fields, default_values)
display_form()

# STEP 4: Optional - get the data later in your code
# student_data = get_data()
# print(f"Student name: {student_data['field_variable_name']}")
```

### **Example: Course Feedback Form**
```python
#@title Course Feedback
#@markdown Please provide your feedback on today's lab session.

title = "Lab Session Feedback"
fields = [
    {
        'name': 'student_name',
        'label': 'Your Name:',
        'placeholder': 'Enter your full name'
    },
    {
        'name': 'lab_rating',
        'label': 'Lab Rating (1-10):',
        'placeholder': 'Rate from 1 to 10'
    },
    {
        'name': 'favorite_part',
        'label': 'Favorite Part:',
        'placeholder': 'What did you enjoy most?'
    },
    {
        'name': 'suggestions',
        'label': 'Suggestions:',
        'placeholder': 'Any improvements?'
    }
]

# Optional: Provide starter hints
default_values = [
    "FirstName LastName",
    "Between 1-10",
    "What I liked most was...",
    "One thing that could improve..."
]

display_form, get_data = forms.create_info_form(title, fields, default_values)
display_form()
```

---

## ❓ **Form Type 2: Question Forms**

**Use for**: Open-ended questions, short answer exercises, comprehension checks

### **Template:**
```python
#@title Your Quiz Title
#@markdown Instructions for the exercise.

# STEP 1: Define your questions
title = "Your Exercise Title"
questions = [
    {
        "number": 1,
        "question": "Your first question here?",
        "type": "text"  # or "textarea" for longer answers
    },
    {
        "number": 2,
        "question": "Your second question here?",
        "type": "textarea"
    }
]

# STEP 2: Define model answers (optional)
answer_key = [
    "Model answer for question 1",
    "Model answer for question 2"
]

# STEP 3: Optional default values (appear as placeholder text)
default_values = [
    "Hint for question 1...",
    "To answer this, think about...",
    # Leave empty string "" for no hint
]

# STEP 4: Create and display the form
display_form = forms.create_question_form(title, questions, answer_key, default_values)
display_form()
```

### **Example: Python Basics Quiz**
```python
#@title Python Basics Understanding
#@markdown Answer these questions about Python fundamentals.

title = "Python Variables and Data Types"
questions = [
    {
        "number": 1,
        "question": "What is the difference between a variable and a value in Python?",
        "type": "textarea"
    },
    {
        "number": 2,
        "question": "What data type is the result of: type(42)?",
        "type": "text"
    },
    {
        "number": 3,
        "question": "Explain why this code causes an error: x = 5; y = '10'; result = x + y",
        "type": "textarea"
    }
]

answer_key = [
    "A variable is a name that stores a value. The variable is like a labeled box, and the value is what's inside the box. For example, in 'age = 25', 'age' is the variable and 25 is the value.",
    "<class 'int'>",
    "This causes a TypeError because you cannot add an integer (5) and a string ('10') directly. Python doesn't automatically convert between types. You would need to convert one to match the other, like: x + int(y) or str(x) + y"
]

# Provide helpful starter hints
default_values = [
    "A variable is...",
    "<class '?'>",
    "This error occurs because..."
]

display_form = forms.create_question_form(title, questions, answer_key, default_values)
display_form()
```

---

## 🔮 **Form Type 3: Prediction Tables**

**Use for**: Predicting code output, trace tables, algorithm prediction

### **Template:**
```python
#@title Code Prediction Exercise
#@markdown Predict what each line of code will output.

# STEP 1: Define your code snippets
title = "Your Prediction Exercise"
code_snippets = [
    "print('Hello')",
    "x = 5",
    "print(x * 2)"
]

# STEP 2: Define expected answers (optional)
expected_answers = [
    "Hello",
    "",  # No output for assignments
    "10"
]

# STEP 3: Optional default values (appear as placeholder text)
default_values = [
    "What will this print?",
    "No output",
    "Think about x * 2..."
]

# STEP 4: Create and display the form
display_form = forms.create_prediction_table(title, code_snippets, expected_answers, default_values)
display_form()
```

### **Example: Boolean Logic Prediction**
```python
#@title Boolean Logic Prediction
#@markdown Predict the output of these Boolean expressions with a=3, b=4, c=5.

title = "Boolean Operations Prediction (a=3, b=4, c=5)"
code_snippets = [
    "print(a < b and b < c)",
    "print(a < b or b > c)",
    "print(not a < b)",
    "result = a > b",
    "print(result)"
]

expected_answers = [
    "True",
    "True", 
    "False",
    "",  # No output from assignment
    "False"
]

# Strategic hints - some filled, some empty
default_values = [
    "True and True = ?",
    "",  # No hint - let them think
    "not True = ?",
    "No output expected",
    "What is result?"
]

display_form = forms.create_prediction_table(title, code_snippets, expected_answers, default_values)
display_form()
```

---

## ✅ **Form Type 4: Validation Forms**

**Use for**: Truth tables, fill-in-the-blank with validation, structured exercises

### **Template:**
```python
#@title Truth Table Exercise
#@markdown Complete the table below.

# STEP 1: Define your table structure
title = "Your Table Title"
instructions = "Instructions for completing the table"

# STEP 2: Fixed data that students see (but don't edit)
data_rows = [
    {"Column1": "Value1", "Column2": "Value2"},
    {"Column1": "Value3", "Column2": "Value4"}
]

# STEP 3: All column headers (fixed + input columns)
headers = ["Column1", "Column2", "Student_Input1", "Student_Input2"]

# STEP 4: Correct answers for input columns only
correct_answers = [
    ["Answer1_Row1", "Answer2_Row1"],  # Answers for row 1
    ["Answer1_Row2", "Answer2_Row2"]   # Answers for row 2
]

# STEP 5: Optional default values (appear as placeholder text)
default_values = [
    ["Hint for row 1 col 1", "Hint for row 1 col 2"],
    ["Hint for row 2 col 1", "Hint for row 2 col 2"]
]

# STEP 6: Create and display the form
display_form = forms.create_validation_form(title, data_rows, headers, correct_answers, instructions, default_values)
display_form()
```

### **Example: Logic Gates Truth Table**
```python
#@title Logic Gates Truth Table  
#@markdown Complete the truth table for AND and OR gates.

title = "Logic Gates: AND and OR Operations"
instructions = "Fill in the output for each logic gate given the inputs:"

# Fixed input data
data_rows = [
    {"Input A": "0", "Input B": "0"},
    {"Input A": "0", "Input B": "1"},
    {"Input A": "1", "Input B": "0"},
    {"Input A": "1", "Input B": "1"}
]

# All columns (inputs are fixed, outputs are filled by students)
headers = ["Input A", "Input B", "AND Output", "OR Output"]

# Correct answers for the output columns
correct_answers = [
    ["0", "0"],  # Row 1: A=0, B=0 → AND=0, OR=0
    ["0", "1"],  # Row 2: A=0, B=1 → AND=0, OR=1  
    ["0", "1"],  # Row 3: A=1, B=0 → AND=0, OR=1
    ["1", "1"]   # Row 4: A=1, B=1 → AND=1, OR=1
]

# Strategic hints - give pattern clues
default_values = [
    ["0", ""],     # Hint for AND, let them figure out OR
    ["", "1"],     # Let them figure out AND, hint for OR
    ["0", ""],     # Pattern emerging...
    ["", "1"]      # Final row - they should see the pattern
]

display_form = forms.create_validation_form(title, data_rows, headers, correct_answers, instructions, default_values)
display_form()
```

---

## 📚 **Form Type 5: Educational Context (Structured)**

**Use for**: Complex learning sections with multiple topics

### **Template:**
```python
# Add this after your forms to provide educational context

forms.add_educational_context(
    title="🧠 Your Learning Section Title",
    sections=[
        {
            'heading': 'Topic 1',
            'emoji': '📊',  # Optional
            'content': '''Your content here...
- Can include bullet points
- Code examples
- Multiple paragraphs'''
        },
        {
            'heading': 'Topic 2', 
            'content': '''More content...
```python
# Code examples work great
print("Hello World")
```'''
        }
    ]
)
```

### **Example: Boolean Logic Context**
```python
forms.add_educational_context(
    title="🧠 Key Concepts Review:",
    sections=[
        {
            'heading': 'Boolean Data Type',
            'emoji': '📊',
            'content': '''- Boolean expressions always return the `bool` data type
- Only two possible values: `True` or `False`
- Result of comparison operations (`<`, `>`, `==`, etc.)'''
        },
        {
            'heading': 'Short-Circuit Evaluation', 
            'emoji': '⚡',
            'content': '''- **AND (`and`)**: If first expression is `False`, second is not evaluated
- **OR (`or`)**: If first expression is `True`, second is not evaluated
- This improves performance and prevents errors'''
        },
        {
            'heading': 'Practical Examples',
            'emoji': '💻', 
            'content': '''```python
# Short-circuit AND
result = (x != 0) and (10 / x > 5)  # Safe - won't divide by zero

# Short-circuit OR  
result = (user_input == "") or (len(user_input) > 0)  # Efficient
```'''
        }
    ]
)
```

---

## 💡 **Form Type 6: Quick Context (Simple)**

**Use for**: Simple explanations, tips, summaries

### **Template:**
```python
forms.add_quick_context("""
### 🎯 **Your Title Here**

Your content in markdown format...

#### **Subtopic:**
- Bullet points work
- So do **bold** and *italic*

#### **Code Examples:**
```python
print("Code blocks work too!")
```

#### **Key Takeaways:**
- Remember the important points
- Keep it concise and helpful
""")
```

### **Example: Quick Boolean Tips**
```python
forms.add_quick_context("""
### 📚 **Quick Boolean Logic Reference**

#### **Truth Table Summary:**
- **AND**: True only when BOTH inputs are True
- **OR**: True when AT LEAST ONE input is True

#### **Memory Tricks:**
- **AND**: "**A**ll **N**eed to be **D**one" 
- **OR**: "**O**ne **R**equirement is enough"

#### **Common Mistakes:**
- Don't confuse `=` (assignment) with `==` (comparison)
- Remember parentheses for complex expressions: `(a < b) and (c > d)`
""")
```

---

## 🛠 **Advanced Usage Examples**

### **Example 1: Complete Exercise with Context**
```python
#@title Complete Boolean Exercise
#@markdown This shows how to combine multiple components.

# Main exercise form
title = "Boolean Logic Mastery"
questions = [
    {"number": 1, "question": "What is short-circuit evaluation?", "type": "textarea"},
    {"number": 2, "question": "Write a boolean expression with variables a, b, c", "type": "text"}
]

answer_key = [
    "Short-circuit evaluation means that boolean operators stop evaluating as soon as the result is known.",
    "Examples: a < b and b < c, a > 10 or c == 5"
]

default_values = [
    "Short-circuit evaluation means...",
    "a < b and ..."
]

display_form = forms.create_question_form(title, questions, answer_key, default_values)
display_form()

# Add educational context
forms.add_quick_context("""
### 🎯 **Study Tips:**
- Practice with different variable values
- Draw truth tables for complex expressions
- Test your logic with real Python code
""")
```

### **Example 2: Multiple Forms in Sequence**
```python
# Form 1: Information Collection
display_form, get_data = forms.create_info_form("Student Info", fields)
display_form()

# Form 2: Prediction Exercise  
display_form = forms.create_prediction_table("Code Prediction", code_snippets, answers)
display_form()

# Form 3: Knowledge Check
display_form = forms.create_question_form("Understanding Check", questions, answer_key)
display_form()

# Final context
forms.add_quick_context("### 🎉 **Great work!** You've completed all exercises.")
```

### **Example 3: Differentiated Instruction**
```python
# Version A: Beginner (lots of hints)
beginner_defaults = ["False", "True", "Think about AND logic...", "False"]
display_form = forms.create_prediction_table("Beginner Version", codes, answers, beginner_defaults)
display_form()

# Version B: Advanced (no hints)
display_form = forms.create_prediction_table("Challenge Version", codes, answers)
display_form()

# Version C: Assessment (no reveals)
display_form = forms.create_prediction_table("Assessment Version", codes)
display_form()
```

---

## 🔧 **Troubleshooting Guide**

### **Common Issues and Solutions:**

#### **❌ "NameError: name 'forms' is not defined"**
**Solution**: Make sure you ran the Lab Setup code block first

#### **❌ Form doesn't display properly**
**Solution**: Check that all required fields in your data dictionaries are present:
- Every question needs: `'number'`, `'question'`, `'type'`
- Every field needs: `'name'`, `'label'`, `'placeholder'`

#### **❌ Default values not working**
**Solution**: Ensure your `default_values` array length matches your questions/fields:
```python
# Wrong: 3 questions, 2 defaults
questions = [q1, q2, q3]
default_values = ["hint1", "hint2"]  # Missing hint3!

# Right: Match the lengths
default_values = ["hint1", "hint2", "hint3"]
# Or use empty string for no hint: ["hint1", "", "hint3"]
```

#### **❌ Validation not working correctly**
**Solution**: For validation forms, ensure:
- `correct_answers` structure matches input columns
- Use nested arrays: `[["row1_ans1", "row1_ans2"], ["row2_ans1", "row2_ans2"]]`

#### **❌ Long questions getting cut off**
**Solution**: The library handles this automatically with HTML text wrapping. If still having issues, break long questions into shorter sentences.

#### **❌ Buttons not working**
**Solution**: Make sure you're running in a Jupyter/Colab environment with widgets enabled

---

## 📝 **Quick Reference Cheat Sheet**

### **Function Signatures:**
```python
# Information Form
display_form, get_data = forms.create_info_form(title, fields, default_values=None)

# Question Form  
display_form = forms.create_question_form(title, questions, answer_key=None, default_values=None)

# Prediction Table
display_form = forms.create_prediction_table(title, code_snippets, expected_answers=None, default_values=None)

# Validation Form
display_form = forms.create_validation_form(title, data_rows, headers, correct_answers, instructions="", default_values=None)

# Educational Context
forms.add_educational_context(title, sections)
forms.add_quick_context(markdown_content)
```

### **Required Data Structures:**

**Fields** (for info forms):
```python
{'name': 'variable_name', 'label': 'Display Text:', 'placeholder': 'Hint text'}
```

**Questions** (for question forms):
```python
{'number': 1, 'question': 'Question text?', 'type': 'text'}  # or 'textarea'
```

**Data Rows** (for validation forms):
```python
{'Fixed_Column': 'Fixed_Value'}  # Only include columns students don't edit
```

### **Optional Parameters:**
- **`default_values`**: Provide hints/starter text as placeholder text
- **`answer_key`**: Enable reveal functionality for instructors
- **`expected_answers`**: Enable validation for prediction tables
- **`instructions`**: Add guidance text for validation forms

---

## 🎓 **Best Practices**

### **1. Progressive Disclosure:**
Start easy, increase difficulty:
```python
# Early questions: More hints
default_values = ["Complete hint", "Starter text...", "Think about..."]
# Later questions: Less help  
default_values = ["", "", ""]
```

### **2. Consistent Numbering:**
```python
# Good: Sequential numbering
questions = [
    {"number": 1, "question": "...", "type": "text"},
    {"number": 2, "question": "...", "type": "text"}
]

# Also good: Custom numbering
questions = [
    {"number": "1a", "question": "...", "type": "text"},
    {"number": "1b", "question": "...", "type": "text"}
]
```

### **3. Meaningful Placeholders:**
```python
# Better than generic hints
default_values = [
    "Think about operator precedence...",  # Specific guidance
    "What happens when both are True?",    # Leading question
    ""                                     # No hint for challenge
]
```

### **4. Strategic Context Placement:**
```python
# Pattern: Form → Context → Form → Context
display_form = forms.create_prediction_table(...)
display_form()

forms.add_quick_context("### 🎯 **Key insight:** Notice the pattern...")

display_form = forms.create_question_form(...)  
display_form()
```

---

## 🚀 **Ready to Create!**

You now have everything you need to create engaging, interactive lab exercises. Start with the templates, customize the data to fit your content, and enhance with educational context.

### **Remember:**
- **Focus on pedagogy** - let the library handle the technical complexity
- **Test your forms** before using with students
- **Iterate and improve** based on student feedback
- **Mix different form types** for varied learning experiences

### **Need Help?**
- Reference the examples above
- Check the troubleshooting section
- Ask your lab coordinator for assistance

**Happy form creating! 🎉**
