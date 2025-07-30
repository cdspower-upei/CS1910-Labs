### Step 1: Create the Python Library

1. **Create the Python File**:
   - Open your favorite code editor or IDE.
   - Create a new file named `upei_smcs_lablibrary.py`.

2. **Write Your Library Code**:
   - Add some functions or classes to your library. Here’s a simple example:

   ```python
   # upei_smcs_lablibrary.py

   def greet(name):
       """Function to greet a person."""
       return f"Hello, {name}!"

   def add(a, b):
       """Function to add two numbers."""
       return a + b

   def multiply(a, b):
       """Function to multiply two numbers."""
       return a * b
   ```

### Step 2: Upload to GitHub

1. **Create a GitHub Repository**:
   - Go to GitHub and create a new repository (e.g., `my-python-libraries`).

2. **Upload the File**:
   - You can upload the `upei_smcs_lablibrary.py` file directly through the GitHub web interface or use Git commands to push it to your repository.

   If using Git commands:
   ```bash
   git init
   git add upei_smcs_lablibrary.py
   git commit -m "Add upei_smcs_lablibrary"
   git branch -M main
   git remote add origin https://github.com/yourusername/my-python-libraries.git
   git push -u origin main
   ```

### Step 3: Access the Library from a Jupyter Notebook

1. **Clone the Repository**:
   - In your Jupyter notebook environment, clone your repository:

   ```bash
   !git clone https://github.com/yourusername/my-python-libraries.git
   ```

2. **Import the Library**:
   - Navigate to the directory where the library is located and import it in your Jupyter notebook:

   ```python
   import sys
   sys.path.append('my-python-libraries')  # Adjust the path if necessary

   from upei_smcs_lablibrary import greet, add, multiply

   # Test the functions
   print(greet("Alice"))  # Output: Hello, Alice!
   print(add(5, 3))       # Output: 8
   print(multiply(4, 2))  # Output: 8
   ```

### Step 4: (Optional) Create a README

Consider adding a `README.md` file to your repository to explain how to use your library. This can include installation instructions, examples, and any other relevant information.

### Summary

You have now created a Python library, uploaded it to GitHub, and accessed it from a Jupyter notebook. You can expand your library with more functions or classes as needed!