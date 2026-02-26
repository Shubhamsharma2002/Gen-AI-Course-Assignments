# Task 04: Python File Handling 📂

## 📝 Problem Statement
This assignment involves building retail analytics utilities to manage sales and product data using Python's native file handling capabilities. It covers the complete lifecycle of data persistence including:
* **File Modes**: Using `w` (write), `r` (read), and `a` (append) effectively.
* **Reading Techniques**: Utilizing `.read()`, `.readline()`, and `.readlines()` for different data extraction needs.
* **Data Export**: Generating formatted summary reports and exporting processed dictionary data to text files.

## 📁 Files in this Folder
* `file_handling_assignment.ipynb`: Full solution containing Tasks 1 through 7.
* `sales_data.txt`: Generated file containing raw sales amounts.
* `products.txt`: Generated file containing user-input product details.
* `discount_report.txt`: Final exported report with calculated discounts.
* `README.md`: This documentation.

## 🚀 Key Features
1. **Dynamic Sales Tracking**: Ability to write initial records and append new sales data without overwriting existing files.
2. **Robust Reporting**: Automated calculation of business metrics (Total, Max, Min, Avg) directly from stored files.
3. **Safe File Operations**: Implementation of `os.path.exists()` to prevent program crashes during file reading.


## ⚙️ How to Run
1. Open the `.ipynb` file in **Jupyter Notebook**.
2. Ensure you have write permissions in the local directory for file creation.
3. Run cells sequentially; follow the prompts for Task 5, 6, and 7.