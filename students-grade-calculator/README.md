# Student Grade Calculator

A beginner-friendly Python project that calculates a student's grade based on marks and displays encouraging messages. The program uses **if-elif-else conditions, functions, while loops, and input validation**.

---

## Project Overview

### Goal

The goal of this project is to create a simple grading system that:

* Accepts student name and marks as input
* Validates marks between **0 and 100**
* Calculates grade using grading rules
* Displays personalized encouraging messages
* Handles invalid input without crashing

### Learning Objectives

This project demonstrates:

* Decision making using **if-elif-else**
* Repetition using **while loops**
* Reusable code using **functions**
* Input validation and basic error handling
* Console-based user interaction

---

## Grading Logic

The program follows this grading system:

| Marks Range | Grade |
| ----------- | ----- |
| 90-100      | A     |
| 80-89       | B     |
| 70-79       | C     |
| 60-69       | D     |
| 0-59        | F     |

### Encouraging Messages

* **A:** Excellent! Outstanding performance!
* **B:** Very Good! Keep it up!
* **C:** Good effort! You can do even better!
* **D:** Keep practicing, improvement is possible!
* **F:** Do not give up. Work hard and try again!

---

## Functions Used

### `calculate_grade(marks)`

**Purpose:** Determines the student's grade and returns an encouraging message.

**Input:** Integer marks (0-100)

**Output:** Grade and message

Example:

```python
grade, message = calculate_grade(85)
```

Returns:

```python
("B", "Very Good! Keep it up! 👍")
```

---

## Setup Instructions

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Verify Installation

Open terminal or command prompt and run:

```bash
python --version
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/Sakshiiikashyap/work/tree/main/students-grade-calculator
```

### Step 4: Open the Project Folder

```bash
cd student-grade-calculator
```

### Step 5: Run the Program

```bash
python grade_calculator.py
```

---

## Code Structure

```text
student-grade-calculator/
│
├── README.md
├── grade_calculator.py
├── test_cases.txt
└── screenshots/
    ├── valid_input.png
    ├── invalid_input.png
    └── final_result.png
```

### File Description

| File                | Purpose               |
| ------------------- | --------------------- |
| README.md           | Project documentation |
| grade_calculator.py | Main Python program   |
| test_cases.txt      | Testing examples      |
| screenshots/        | Output screenshots    |

---

## Program Workflow

### Step-by-Step Flow

1. User enters student name
2. Program asks for marks
3. **While loop** keeps asking until valid input is provided
4. Marks are checked to be between **0 and 100**
5. `calculate_grade()` determines grade
6. Final result is displayed

---

## Technical Details

### Algorithm

#### Input Validation Algorithm

```text
START
Ask for marks
IF input is not a number
    Show error
    Ask again
ELSE IF marks are not between 0 and 100
    Show range error
    Ask again
ELSE
    Accept input
END
```

#### Grade Calculation Algorithm

```text
IF marks >= 90 → Grade A
ELSE IF marks >= 80 → Grade B
ELSE IF marks >= 70 → Grade C
ELSE IF marks >= 60 → Grade D
ELSE → Grade F
```

### Data Structures Used

| Structure             | Usage                             |
| --------------------- | --------------------------------- |
| Variables             | Store name, marks, grade, message |
| Function return tuple | Return grade and message together |
| String formatting     | Display formatted output          |

### Architecture

```text
User Input
    ↓
Validation (while + try-except)
    ↓
Grade Function
    ↓
Result Display
```

---

## Sample Output

```text
Enter student name: Priya
Enter marks (0-100): 85

📊 RESULT FOR PRIYA
Marks: 85/100
Grade: B
Message: Very Good! Keep it up! 👍
```

---

## Testing Evidence

### Test Case 1 - Grade A

| Input | Expected Output |
| ----- | --------------- |
| 95    | Grade A         |

### Test Case 2 - Grade B

| Input | Expected Output |
| ----- | --------------- |
| 85    | Grade B         |

### Test Case 3 - Grade C

| Input | Expected Output |
| ----- | --------------- |
| 74    | Grade C         |

### Test Case 4 - Grade D

| Input | Expected Output |
| ----- | --------------- |
| 62    | Grade D         |

### Test Case 5 - Grade F

| Input | Expected Output |
| ----- | --------------- |
| 45    | Grade F         |

### Validation Test Cases

| Input | Expected Behavior      |
| ----- | ---------------------- |
| 150   | Ask again              |
| -10   | Ask again              |
| abc   | Show numeric error     |
| 89.5  | Reject if integer only |

---

## Example `test_cases.txt`

```text
95 -> A
85 -> B
74 -> C
62 -> D
45 -> F
150 -> Invalid
-5 -> Invalid
abc -> Invalid
```

---

## Quality Standards Checklist

### Project Requirements

* [x] Uses **if-elif-else**
* [x] Uses at least **one function**
* [x] Uses **while loop** for validation
* [x] Handles invalid input
* [x] Displays encouraging messages
* [x] Includes documentation
* [x] Includes test cases
* [x] Includes screenshots
* [x] Organized file structure

---

## Skills Demonstrated

* Python fundamentals
* Conditional statements
* Loops
* Functions
* Error handling
* Input validation
* Program organization
* GitHub project documentation

---

## Future Improvements

Possible enhancements:

* Multiple student support
* Save results to a file
* Percentage calculator
* Grade statistics
* Graphical user interface (Tkinter)
* Database integration

---

## Author

**Sakshi Kashyap**
B.Tech CSE Student | Aspiring AI/ML Engineer

---

## Conclusion

This project successfully implements a **Student Grade Calculator** using core Python concepts. It validates user input, calculates grades accurately, displays encouraging feedback, and demonstrates structured programming practices suitable for beginner-level software development and academic submission.
