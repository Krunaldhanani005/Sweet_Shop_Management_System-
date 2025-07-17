# Sweet_Shop_Management_System-
Simple Sweet Shop Management System following TDD that allows users to  perform basic operations such as adding sweets, updating sweet details, deleting sweets,  searching, sorting, and viewing available sweets. 

# 🍬 Sweet Shop Management System

This is a simple web-based Sweet Shop Management System developed using **Python (Flask)** and **MySQL**. It allows shopkeepers to manage sweets inventory efficiently — including features like adding, deleting, purchasing, restocking, and viewing sweets.

---

## 🔧 Tech Stack

- **Frontend**: HTML, Bootstrap 4 (via CDN)
- **Backend**: Python (Flask)
- **Database**: MySQL
- **Tools**: MySQL Workbench, GitHub

---

## 📦 Features

### 🎯 Core Functionality
- **Add Sweet**: Add a new sweet with ID, name, category, price, and quantity.
- **View Sweets**: Display all sweets in a table with search and sort features.
- **Search & Sort**: Search sweets by name or category and sort by ID, name, price, etc.
- **Purchase**: Reduce quantity from inventory when a sweet is purchased.
- **Restock**: Add quantity back to stock.
- **Delete**: Remove a sweet permanently from the system.

### 🔒 Error Handling
- Duplicate IDs are handled gracefully using flash messages.
- Purchase operations ensure sufficient stock exists before processing.

---

## 🗃️ Database Schema

```sql
CREATE DATABASE sweet_shop;

USE sweet_shop;

CREATE TABLE sweets (
  id VARCHAR(10) PRIMARY KEY,
  name VARCHAR(50),
  category VARCHAR(50),
  price FLOAT,
  quantity INT
);

📁 Project Structure

sweet-shop-management/
│
├── app.py             # Main Flask application
├── db.py              # Database helper functions
├── templates/
│   └── index.html     # HTML front-end
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation