# Student_Management_System_in_python

## Features:

 1. Admin Privileges: The project focuses on providing exclusive admin privileges, ensuring secure access and control over the student management system.

 2. Efficient Student Data Management: The project enables seamless management of student records, including their ID, name, gender, mobile number, email, date of birth (DOB), and added date.

 3. User-friendly Interface: The application offers a user-friendly interface designed with Tkinter GUI toolkit, making it easy to navigate and operate for administrators.

 4. Add Student: Administrators can add new student information by entering the required details, ensuring comprehensive and up-to-date data.

 5. Search Student: The project provides a search functionality to locate specific students based on their ID, name, gender, mobile number, email, or DOB, simplifying the process of retrieving relevant records.

 6. Update Student: Administrators have the ability to update existing student records, allowing them to modify information such as name, gender, mobile number, email, and DOB as needed.

 7. Delete Student: The application allows administrators to delete student records, facilitating the removal of outdated or unnecessary data from the system.

 8. Sorting and Ordering: The student records can be sorted and ordered based on various columns such as ID, name, gender, mobile number, email, DOB, and added date, providing flexibility in data presentation.

 9. Export Data: Administrators can export the student data to a CSV file, enabling easy sharing and analysis of the information.
 10. Schema used for 'student' table:

 - id: int
 - name: varchar(25)  
 - gender: varchar(7)  
 - mobile: varchar(13)  
 - email: varchar(30) 
 - dob: date 
 - added_date: date 


## How to Install and Run this project?
### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. MySQL Server
[ https://dev.mysql.com/downloads/mysql/ ]

4. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv .
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

For Linux
```
$  source bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/ktoyesh04/Student_Management_System_in_python.git
```

Then, Enter the project
```
$  cd Student_Management_System_in_python
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip3 install -r requirements.txt
```

**5. Add the database details**

- Got to right_frame.py file, line no.42  
- Then replace with your details
```python
entries = {'host': 'your_host', 'user': 'your_user', 'password': 'your_password'}
```
- Enter your database name at line no.55
```python
cursor.execute('use your_database')
```
