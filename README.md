# Integrating Flask App with MySQL for Database Query 🚀

## Project Overview 🌟

This project demonstrates how to integrate a Flask application with a MySQL database to execute and display SQL queries. Users can input SQL queries in the frontend, and the application will retrieve and display the results from a local MySQL database.

## Project Structure 📁

- `app.py` 🐍: The main Flask application file.
- `templates/` 🗂️: Contains HTML files for frontend and results display.
  - `index.html` 📝: Frontend form for entering SQL queries.
  - `result.html` 📊: Displays the results of the executed SQL query.
- `static/` 🗂️: Contains static files like CSS.
  - `style.css` 🎨: CSS file for styling the frontend and results.

## Set Up MySQL Database 🛠️

1. Ensure that MySQL Server is installed and running on your local machine. ⚙️
2. Create a database named `instagram_clone` in MySQL. 🗃️
3. Make sure the database is accessible with the following credentials:
   - **Host:** 127.0.0.1 🌐
   - **User:** root 🔑
   - **Password:** root 🔑

## Configure Database Connection 🔧

In `app.py`, ensure that the database configuration matches your local MySQL setup:

```python
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
DATABASE = 'instagram_clone' 
``` 
## Add HTML and CSS Files 📄

- Place `index.html` and `result.html` in the `templates` folder. 📂
- Place `style.css` in the `static` folder. 📂

## Install Dependencies 📦

Install the required Python packages using pip:

```bash
pip install flask pymysql
```

## Notes 📝

- Ensure that the HTML files are placed in the `templates` folder and the CSS file is in the `static` folder.
- Verify that your MySQL database is set up and accessible with the specified credentials for the application to function correctly.
- create the `instagram_clone` database or any other database you wish to use

### Contact Information 📫

- **Name**: Akash Anandani
- **Email**: akashanandani.56@gmail.com

Happy coding and good luck with your project! 🎉
