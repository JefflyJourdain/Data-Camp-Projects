# 🏅 Nobel Prize Data Analysis (1901–2023)

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-lightblue)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-teal)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

Exploratory data analysis of every Nobel Prize awarded between 1901 and 2023, uncovering patterns across gender, nationality, categories, and repeat winners.

---

## 📌 Overview

The Nobel Prize is one of the most prestigious international awards, granted annually in Chemistry, Literature, Physics, Physiology or Medicine, Economics, and Peace. This project uses the official Nobel Prize API dataset to answer key questions about prize-winning trends across more than a century of awards.

---

## 🎯 Key Questions Answered

| # | Question |
|---|----------|
| 1 | What is the most common gender and birth country among all laureates? |
| 2 | Which decade had the highest proportion of US-born winners? |
| 3 | Which decade–category combination had the highest share of female winners? |
| 4 | Who was the first woman to win a Nobel Prize, and in which category? |
| 5 | Which individuals or organizations have won the prize more than once? |

---

## 🗂️ Dataset

**Source:** [Nobel Prize API](https://www.nobelprize.org/about/developer-zone-2/) — accessed via DataCamp  
**File:** `data/nobel.csv`  
**Coverage:** 1901–2023

### Columns

| Column | Description |
|--------|-------------|
| `year` | Year the prize was awarded |
| `category` | Prize category (e.g. Physics, Peace) |
| `prize` | Full prize name |
| `motivation` | Official motivation for the award |
| `prize_share` | Fraction of the prize received |
| `laureate_id` | Unique laureate identifier |
| `laureate_type` | Individual or Organization |
| `full_name` | Laureate's full name |
| `birth_date` | Date of birth |
| `birth_city` | City of birth |
| `birth_country` | Country of birth |
| `sex` | Gender |
| `organization_name` | Affiliated organization |
| `organization_city` | Organization city |
| `organization_country` | Organization country |
| `death_date` | Date of death (if applicable) |
| `death_city` | City of death |
| `death_country` | Country of death |

---

## 🔍 Analysis Summary

### 1 · Most common gender and birth country
The dominant gender among Nobel laureates is **Male**. The country producing the most winners is the **United States of America**.

### 2 · Decade with highest US-born winner proportion
A binary flag was created for US-born laureates. The mean flag per decade identifies the era of peak American dominance in Nobel Prize history.

### 3 · Female winner proportion by decade and category
Female winners were flagged (1/0) and averaged across every decade–category pair. The combination with the highest proportion was **Literature in the 2020s**.

### 4 · First female Nobel laureate
Filtering to female winners and sorting chronologically reveals **Marie Curie** as the first woman to win, awarded the **Physics** prize.

### 5 · Repeat winners
The following individuals and organizations have won the Nobel Prize more than once:

- Comité international de la Croix Rouge (International Committee of the Red Cross)
- Frederick Sanger
- John Bardeen
- Linus Carl Pauling
- Marie Curie, née Sklodowska
- Office of the United Nations High Commissioner for Refugees (UNHCR)

---

## 📁 Project Structure

```
├── data/
│   └── nobel.csv               # Nobel Prize dataset (1901–2023)
├── notebook_commented.ipynb    # Annotated analysis notebook
├── Nobel_Prize.png             # Header image used in the notebook
└── README.md                   # This file
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/nobel-prize-analysis.git
cd nobel-prize-analysis

# Install dependencies
pip install pandas seaborn numpy matplotlib

# Launch the notebook
jupyter notebook notebook_commented.ipynb
```

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **pandas** — data loading, filtering, groupby aggregations
- **NumPy** — binary flag creation with `np.where`
- **Matplotlib / Seaborn** — visualization

---

## 📄 License

This project is for educational purposes. Nobel Prize data is provided by the [Nobel Prize API](https://www.nobelprize.org/about/developer-zone-2/) under their terms of use.
