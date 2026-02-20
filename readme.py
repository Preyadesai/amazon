# 🛒 Mini Amazon – Console-Based E-Commerce System

## 📌 Project Overview

This project is a console-based Mini Amazon / E-Commerce system built using Python.  
It simulates a simplified online shopping platform where users can register, log in, browse products, manage a shopping cart, and place orders.

The system uses JSON file storage for data persistence and follows Object-Oriented Programming (OOP) principles with modular design.

---

## 🎯 Features Implemented

### 👤 User System
- User registration (unique username required)
- Password validation (minimum 6 characters)
- Password hashing using `hashlib` (SHA-256)
- User login authentication
- Persistent user storage (`users.json`)

---

### 📦 Product Catalog
- List all available products
- Search products by name (case-insensitive)
- View product details
- Stock validation before adding to cart
- Persistent product storage (`products.json`)

---

### 🛒 Cart System
- Add items to cart
- Remove items from cart
- View cart with:
  - Product name
  - Quantity
  - Unit price
  - Subtotal
- Display total cart value
- Persistent cart storage (`carts.json`)

---

### 💳 Checkout System
- Re-validates stock before purchase
- Deducts purchased quantities from stock
- Generates unique order ID
- Saves order history
- Clears cart after successful checkout
- Exports receipt as a text file
- Persistent order storage (`orders.json`)

---

## 🗂 Project Structure
