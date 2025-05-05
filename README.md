# 🎭 Playwright Python Testing Project

This is a **training project** created during my learning journey on the LinkedIn course **"Learning Playwright" by Butch Mayhew**.

While the course focuses on **Playwright with Node.js and JavaScript**,  
I decided to **adapt the concepts to a Python stack** using **Playwright + Pytest**, applying the **Page Object Model (POM)** architecture.

---

## 🧪 Tech Stack

- **Python 3.12**
- **Playwright for Python**
- **Pytest**
- **pytest-asyncio**
- **Page Object Model (POM)**

---

## ✅ What Has Been Learned and Implemented

1. **Playwright installation and configuration** for Python.
2. **Project environment setup** using `venv`, `pytest.ini`, and `Makefile`.
3. **Test structure** is based on:
   - Page Object Model (POM)
   - Custom fixtures (`conftest.py`)
   - Test data parametrization from the `data/` directory.
4. All dependencies are listed in `requirements.txt`.
5. **API testing**: Used Playwright to interact with APIs and validate data in assertions.
6. **Visual testing**: Tried basic visual regression testing using a Playwright plugin.
7. **Authentication**: Implemented cookie-based authentication for test sessions.

---

## 🚀 Setup Instructions

Clone the repository and set up your virtual environment:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install browser binaries
playwright install

## 📁 Project Structure (in progress)

├── Makefile
├── README.md
├── conftest.py
├── pytest.ini
├── requirements.txt
├── data/
│   ├── auth_test_data.py
│   └── product_filter_data.py
├── pages/
│   ├── admin_page.py
│   ├── auth_page.py
│   ├── base_page.py
│   ├── main_menu_page.py
│   ├── api/
│   │   └── products_api.py
│   ├── catalog/
│   │   ├── filter_panel_page.py
│   │   ├── pagination_page.py
│   │   ├── product_grid_page.py
│   │   └── search_bar_page.py
│   └── product/
│       └── product_page.py
├── tests/
│   ├── api/
│   │   └── test_api.py
│   └── ui/
│       ├── auth/
│       ├── catalog/
│       ├── test_account_page.py
│       ├── test_main_menu.py
│       ├── test_product_page.py
│       └── test_saved_session.py
├── utils/
└── venv/  # virtual environment (in .gitignore)