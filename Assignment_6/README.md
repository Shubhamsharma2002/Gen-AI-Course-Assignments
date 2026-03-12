# Task 06: Exception Handling 🛡️

## 📝 Problem Statement
This assignment focuses on building "crash-proof" applications by handling runtime errors and unexpected user inputs. I have implemented various safeguards to manage data types, mathematical errors, and file system issues using:
* **Try-Except Blocks**: To catch specific errors like `ValueError` and `ZeroDivisionError`.
* **Else & Finally**: To manage code execution flow regardless of whether an error occurred.
* **Custom Exceptions**: Using `raise` to enforce business rules (e.g., age ranges or negative prices).

## 📁 Files in this Folder
* `exception_handling_assignment.ipynb`: Full solution containing Tasks 1 through 5.
* `README.md`: This documentation file.

## 🚀 Key Features
1. **Safe Calculations**: A division utility that handles non-numeric input and division by zero.
2. **Data Sanitization**: A bill calculator that skips strings and negative values while continuing to process valid items.
3. **Age Validation**: Logic to ensure user-provided ages fall within a realistic 1-120 range.
4. **Resilient Shopping Cart**: An interactive loop that collects prices and summarizes totals while ignoring invalid entries.


## ⚙️ How to Run
1. Open the `.ipynb` file in **Jupyter Notebook**.
2. Run the cells sequentially.
3. Call the specific functions (e.g., `safe_shopping_cart()`) to interact with the programs.