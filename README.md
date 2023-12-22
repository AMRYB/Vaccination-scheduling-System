
## 📌 About the Project
The **Vaccination Scheduling System** is a Python-based console application built to help Egypt's Ministry of Health manage and organize the vaccination process.  
It enables two roles:

- **Users**: Register, reserve a vaccination, and check appointment status.
- **Admins**: Manage vaccination centers and handle reservation approvals.

The system uses local `.txt` files as a simple database for storing users, centers, and appointments.

---

## ⚙️ System Workflow

### 👤 User Flow
1. Launch `main.py` and choose **(u)**.
2. Register (if new) or log in using email and password.
3. View available vaccination centers and vaccines.
4. Submit a vaccination request.
5. Track request status or view appointment date after admin approval.

### 🛠️ Admin Flow
1. Launch `main.py` and choose **(a)**.
2. Log in using admin credentials.
3. Admins can:
   - Add or remove vaccination centers.
   - Search for centers by name.
   - View user requests.
   - Approve or reject reservations.
   - Assign vaccination dates.

---

## 🗃️ Project Files Overview

| File Name                | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `main.py`                | Entry point of the program. Lets user choose between Admin and User modes.  |
| `User_registration.py`   | Handles user registration and login process.                                |
| `Reserve_vaccination.py` | Allows logged-in users to make reservations and check their vaccination status. |
| `Admin_registration.py`  | Manages admin login and displays admin options.                             |
| `Vaccine_Administration.py` | Contains all admin-side functionalities: center management, approvals, search. |

---

## 📂 Data Files Format

| File Name               | Purpose                                  | Format Example |
|-------------------------|------------------------------------------|----------------|
| `user_data.txt`         | Stores registered user information.      | `U01, Amr, amr10tuf@email.com, 1234, 01211774738, 30601010000000` |
| `admin_data.txt`        | Stores registered admin info.            | `A01, Admin, admin@email.com, admin123, 0111111111, 98765432109876` |
| `VaccinationCenter.txt` | Holds vaccination center data.           | `C01, Cairo Center, Nasr City, Pfizer, Moderna` |
| `vaccination_records.txt` | Stores vaccination requests.           | `U01, Amr, Cairo Center, Pfizer, Under review` or `2025-07-10` or `Rejected` |

---

## 🚀 How to Run the Project

1. Make sure you have Python 3 installed.
2. Place all `.py` and `.txt` files in the same folder.
3. Open your terminal or command prompt.
4. Run the program using:
   ```bash
   python main.py
## ✅ Choose Mode

- `(u)` to **log in or register as a User**  
- `(a)` to **log in as an Admin**

---

## 🔧 Features Summary

### 👤 Users
- ✅ Register & login securely  
- 🏥 View vaccination centers and vaccine types  
- 📄 Reserve vaccination  
- 📅 Check appointment status after admin approval  

### 🛠️ Admins
- ➕ Add or ➖ remove vaccination centers  
- 🔍 Search centers by name  
- 👥 View user reservations  
- ✅ Approve or ❌ reject vaccination requests  
- 🗓️ Set appointment dates for approved users  

---

## 👨‍👩‍👧‍👦 Team Members

- **Project Leader:** Amr Yasser  

**Team Members:**
- Farid El-Sharkawy  
- Omar Rahab  
- Ahmed Nasr  
- Omar Shrief  
- Abdullah Adel  

> 🛠️ This project was manually developed with assistance from **ASWEPRO** and **TA. Khulood**.