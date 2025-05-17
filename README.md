
# 🌞 Solar Challenge Week 1 - 10 Academy

This repository contains the setup and exploratory work for the **B5W0: Solar Data Discovery** challenge, part of the 10 Academy Week 0 assessment. The goal is to analyze solar radiation data from Benin, Togo, and Sierra Leone to identify high-potential regions for solar energy investment.

---

## 📁 Project Structure

```

solar-challenge-week1/
├── .vscode/              # Editor-specific settings
├── .github/workflows/    # CI workflow for Python env
├── src/                  # Core Python modules
├── notebooks/            # Jupyter notebooks for EDA
├── tests/                # Unit tests (TBD)
├── scripts/              # Utility scripts
├── data/                 # Local data folder (ignored in git)
├── .gitignore
├── requirements.txt
├── README.md

````

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Fitsumhelina/solar-challenge-week1.git
cd solar-challenge-week1
````

### 2. Create and Activate Virtual Environment

**Option A: venv**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Option B: conda**

```bash
conda create -n solar-env python=3.10 -y
conda activate solar-env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Continuous Integration (CI)

GitHub Actions is configured to:

* Install dependencies from `requirements.txt`
* Print Python version

File: `.github/workflows/ci.yml`

---

## 🚀 Task 1 Summary

✅ GitHub repo initialized
✅ Virtual environment created (`venv`)
✅ `.gitignore` includes cache, `.csv`, and data
✅ CI/CD pipeline setup with GitHub Actions
✅ PR merged from `setup-task` branch into `main`

---

## 📊 Upcoming Work

Next steps include:

* Exploratory Data Analysis on solar data (Task 2)
* Cleaned dataset preparation
* Comparative analytics (Task 3)
* Streamlit dashboard development (Bonus)

---

## 📅 Submission Timeline

* Interim Submission: **May 18, 2025**
* Final Submission: **May 21, 2025**

---

## 👨‍💻 Author

**Fitsum Helina**
Trainee @ 10 Academy
3rd Year Software Engineering Student | Debre Berhan University

```
