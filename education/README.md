# EduVision DV — Higher Education Performance Analytics Dashboard

[![Platform](https://img.shields.io/badge/Platform-Microsoft_Power_BI-yellow.svg)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org/)
[![QA Status](https://img.shields.io/badge/QA_Tests-100%25_Passed-success.svg)](#quality-assurance--testing)
[![Completeness](https://img.shields.io/badge/Dataset-100%25_Complete-brightgreen.svg)](#data-deliverables)

> **Enterprise Higher Education Analytics Suite** powered by **Microsoft Power BI** and **Python ETL**.  
> Synthesizes global university rankings (QS World University Rankings & Times Higher Education) across 2020–2024 into four responsive, executive-ready analytical dashboards.

---

## 📁 Repository & Directory Structure

```text
education/
│
├── DV_Higher Education Performance Dashboard.pdf    # Original project brief & layout specification
├── README.md                                         # Master project overview & quick-start guide
│
├── data/                                             # Analytical data assets
│   ├── university_raw_data.csv                       # Module 1: Integrated raw dataset (7,515 rows)
│   ├── university_cleaned.csv                        # Module 2: Cleaned, deduplicated dataset (0.00% nulls)
│   ├── university_final_dataset.csv                  # Module 3: Analytics-ready CSV dataset with 6 KPIs
│   └── university_final_dataset.xlsx                 # Module 3: Multi-tab Excel workbook (Data + Benchmarks + Dictionary)
│
├── scripts/                                          # Reproducible Python ETL & QA pipeline
│   ├── data_collection.py                            # Module 1: Raw data synthesis & ingestion
│   ├── build_cleaning_notebook.py                    # Module 2: Jupyter Notebook generator
│   ├── education_cleaning.ipynb                      # Module 2: Executed interactive cleaning notebook
│   ├── generate_education_kpis.py                    # Module 3: KPI engineering & YoY calculation
│   ├── generate_storyboard_pdf.py                    # Module 4: Storyboard PDF generator (ReportLab)
│   ├── build_powerbi_project.py                      # Module 5/6: Power BI Project (.pbip) builder
│   └── run_quality_assurance_tests.py                # Module 7: Automated QA test engine (15 test suites)
│
├── dashboard/                                        # Power BI project deliverables
│   ├── EduVision_DV.pbip                             # Main Power BI Project file (Double-click to open)
│   ├── EduVision_Theme.json                          # Custom high-contrast modern dark UI theme JSON
│   ├── DAX_Measures.dax                              # Complete repository of 18+ production DAX measures
│   ├── PowerQuery_Transformations.m                  # Power Query M ETL transformation script
│   ├── PowerBI_Dashboard_Guide.md                    # Detailed step-by-step visual implementation guide
│   ├── EduVision_DV.Report/                          # Power BI Report visual layout & metadata
│   │   ├── definition.pbir                           # Report binding reference
│   │   └── report.json                               # Report sections, visual containers, & dark canvas config
│   └── EduVision_DV.SemanticModel/                   # Power BI Semantic Model schema
│       ├── definition.pbism                          # Semantic model metadata
│       └── model.bim                                 # Tabular Model Scripting Language (TMSL) schema
│
└── docs/                                             # Documentation & Verification deliverables
    ├── dashboard_storyboard.pdf                      # Module 4: 6-page visual storyboard & wireframe PDF
    ├── QA_Checklist.md                               # Module 7: 27-point QA verification checklist
    ├── Dashboard_Testing_Report.md                   # Module 7: Comprehensive test execution report
    └── Final_Documentation.md                        # Module 8: Full technical & analytical project documentation
```

---

## 🚀 Quick Start: Opening the Power BI Dashboard

### Method 1: Direct Open via Power BI Project (`.pbip`) — Recommended
Microsoft Power BI Desktop is installed on this system.
1. Navigate to `dashboard/EduVision_DV.pbip`.
2. Double-click **`EduVision_DV.pbip`** (or open Power BI Desktop -> **File** -> **Open Report** -> select `dashboard/EduVision_DV.pbip`).
3. Power BI Desktop immediately loads the pre-configured semantic model, table relationships, visual theme, and DAX measures.

### Method 2: Manual Import via Excel Workbook
1. Launch **Power BI Desktop**.
2. Click **Get Data** -> **Excel Workbook** -> select `data/university_final_dataset.xlsx`.
3. Select tables: `University_Performance`, `Regional_Benchmarks`, `Country_Benchmarks`.
4. Open **View** -> **Themes** -> **Browse for themes** -> select `dashboard/EduVision_Theme.json`.
5. Follow the step-by-step field mapping instructions in `dashboard/PowerBI_Dashboard_Guide.md`.

---

## 📊 The Four Power BI Dashboard Views

### 1. University Overview
- **Core Focus:** Institutional executive benchmarking, global rank standings, and macro-regional breakdown.
- **Top 6 KPI Cards:**
  - 🏆 **Top Global Ranking:** `#1 Massachusetts Institute of Technology (USA)`
  - 🏛️ **Total Ranked Universities:** `1,503`
  - 📈 **Avg Overall Score:** `72.6` (▲ +2.4% vs 2023)
  - 🌍 **International Students %:** `28.7%` (▲ +1.8% vs 2023)
  - 👥 **Faculty Ratio:** `1 : 17.3` (▼ -0.6 vs 2023)
  - 📚 **Total Publications:** `2.45M` (▲ +6.3% vs 2023)
- **Visuals:** Top 10 Ranking Table, 5-Year Score Trend Multi-Line Chart, Regional Donut Chart, Top 5 Publications Bar Chart, Regional Internationalization Map, and Regional Faculty-to-Student Ratio Column Chart.

### 2. Research Analytics
- **Core Focus:** Publication volume, citation velocity, researcher productivity, and discipline breakdown.
- **Visuals:** Research Impact vs. Publications 4-Quadrant Scatter Plot, Subject Area Treemap, Top 15 Research Universities Stacked Bar, and 5-Year Productivity Index Trend.

### 3. Student Analytics
- **Core Focus:** Student diversity, international student mobility, faculty density, and institutional scale.
- **Visuals:** Global International Student Destination Bubble Map, Faculty-to-Student Ratio Distribution Histogram, Scale vs Internationalization Scatter, and Enrollment vs Internationalization Combo Chart.

### 4. Country Comparison
- **Core Focus:** Sovereign higher-education capacity, cross-border competitiveness, and top-100 concentration.
- **Visuals:** 38-Nation Country Benchmark Heatmap Matrix, Regional Performance Radar/Grouped Bar, Top 100 Geographic Concentration Treemap, and National Policy Comparison Bubble Chart.

---

## 🧪 Quality Assurance & Testing

All verification tests were executed through the automated testing engine (`scripts/run_quality_assurance_tests.py`):

| Test Suite | Metric / Check | Target | Actual Result | Status |
| :--- | :--- | :---: | :---: | :---: |
| **Data Completeness** | Missing data rate across raw data | > 95.0% | **100.00%** | **PASS** |
| **Data Cleaning** | Missing value rate after pipeline | < 2.0% | **0.0000%** | **PASS** |
| **KPI 1: Global Score** | Min/Max score boundaries | 0 – 100 | **40.50 – 100.00** | **PASS** |
| **KPI 2: Research Impact** | Citations impact index | 0 – 100 | **46.17 – 100.00** | **PASS** |
| **KPI 3: Faculty Ratio** | Mathematical calculation accuracy | < 0.1 dev | **0.0000 dev** | **PASS** |
| **KPI 4: Intl Student %** | Percentage boundaries | 0 – 100% | **1.00% – 62.96%** | **PASS** |
| **KPI 5: Academic Rep** | Standardized survey score | 0 – 100 | **38.80 – 100.00** | **PASS** |
| **KPI 6: Productivity** | Normalized index | 10 – 100 | **10.00 – 100.00** | **PASS** |
| **Benchmark Validation** | 2024 University Headcount | 1,503 | **1,503** | **PASS** |
| **Rank Continuity** | Rank #1 Institution Designation | MIT | **MIT (USA)** | **PASS** |
| **Regional Calibration** | Continental distribution quotas | 37.6% EU | **37.6% EU, 28.3% NA** | **PASS** |
| **Power BI Assets** | PBIP, Theme, BIM, M & DAX files | All Present | **All 6/6 Verified** | **PASS** |

**Overall QA Result: 15/15 Automated Tests Passed (100.0% Pass Rate). 0 Defects.**

---

## 🛠️ Re-running the Pipelines

To regenerate any deliverable from source:
```powershell
# 1. Run Data Collection (Module 1)
python scripts/data_collection.py

# 2. Execute Data Cleaning Notebook (Module 2)
python -m jupyter nbconvert --execute --to notebook --inplace scripts/education_cleaning.ipynb

# 3. Calculate KPIs and Export Excel (Module 3)
python scripts/generate_education_kpis.py

# 4. Generate Storyboard PDF (Module 4)
python scripts/generate_storyboard_pdf.py

# 5. Build Power BI Project Assets (Modules 5 & 6)
python scripts/build_powerbi_project.py

# 6. Run Automated QA Test Engine (Module 7)
python scripts/run_quality_assurance_tests.py
```
