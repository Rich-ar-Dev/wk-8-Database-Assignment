# Library Management System - Database Schema

## Overview
This repository contains a complete MySQL database schema for a Library Management System. The database is designed to handle books, members, loans, reservations, and other essential library operations with proper relational integrity and constraints.

## Database Design

### Tables Structure

#### 1. Members Table
Stores information about library members with constraints to ensure data integrity.

#### 2. Books Table
Contains details about books in the library collection with availability tracking.

#### 3. Loans Table
Manages book borrowing transactions with foreign key relationships to members and books.

#### 4. Authors Table
Stores author information separate from books to support multiple authors per book.

#### 5. Book_Authors Junction Table
Implements a many-to-many relationship between books and authors.

#### 6. Reservations Table
Tracks book reservations by members.

#### 7. Fines Table
Manages fine records for overdue books.

## Relationships
- One-to-Many: Members → Loans
- One-to-Many: Books → Loans
- Many-to-Many: Books ↔ Authors (via book_authors junction table)
- One-to-Many: Members → Reservations
- One-to-Many: Books → Reservations
- One-to-Many: Members → Fines
- One-to-Many: Loans → Fines

## Constraints Implemented
- PRIMARY KEY constraints on all main tables
- FOREIGN KEY constraints to maintain referential integrity
- UNIQUE constraints on email and ISBN fields
- NOT NULL constraints on required fields
- ENUM constraints for status fields
- DEFAULT values for common fields

## Installation

1. Ensure MySQL Server is installed and running
2. Execute the SQL file to create the database and tables:

```bash
mysql -u your_username -p < library_management_system.sql
```

## Sample Data
The SQL file includes sample data for:
- 3 library members
- 3 books with different genres
- 3 authors
- Book-author relationships

## Indexes
The schema includes indexes on frequently queried columns for performance optimization:
- Member emails
- Book ISBNs and titles
- Loan statuses and relationships
- Reservation relationships

## Usage
After executing the SQL script, you'll have a fully functional library management database that can be integrated with applications for managing:
- Member registrations and management
- Book cataloging and inventory
- Loan transactions and tracking
- Reservation systems
- Fine calculation and management

## File Structure
```
library_management_system.sql - Complete database schema with sample data
```

