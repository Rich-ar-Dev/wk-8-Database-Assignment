

# 📘 Assignment: Classes, Inheritance & Polymorphism in Python

## 🎯 Learning Objectives

* 🏗️ Practice designing your own classes with attributes and methods.
* 🔄 Explore **constructors** (`__init__`) to initialize objects with unique values.
* 🧬 Implement **inheritance** to build relationships between classes.
* 🎭 Demonstrate **polymorphism** by overriding methods across different classes.

---

## 📝 Assignment Overview

### **Activity 1: Design Your Own Class! 🏗️**

In this activity, we designed a **Book** class to represent real-world objects.

* Attributes: `title`, `author`, `pages`, `genre`.
* Methods: `read()`, `info()`.
* Constructor: Initializes each book with unique values.

We then extended the design with an **EBook** subclass:

* Inherited all attributes from `Book`.
* Added a new attribute: `file_size`.
* Overrode the `info()` method to demonstrate **polymorphism**.
* Added a new method: `download()`.

This demonstrates **object-oriented design**, **encapsulation**, and **inheritance** in action.

---

### **Activity 2: Polymorphism Challenge 🎭**

We explored **polymorphism** by creating an `Animal` base class and multiple subclasses (`Dog`, `Bird`, `Fish`).

* Each subclass overrides the `move()` method.
* The same method call produces different outputs depending on the object type:

  * 🐕 Dog → "runs"
  * 🐦 Bird → "flies"
  * 🐟 Fish → "swims"

This shows how one interface (`move()`) can be implemented differently across related classes.

---

## 📂 Files Included

* `assignment1.py` → Python code for both activities.
* `README.md` → Documentation of objectives, design, and explanation.

---

## 🚀 How to Run

1. Ensure Python 3 is installed on your machine.
2. Open a terminal in the assignment folder.
3. Run:

   ```bash
   python assignment1.py
   ```
4. Observe outputs for both **Activity 1** and **Activity 2**.

---

## ✅ Key Concepts Demonstrated

* **Encapsulation** → Grouping related data and methods in classes.
* **Constructors** → Initializing objects with unique values.
* **Inheritance** → Creating subclasses that reuse and extend parent class functionality.
* **Polymorphism** → Same method name behaving differently across classes.


