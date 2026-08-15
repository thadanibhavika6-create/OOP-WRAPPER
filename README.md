# OOP-WRAPPER

# 🧑‍💼 Employee Management System — Python OOP Project

A simple, menu-driven **console application** built in **Python** using **Object-Oriented Programming** to manage Person, Employee, and Manager records — create and view details, all through an easy-to-use terminal interface.

---

## 🚀 Project Overview

This project is an **Employee Management System** built using **core Python OOP** (no external libraries required). It allows a school, company, or admin to maintain Person, Employee, and Manager records directly from the terminal with a clean menu system.

The tool lets you:

- 🧍 **Create a Person** — store name & age
- 👔 **Create an Employee** — store name, age, employee ID & salary
- 🧑‍💼 **Create a Manager** — store name, age, ID, salary & department
- 📋 **Show Details** — view Person / Employee / Manager records on demand
- 🚪 **Exit** — close the program safely, freeing all resources

It's a great beginner-to-intermediate project demonstrating **classes, inheritance, encapsulation, and polymorphism** in Python.

---

## 🗂️ Project Files

| File Name | Description |
|---|---|
| 🐍 `employee_management.py` | Main Python script with all functionality |
| 📘 `README.md` | Project documentation |

---

## 🧩 Program Structure

The program runs on a **`while True` main loop** displaying a menu, and routes user choices to the following features:

| Menu Option | Functionality |
|---|---|
| `1` | Create a Person |
| `2` | Create an Employee |
| `3` | Create a Manager |
| `4` | Show a Details |
| `5` | Exit the program |

---

## 🔹 Key Features

### 1️⃣ Create a Person
Collects and stores:
- Name
- Age

### 2️⃣ Create an Employee
Extends `Person` and additionally collects:
- Employee ID
- Salary

### 3️⃣ Create a Manager
Extends `Employee` and additionally collects:
- Department

### 4️⃣ Show a Details
Lets the user pick **Person / Employee / Manager** and prints that record's full details in a clean, aligned format.

### 5️⃣ Exit
Gracefully ends the program with a "resources freed" and thank-you message.

---

## 🏗️ Class Hierarchy

```
Person
  ├── name
  ├── age
  │
  └── Employee (inherits Person)
        ├── emp_id
        ├── salary
        │
        └── Manager (inherits Employee)
              └── department
```

---

## 📦 Record Fields

| Field | Description |
|---|---|
| `name` | Full name of the person |
| `age` | Person's age |
| `emp_id` | Unique Employee ID |
| `salary` | Employee's / Manager's salary |
| `department` | Manager's department |

---

## 🛠️ Tools & Concepts Used

**Python (Core / Standard Library only):**
- ✅ Classes & Objects for record modeling
- ✅ Inheritance (`Employee → Person`, `Manager → Employee`)
- ✅ Encapsulation of attributes within classes
- ✅ `while` loop for menu-driven interface
- ✅ Conditional statements (`if` / `elif`)
- ✅ `input()` for user interaction
- ✅ Type casting (`int()`)

---

## ▶️ How to Run

1. Make sure **Python 3** is installed on your system
2. Clone or download this repository
3. Open a terminal in the project folder
4. Run the script:
   ```bash
   python employee_management.py
   ```
5. Follow the on-screen menu to create Persons, Employees, or Managers and view their details

---

## 📌 Sample Workflow

1. Choose `1` → Create a Person
2. Choose `2` → Create an Employee
3. Choose `3` → Create a Manager
4. Choose `4` → Show details of any saved record
5. Choose `5` → Exit the program

---

## 🌟 Future Enhancements

- 💾 Save/load data to a file (CSV / JSON) for persistence
- 🔎 Search records by name or ID
- ✅ Input validation (e.g., age, salary checks)
- 🖥️ GUI version using Tkinter
- 🗃️ Database integration (SQLite)
- 📊 Export employee records to Excel/CSV report

---

## 🖥️ Sample Output

<img width="735" alt="employee_management_output" src="employee_management_output.png" />

---

## 👩‍💻 Author

**Bhavika**
📍 India

---

## 🙌 Feedback & Contributions

Suggestions, improvements, and pull requests are always welcome! Feel free to **fork** this repository or open an **issue** if you'd like to contribute.

---
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-9B59B6)
![Made with](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)


> 🧑‍💼 *Managing People and Employees, One Record at a Time*
