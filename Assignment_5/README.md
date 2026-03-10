# Task 05: Modules and Packages 📦

## 📝 Problem Statement
This assignment focuses on organizing Python code into a professional, scalable structure. By creating custom modules and packages, I have implemented a reusable system for mathematical utilities, string manipulation, and e-commerce billing logic.

## 🏗️ Folder Structure
The project is organized into a main execution script and specialized utility files:
* **Modules**: `math_utils.py` and `string_utils.py` for general functions.
* **Package**: `shop_package/` containing `discount.py` and `billing.py`, initialized via `__init__.py`.

## 🚀 Key Features
1. **Namespace Management**: Using different import styles (`import module` vs `from module import function`) to manage scope.
2. **Package Initialization**: Using `__init__.py` to allow direct function calls from the package level.
3. **Aliasing**: Using `as` to simplify package references (e.g., `import shop_package.discount as disc`).


## ⚙️ How to Run
1. Navigate to the `modules_assignment` folder.
2. Run the main script: `python main.py`.