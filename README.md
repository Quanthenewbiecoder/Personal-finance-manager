# Financial Manager Project

## 🚀 Project Overview  

The **Financial Manager** is a dynamic personal finance management application crafted to empower users to take control of their finances. With its user-friendly interface and robust functionality, this application simplifies the tracking of income, expenses, and savings.  

Built using **Flask** for backend operations, **HTML**, **CSS**, and **JavaScript** for the Front-end, and **SQLite** for data management, this project demonstrates my ability to design, develop, and deploy scalable software solutions.  

Key features:  
- **Secure Authentication**: Ensures user data is protected.  
- **Transaction Management**: Allows users to add, edit, or delete income and expenses.  
- **Data Insights**: Visualizes financial health with balances and summaries.  
- **Responsive Design**: Ensures usability on all devices.  

---

### 🎥 Watch the Demo  

Click the image below to watch the demo on YouTube:  

[![Watch the Demo](https://img.youtube.com/vi/d60LIeFdBEU/0.jpg)](https://youtu.be/d60LIeFdBEU?si=L0jFZi9nZG-jlvOJ)

---

## 🖼️ Screenshots  

### **Dashboard**  
Provides a comprehensive summary of income, expenses, and savings.  
![Dashboard](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/Dashboard.png)  

### **Login Page**  
Streamlined login form with real-time validation.  
![Login Page](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/Login.png)  

### **Successful Login Message (Popup)**  
Confirms secure access to user accounts.  
![Login Successful](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/loginnoti.png)  

### **Register Page**  
Enables new users to sign up with ease.  
![Register Page](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/Register.png)  

### **Successful Registration Message (Popup)**  
Welcomes new users with a success notification.  
![Register Successful](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/registernoti.png)  

### **Add Transaction**  
Quickly add new income or expenses.  
![Add Transaction](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/Add_transaction.png)

### **Edit Transaction**  
Modify existing financial entries with ease.  
![Edit Transaction](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/Edit_transaction.png)  

### **Balances Overview**  
Visualizes balances across months for easy comparison.  

#### December Balances  
![December Balances 1](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/December2.png)  
![December Balances 2](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/December2.png)  

#### September Balance  
![September Balance](https://raw.githubusercontent.com/Quanthenewbiecoder/Personal-finance-manager/main/app/static/projectimage/September.png)  

---

## 🛠️ File Structure and Functionality  

### `/app/__init__.py`  
Initializes the Flask application and integrates SQLAlchemy for database management and Flask-Babel for localization.  

### `/app/models.py`  
Defines robust database models to manage user credentials securely and handle financial transactions efficiently.  

### `/app/routes.py`  
Manages application routing, including:  
- **User Authentication**: Secure login and registration routes.  
- **Dashboard**: Displays financial summaries.  
- **Transaction Management**: Enables adding and editing transactions.  

### `/app/templates/`  
Uses Jinja2 templates to deliver a consistent, responsive UI.  

### `/app/static/`  
Hosts CSS and JavaScript files for styling and interactivity, ensuring a modern user experience.  

### `config.py`  
Stores essential configuration settings, emphasizing security with environment variables.  

### `run.py`  
Launches the Flask development server for testing and deployment.  

---

## 🏆 Why This Project Stands Out  

- **Real-World Problem Solving**: Addresses a common pain point—financial management—through innovative solutions.  
- **Scalable Architecture**: Designed to accommodate future enhancements like budget tools and data visualization.  
- **Technical Expertise**: Demonstrates proficiency in Python, Flask, SQLAlchemy, HTML/CSS, and JavaScript.  
- **User-Centric Design**: Built with a focus on accessibility and responsiveness.  

---

## 🌟 Future Enhancements  

- **Budgeting Tools**: Introduce goal-setting features for better financial planning.  
- **Data Visualization**: Add charts for transaction trends and analysis.  
- **Multi-Currency Support**: Expand usability for global users.  
