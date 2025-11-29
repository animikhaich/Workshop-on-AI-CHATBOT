<div align="center">

# 🤖 Workshop on AI & Chatbot Development

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE)

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="120" alt="Python Logo"/>

### 🎓 A Comprehensive Python & AI Workshop
#### 📍 RNSIT College Campus | Department of Electronics and Communication

*Learn Python from basics to building AI-powered chatbots and Machine Learning models*

---

[📚 Explore Topics](#-workshop-curriculum) • [🚀 Quick Start](#-quick-start) • [💬 Chatbot](#-caseybot---ai-shopping-assistant) • [📊 ML Projects](#-machine-learning-projects)

</div>

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [✨ Features](#-features)
- [📦 Dependencies](#-dependencies)
- [🚀 Quick Start](#-quick-start)
- [📚 Workshop Curriculum](#-workshop-curriculum)
  - [1️⃣ Python Fundamentals](#1️⃣-python-fundamentals)
  - [2️⃣ Data Types & Collections](#2️⃣-data-types--collections)
  - [3️⃣ Control Flow & Functions](#3️⃣-control-flow--functions)
  - [4️⃣ Object-Oriented Programming](#4️⃣-object-oriented-programming)
  - [5️⃣ File Handling & Modules](#5️⃣-file-handling--modules)
  - [6️⃣ GUI Development](#6️⃣-gui-development)
  - [7️⃣ Web Scraping](#7️⃣-web-scraping)
  - [8️⃣ NumPy for Numerical Computing](#8️⃣-numpy-for-numerical-computing)
  - [9️⃣ Data Visualization with Matplotlib](#9️⃣-data-visualization-with-matplotlib)
  - [🔟 Machine Learning Projects](#-machine-learning-projects)
- [💬 CaseyBot - AI Shopping Assistant](#-caseybot---ai-shopping-assistant)
- [🎮 Fun Projects](#-fun-projects)
- [📝 Programming Exercises](#-programming-exercises)
- [📁 Repository Structure](#-repository-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [⚠️ Disclaimer](#️-disclaimer)

---

## 🌟 Overview

Welcome to the **AI & Chatbot Development Workshop**! This comprehensive repository contains all the materials, code samples, and projects from a hands-on workshop conducted at **RNSIT College Campus** for the Department of Electronics and Communication.

Whether you're a complete beginner or looking to strengthen your Python skills for AI development, this workshop takes you on a journey from basic Python concepts all the way to building intelligent chatbots and implementing machine learning algorithms.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🐍 **Python Basics** | From Hello World to advanced concepts |
| 📊 **Data Science** | NumPy arrays, data manipulation, and analysis |
| 📈 **Visualization** | 2D & 3D plotting with Matplotlib |
| 🤖 **Machine Learning** | Linear Regression with multiple approaches |
| 💬 **AI Chatbot** | AIML-powered intelligent assistant |
| 🖥️ **GUI Apps** | Desktop applications with Tkinter |
| 🌐 **Web Scraping** | Extract data from websites |
| 🎮 **Fun Projects** | Rock-Paper-Scissors game and more! |

---

## 📦 Dependencies

Make sure you have the following installed:

```bash
# Core Python
Python >= 3.6

# Data Science Libraries
numpy>=1.19.0
matplotlib>=3.3.0
scikit-learn>=0.23.0

# Web Scraping
beautifulsoup4>=4.9.0
html5lib>=1.1

# AI/Chatbot
python-aiml>=0.9.3

# GUI (comes with Python)
tkinter
```

### 📥 Installation

```bash
# Clone the repository
git clone https://github.com/animikhaich/Workshop-on-AI-CHATBOT.git
cd Workshop-on-AI-CHATBOT

# Install dependencies
pip install numpy matplotlib scikit-learn beautifulsoup4 html5lib python-aiml
```

---

## 🚀 Quick Start

```python
# Run any Python file directly
python "01. Introduction.py"

# Start the AI Chatbot
cd CaseyBot
python CaseyBot.py

# Run a Machine Learning demo
python "15. Linear Regression Using SkLearn.py"
```

---

## 📚 Workshop Curriculum

### 1️⃣ Python Fundamentals
> **File:** `01. Introduction.py`

Learn the building blocks of Python programming:

```python
# Variables and Data Types
x = 10000000000000000000000000000000000000000000
x = x + 1
print(x)  # Python handles big numbers naturally!
print(type(x))  # <class 'int'>

# User Input
name = input("Hi! Tell me your name: ")
print("Hi, nice to meet you,", name)

# The Beauty of Python - Swapping Variables
a, b = 2, 3
print("Before:", "a =", a, "| b =", b)
b, a = a, b  # Magic! ✨
print("After:", "a =", a, "| b =", b)

# Any and All Functions (Like OR and AND gates)
mixed = [True, False, True, True]
print("Any (OR Gate):", any(mixed))  # True
print("All (AND Gate):", all(mixed))  # False
```

---

### 2️⃣ Data Types & Collections
> **Files:** `02.1. Datatypes.py`, `02.2. Python_lists.py`

Master Python's powerful data structures:

```python
# 📋 Lists - Mutable sequences
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.extend([7, 8, 9])
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🔒 Tuples - Immutable sequences
coordinates = (10, 20, 30)
x, y, z = coordinates  # Unpacking!

# 🔑 Dictionaries - Key-Value pairs
student = {
    'name': 'Akhilesh',
    'usn': '1RN15EC009',
    'branch': 'ECE'
}
print(student['name'])  # Akhilesh

# 🎯 Sets - Unique elements only
unique_nums = {1, 1, 2, 2, 2, 3, 3, 3, 3}
print(unique_nums)  # {1, 2, 3}

# 🔄 List Slicing
lst = list(range(0, 10))
print(lst[1:9:2])   # [1, 3, 5, 7] - Start:Stop:Step
print(lst[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - Reverse!
```

---

### 3️⃣ Control Flow & Functions
> **Files:** `03. Conditionals and Functions.py`, `04. Loops.py`, `05. One Liners.py`

Control your program flow like a pro:

```python
# 🎯 Conditional Statements
num = int(input('Enter a number: '))
if num > 0:
    print("Positive! ✅")
elif num < 0:
    print("Negative! ❌")
else:
    print("Zero! 🎯")

# 🔄 Loops with else clause
for char in 'RNSIT':
    if char == 'I':
        break
    print(char)
else:
    print("Loop completed!")  # Won't print due to break

# ⚡ Lambda Functions
cube = lambda x: x ** 3
print(cube(3))  # 27

# 🎨 Map and Filter
numbers = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
odds = list(filter(lambda x: x % 2 != 0, numbers))
doubled = list(map(lambda x: x * 2, numbers))

# 🚀 One-Liners (List Comprehensions)
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(20) if x % 2 == 0]
```

---

### 4️⃣ Object-Oriented Programming
> **File:** `07. OOPs.py`

Build robust applications with OOP:

```python
# 📦 Basic Class
class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# 👨‍👩‍👧 Inheritance
class Employee(Person):
    def __init__(self, first, last, staff_num):
        super().__init__(first, last)
        self.staff_number = staff_num
    
    def get_employee_info(self):
        return f"{self.full_name()} - ID: {self.staff_number}"

# 🎯 Multiple Inheritance
class Base1:
    def __init__(self):
        self.str1 = 'Electronics'

class Base2:
    def __init__(self):
        self.str2 = "Computer Science"

class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
    
    def print_str(self):
        print(f"{self.str1}, {self.str2}")

# Usage
employee = Employee("Shahrukh", "Khan", "1011")
print(employee.get_employee_info())  # Shahrukh Khan - ID: 1011
```

---

### 5️⃣ File Handling & Modules
> **Files:** `08. Import Module.py`, `09. File Handling DateTime Time Random.py`

Work with files and create modular code:

```python
# 📂 File Operations
# Reading a file
with open('Database/Elon_Musk.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file
with open('output.txt', 'w') as file:
    file.write('Hello, World!')

# 📅 DateTime Operations
import datetime
today = datetime.date.today()
print(f"Today's date: {today}")
print(f"Day: {today.day}, Month: {today.month}, Year: {today.year}")

# 🎲 Random Module
import random
names = ['Animikh', 'Akhilesh', 'Akshay', 'Aishwarya']
print(random.choice(names))  # Random selection

# 🥒 Pickling (Serialization)
import pickle
data = [1, 2, 3, 4, 5]
with open("data.pkl", 'wb') as file:
    pickle.dump(data, file)
```

---

### 6️⃣ GUI Development
> **File:** `10. GUI.py`

Create desktop applications with Tkinter:

```python
from tkinter import *

# 🖼️ Basic Window
window = Tk()
window.title('My First GUI App')

# 🏷️ Labels
label = Label(window, text='Welcome to Python GUI!', 
              bg='green', fg='white', font=('Arial', 14))
label.pack(pady=10)

# 🔘 Buttons with Commands
def say_hello():
    print("Hello, World!")

button = Button(window, text='Click Me!', command=say_hello)
button.pack()

# 📝 Entry Fields (Grid Layout)
Label(window, text='Username:').grid(row=0, column=0)
Entry(window).grid(row=0, column=1)
Label(window, text='Password:').grid(row=1, column=0)
Entry(window, show='*').grid(row=1, column=1)

window.mainloop()
```

---

### 7️⃣ Web Scraping
> **File:** `11. Web Scraping.py`

Extract data from the web:

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 🌐 Scrape Wikipedia
url = 'https://en.wikipedia.org/wiki/Google'
raw_html = urlopen(url)
html = BeautifulSoup(raw_html, 'html5lib')

# 📑 Get All Headings
headlines = html.findAll("span", {"class": "mw-headline"})
for headline in headlines:
    print(headline.text)

# 📄 Get Paragraph Content
paragraphs = html.findAll("div", {"id": "mw-content-text"})[0].div.findAll("p")
for p in paragraphs[:5]:  # First 5 paragraphs
    print(p.text)
```

---

### 8️⃣ NumPy for Numerical Computing
> **Files:** `12.1 Numpy_Basics.py`, `12.2 Numpy_Advanced.py`, `Numpy Efficiency.py`

Supercharge your computations with NumPy:

```python
import numpy as np

# 📊 Array Creation
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"Shape: {arr.shape}")      # (3, 4)
print(f"Size: {arr.size}")        # 12
print(f"Dimensions: {arr.ndim}")  # 2

# 🔄 Reshaping
reshaped = arr.reshape(6, 2)
print(reshaped)

# ⚡ Array Operations
a = np.array([10, 20, 30, 40, 50])
b = np.arange(1, 6)

print(a + b)      # Element-wise addition
print(a * b)      # Element-wise multiplication
print(np.dot(a, b))  # Dot product: 550

# 📐 Linear Algebra
matrix = np.array([[1, 2], [3, 4]])
print(np.linalg.det(matrix))  # Determinant: -2.0
print(np.linalg.inv(matrix))  # Inverse matrix

# ⏱️ NumPy vs Python Lists (Speed Comparison)
import time
size = 1000000

# Python list operation
start = time.time()
l1, l2 = range(size), range(size)
result = [(x+y) for x, y in zip(l1, l2)]
print(f"Python Lists: {(time.time()-start)*1000:.2f} ms")

# NumPy operation
start = time.time()
a1, a2 = np.arange(size), np.arange(size)
result = a1 + a2
print(f"NumPy Arrays: {(time.time()-start)*1000:.2f} ms")
# NumPy is typically 10-100x faster! 🚀
```

---

### 9️⃣ Data Visualization with Matplotlib
> **Files:** `13.1 Matplotlib_Basics.py`, `13.2 Matplotlib_2D.py`, `13.3 Matplotlib_3D.py`

Create stunning visualizations:

```python
import matplotlib.pyplot as plt
import numpy as np

# 📈 Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, label='Linear', color='blue', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.legend()
plt.show()

# 📊 Bar Chart
categories = ['Python', 'Java', 'C++', 'JavaScript']
values = [85, 70, 60, 75]
plt.bar(categories, values, color=['blue', 'red', 'green', 'orange'])
plt.title('Programming Language Popularity')
plt.show()

# 🥧 Pie Chart
activities = ['Sleep', 'Work', 'Play']
hours = [8, 10, 6]
plt.pie(hours, labels=activities, autopct='%1.1f%%', 
        colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Daily Activities')
plt.show()

# 🌐 3D Plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
ax.scatter(x, y, z, c='red', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

---

### 🔟 Machine Learning Projects
> **Files:** `15. Linear Regression Using SkLearn.py`, `16. Linear Regression Using Algo.py`, `17. Linear Regression Using Neural Networks.py`

Three approaches to Linear Regression:

#### Method 1: Using Scikit-Learn
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
with open('Database/mpg.csv', 'r') as file:
    data = file.read().split('\n')[1:-1]

X = np.array([[float(i.split(',')[4]) for i in data]]).T  # Weight
y = np.array([[float(i.split(',')[0]) for i in data]]).T  # MPG

# Train model
model = LinearRegression()
model.fit(X, y)

# Visualize
plt.scatter(X, y, marker='x', c='blue', label='Data')
plt.plot(X, model.predict(X), c='red', label='Prediction')
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.title('Linear Regression - MPG Prediction')
plt.legend()
plt.show()
```

#### Method 2: From Scratch (Algorithm)
```python
from statistics import mean
import numpy as np

def linear_regression(xs, ys):
    slope = ((mean(xs) * mean(ys) - mean(xs * ys)) /
             ((mean(xs))**2 - mean(xs**2)))
    intercept = mean(ys) - slope * mean(xs)
    return slope, intercept

# Calculate slope and intercept
m, c = linear_regression(X, y)
predictions = m * X + c
```

#### Method 3: Neural Network Approach
```python
# Gradient Descent Implementation
X_normalized = (X - np.mean(X)) / np.std(X)
X_bias = np.hstack((np.ones(N).reshape(N, 1), X_normalized))

weights = np.array([0., 0.])
learning_rate = 1E-4
epochs = 100

for epoch in range(epochs):
    gradient = np.array([0., 0.])
    for i in range(N):
        error = y[i] - np.dot(weights, X_bias[i])
        gradient += X_bias[i] * error
    weights = weights + gradient * learning_rate
```

---

## 💬 CaseyBot - AI Shopping Assistant

> **Location:** `CaseyBot/`

Meet **Casey**, your intelligent shopping assistant powered by AIML (Artificial Intelligence Markup Language)!

### 🎯 Features
- 🗣️ Natural language conversation
- 🛒 Course recommendations
- 💳 Payment processing simulation
- 🎓 Topics: Machine Learning, AI, Java

### 🚀 Run the Chatbot

```bash
cd CaseyBot
python CaseyBot.py
```

### 💬 Sample Conversation

```
Casey: Hello User! Welcome to shopping.com
       I'm Casey! Your Shopping Assistant
       What is your name?

>> Hi, my name is John

Casey: Oh, John that's a nice name! 
       What kind of courses are you looking for?
       Options: Machine Learning, AI, Java

>> I would like to choose Machine Learning

Casey: Ok, John type MACHINE LEARNING to confirm

>> machine learning

Casey: This will be for 3 months

>> What will be the topics covered

Casey: In machine learning you will learn about 
       Algorithms and Types of machine learning
```

### 🔧 AIML Structure

```xml
<category>
    <pattern>HI</pattern>
    <template>Hello there, can I know your name?</template>
</category>

<category>
    <pattern>MY NAME IS *</pattern>
    <template>
        Oh, <set name="user"><star/></set> that's a nice name!
        What courses are you looking for?
    </template>
</category>
```

---

## 🎮 Fun Projects

### 🪨📄✂️ Rock Paper Scissors
> **File:** `ASSIGNMENT RockPaperScissor.py`

```python
from random import choice

choices = ['Rock', 'Paper', 'Scissors']
user_score, computer_score = 0, 0

while True:
    user_input = input('Rock, Paper or Scissors?: ')
    computer_choice = choice(choices)
    
    if user_input.lower() == 'quit':
        print(f"Final: You {user_score} - {computer_score} Computer")
        break
    
    print(f"Computer chose: {computer_choice}")
    
    # Game logic
    if user_input == computer_choice:
        print("Draw! 🤝")
    elif (user_input == 'Rock' and computer_choice == 'Scissors') or \
         (user_input == 'Paper' and computer_choice == 'Rock') or \
         (user_input == 'Scissors' and computer_choice == 'Paper'):
        user_score += 1
        print("You win! 🎉")
    else:
        computer_score += 1
        print("Computer wins! 🤖")
```

---

## 📝 Programming Exercises

> **File:** `Programming assignments.txt`

100+ Python challenges across three difficulty levels:

| Level | Description | Example |
|-------|-------------|---------|
| 🟢 **Level 1** | Beginner - Basic syntax | Find divisible numbers |
| 🟡 **Level 2** | Intermediate - Multiple concepts | Password validator |
| 🔴 **Level 3** | Advanced - Complex algorithms | Robot distance calculation |

### Sample Exercises

<details>
<summary>🟢 Level 1: Factorial Calculator</summary>

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```
</details>

<details>
<summary>🟡 Level 2: Password Validator</summary>

```python
import re

def validate_password(pwd):
    if len(pwd) < 6 or len(pwd) > 12:
        return False
    if not re.search("[a-z]", pwd):
        return False
    if not re.search("[A-Z]", pwd):
        return False
    if not re.search("[0-9]", pwd):
        return False
    if not re.search("[$#@]", pwd):
        return False
    return True

print(validate_password("ABd1234@1"))  # True
```
</details>

<details>
<summary>🔴 Level 3: Fibonacci with Generator</summary>

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
</details>

---

## 📁 Repository Structure

```
📦 Workshop-on-AI-CHATBOT
├── 📂 CaseyBot/                    # AI Chatbot
│   ├── 📂 AIML_Files/              # AIML patterns
│   │   └── abc.aiml
│   ├── CaseyBot.py                 # Main chatbot script
│   └── aiml_dir.xml                # AIML configuration
│
├── 📂 Database/                    # Sample datasets
│   ├── Elon_Musk.txt               # Text sample
│   ├── height.csv                  # Height data
│   └── mpg.csv                     # MPG dataset
│
├── 📂 06. Python To EXE/           # Convert to executable
│   ├── Hello_World.py
│   ├── Instructions.txt
│   └── setup.py
│
├── 📜 01. Introduction.py          # Python basics
├── 📜 02.1. Datatypes.py           # Data types
├── 📜 02.2. Python_lists.py        # Lists
├── 📜 03. Conditionals and Functions.py
├── 📜 04. Loops.py                 # Loop constructs
├── 📜 05. One Liners.py            # List comprehensions
├── 📜 07. OOPs.py                  # OOP concepts
├── 📜 08. Import Module.py         # Modules
├── 📜 09. File Handling DateTime Time Random.py
├── 📜 10. GUI.py                   # Tkinter GUI
├── 📜 11. Web Scraping.py          # BeautifulSoup
├── 📜 12.1 Numpy_Basics.py         # NumPy fundamentals
├── 📜 12.2 Numpy_Advanced.py       # Advanced NumPy
├── 📜 13.1 Matplotlib_Basics.py    # Basic plots
├── 📜 13.2 Matplotlib_2D.py        # 2D visualization
├── 📜 13.3 Matplotlib_3D.py        # 3D plots
├── 📜 15. Linear Regression Using SkLearn.py
├── 📜 16. Linear Regression Using Algo.py
├── 📜 17. Linear Regression Using Neural Networks.py
├── 📜 Add_Mod.py                   # Custom module
├── 📜 ASSIGNMENT RockPaperScissor.py
├── 📜 Numpy Efficiency.py          # Performance comparison
├── 📜 Programming assignments.txt   # 100+ exercises
├── 📜 LICENSE                      # GNU GPLv3
└── 📜 README.md                    # This file
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🌿 Create a **branch** (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 **Push** to branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a **Pull Request**

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

> 📝 The `Programming assignments.txt` file contains exercises from [Python-programming-exercises](https://github.com/zhiwehu/Python-programming-exercises) repository. These solutions are written in Python 2. For Python 3 compatibility, appropriate syntax modifications may be required (e.g., `print()` function, `input()` instead of `raw_input()`).

---

<div align="center">

### 🌟 Star this repository if you found it helpful!

Made with ❤️ by **Animikh Aich** and workshop contributors

[![GitHub](https://img.shields.io/badge/GitHub-animikhaich-181717?style=for-the-badge&logo=github)](https://github.com/animikhaich)

</div>
