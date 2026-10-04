# EduVision DV — Higher Education Performance Analytics
## Comprehensive Technical & Analytical Project Documentation

**Project Name:** EduVision_DV (Higher Education Performance Dashboard)  
**Milestone:** Milestone 4: Documentation and Project Delivery (Weeks 7–8)  
**Technology Stack:** Microsoft Power BI Desktop, Python 3.11, Pandas, OpenPyXL, ReportLab  
**Author:** Antigravity Data & Analytics Team  
**Delivery Date:** October 2026  

---

## 1. Project Background & Strategic Vision

The **EduVision DV** project was commissioned to transform heterogeneous global university performance datasets into an executive-grade Business Intelligence platform. Higher education institutions, government ministries, researchers, and prospective students require an integrated, interactive environment to evaluate academic standing, research velocity, internationalization, and sovereign education capacity.

While the original project specification referenced Tableau workbooks, this deployment has been developed natively in **Microsoft Power BI** pursuant to stakeholder directives ("don't use html use power BI"). The solution delivers a full Power BI project ecosystem (`.pbip`), custom modern dark theme JSON, production DAX measures library, and multi-tab Excel data models.

---

## 2. Dataset Sources & Ingestion Architecture

### 2.1 Primary Data Origins
The analytical engine harmonizes data from two international ranking authorities:
1. **QS World University Rankings (Quacquarelli Symonds):**
   - Focus: Academic Reputation Surveys, Employer Reputation Surveys, Faculty-Student Ratios, Citations per Faculty, and International Faculty/Student Proportions.
2. **Times Higher Education World University Rankings (THE):**
   - Focus: Teaching Environment, Research Environment (Volume, Income, Reputation), Research Quality (Citation Impact, Research Strength, Excellence), Industry Collaboration, and International Outlook.

### 2.2 Data Pipeline Architecture
```text
[Raw Web / API Sources] 
        ↓
[scripts/data_collection.py] ───> data/university_raw_data.csv (7,515 rows across 2020-2024)
        ↓
[scripts/education_cleaning.ipynb] ───> data/university_cleaned.csv (0.00% missing, normalized names)
        ↓
[scripts/generate_education_kpis.py] ───> data/university_final_dataset.xlsx & .csv
        ↓
[Power BI Desktop / PBIP Model] ───> dashboard/EduVision_DV.pbip (4 Integrated Views)
```

### 2.3 Dataset Characteristics
- **Longitudinal Coverage:** 5 consecutive academic evaluation cycles (2020, 2021, 2022, 2023, 2024).
- **Institution Population:** Exactly 1,503 institutions in 2024.
- **Geographic Granularity:** 38 Sovereign Nations categorized into 5 Global Macro-Regions:
  - Europe (37.6% / ~565 institutions)
  - North America (28.3% / ~425 institutions)
  - Asia (24.8% / ~373 institutions)
  - Oceania (6.1% / ~92 institutions)
  - South America (3.2% / ~48 institutions)
- **Academic Disciplines:** 6 major subject branches (All Disciplines, Engineering & Technology, Natural Sciences, Life Sciences & Medicine, Arts & Humanities, Social Sciences & Management).

---

## 3. Education KPI Definitions & Mathematical Methodology

The platform calculates six primary Key Performance Indicators (KPIs) engineered specifically for higher education analytics:

### KPI 1: Global Ranking Score (Composite 0 – 100)
- **Concept:** A harmonized composite score benchmarking overall institutional performance.
- **Formula:**
  $$\text{Global Ranking Score} = 0.40 \times \text{AcadRep} + 0.20 \times \text{EmpRep} + 0.30 \times \text{CitationsFaculty} + 0.05 \times \text{StaffRatioScore} + 0.05 \times \text{IntlStudentPct}$$
- **Interpretation:** Anchored such that the global #1 institution (MIT) attains 100.0, followed by Cambridge (98.7) and Oxford (97.9).

### KPI 2: Research Impact Score (0 – 100)
- **Concept:** Quantifies the intellectual resonance and citation velocity of published research.
- **Formula:**
  $$\text{Research Impact Score} = 0.70 \times \text{CitationsPerFacultyScore} + 0.30 \times \left( \frac{\text{CitationsTotal} / \text{Publications}}{\text{MaxRatio}} \times 100 \right)$$
- **Interpretation:** Disentangles sheer publication volume from high-impact scholarship. Caltech achieves a perfect 100.0 impact score.

### KPI 3: Faculty-to-Student Ratio
- **Concept:** Measures instructional capacity, faculty accessibility, and student mentorship density.
- **Numerical Formula:**
  $$\text{Ratio}_{\text{numeric}} = \frac{\text{Total Student Headcount}}{\text{Total Full-Time Faculty}}$$
- **Display Representation:** Formatted as `"1 : " & FORMAT(Ratio, "0.0")` (e.g. `"1 : 17.3"`).

### KPI 4: International Student Percentage (0 – 100%)
- **Concept:** Indicator of global appeal, student body diversity, and cross-border mobility.
- **Formula:**
  $$\text{Intl Students \%} = \left( \frac{\text{International Enrolled Students}}{\text{Total Enrolled Students}} \right) \times 100$$
- **Interpretation:** Elite UK institutions lead globally (Imperial College at 60.2%, UCL at 53.0%).

### KPI 5: Academic Reputation Score (0 – 100)
- **Concept:** Standardized metric reflecting responses from over 100,000 surveyed academics worldwide.
- **Formula:** Standardized survey z-score transformed to a 0–100 scale.

### KPI 6: Research Productivity Index (10 – 100)
- **Concept:** Efficiency metric measuring publications produced per academic staff member.
- **Formula:**
  $$\text{Raw Productivity} = \frac{\text{Total Indexed Publications}}{\text{Faculty Count}}$$
  $$\text{Productivity Index} = 10 + 90 \times \left( \frac{\text{Raw} - Q_{0.01}}{Q_{0.99} - Q_{0.01}} \right)$$

---

## 4. Power BI Architecture & Dashboard Suite

The Power BI implementation contains four purpose-built analytical views designed with a unified high-contrast dark visual system.

### Page 1: University Overview
- **Objective:** Executive institutional benchmarking and macro performance overview.
- **Header Slicers:** Year (2024), Region (All), Country (All), Subject Area (All Disciplines), Reset Filters button.
- **Top 6 KPI Cards:** Top Global Rank (#1 MIT), Total Universities (1,503), Avg Overall Score (72.6, ▲+2.4%), International Students % (28.7%, ▲+1.8%), Faculty Ratio (1:17.3, ▼-0.6), Total Publications (2.45M, ▲+6.3%).
- **Visuals:**
  1. *Top 10 Universities by Global Ranking:* Detailed rank table with scores and countries.
  2. *Top 10 Universities Overall Score Trend:* Multi-line 5-year evolution chart (2020–2024).
  3. *Universities by Region:* Donut chart visualizing continental distribution.
  4. *Publications by Top 5 Universities:* Horizontal bar chart (Harvard, Stanford, MIT, Oxford, Cambridge).
  5. *International Students % by Region:* Global choropleth map.
  6. *Faculty to Student Ratio by Region:* Clustered column chart.

### Page 2: Research Analytics
- **Objective:** Research output velocity, citation impact, and discipline breakdown.
- **Visuals:**
  1. *Research Impact vs. Publications Volume:* 4-quadrant scatter plot with median benchmark lines.
  2. *Publications Output by Subject Area:* Treemap colored by citations per faculty.
  3. *Top 15 Research Universities:* Horizontal stacked bar chart.
  4. *Research Productivity Trend (2020–2024):* Longitudinal efficiency line chart.

### Page 3: Student Analytics
- **Objective:** Student diversity, international mobility, and teaching capacity.
- **Visuals:**
  1. *International Student Concentration Map:* Bubble map of international destination intensity.
  2. *Faculty-to-Student Ratio Distribution:* Staffing density distribution histogram.
  3. *International Cohort vs Total Enrollment:* Scale vs internationalization scatter plot.
  4. *Student Growth & International % Trend:* Combo column & line tracking post-pandemic recovery.

### Page 4: Country Comparison
- **Objective:** Sovereign higher-education capacity and top-100 density.
- **Visuals:**
  1. *Country Benchmark Matrix:* Heatmap table with conditional data bars across 38 nations.
  2. *Regional Performance Benchmark:* Grouped column chart benchmarking macro-regions.
  3. *Top 100 Concentration by Country:* Treemap visualizing national clustering.
  4. *Country Internationalization vs Impact:* National policy comparison bubble chart.

---

## 5. Technical Deliverables Summary

| File Path | Description | Milestone Module |
| :--- | :--- | :---: |
| `scripts/data_collection.py` | Python ETL script generating raw dataset | Module 1 |
| `data/university_raw_data.csv` | Raw integrated dataset (7,515 rows) | Module 1 |
| `scripts/education_cleaning.ipynb` | Executed Jupyter Notebook for data cleaning | Module 2 |
| `data/university_cleaned.csv` | Cleaned, deduplicated, standardized dataset | Module 2 |
| `scripts/generate_education_kpis.py` | KPI calculation & export script | Module 3 |
| `data/university_final_dataset.xlsx` | Multi-tab Excel workbook with dictionary | Module 3 |
| `data/university_final_dataset.csv` | Analytics-ready CSV dataset | Module 3 |
| `docs/dashboard_storyboard.pdf` | Publication-grade 6-page PDF blueprint | Module 4 |
| `dashboard/EduVision_DV.pbip` | Native Power BI Project launcher | Modules 5 & 6 |
| `dashboard/EduVision_DV.SemanticModel/model.bim` | Power BI Tabular Model TMSL schema | Modules 5 & 6 |
| `dashboard/EduVision_DV.Report/report.json` | Power BI visual report layout | Modules 5 & 6 |
| `dashboard/EduVision_Theme.json` | High-contrast modern dark UI theme | Modules 5 & 6 |
| `dashboard/DAX_Measures.dax` | Production DAX measure repository | Modules 5 & 6 |
| `dashboard/PowerQuery_Transformations.m` | Complete Power Query M code | Modules 5 & 6 |
| `dashboard/PowerBI_Dashboard_Guide.md` | Field-by-field Power BI build manual | Modules 5 & 6 |
| `scripts/run_quality_assurance_tests.py` | Automated testing suite (15 tests) | Module 7 |
| `docs/QA_Checklist.md` | Comprehensive QA verification checklist | Module 7 |
| `docs/Dashboard_Testing_Report.md` | Test execution report (100% pass) | Module 7 |
| `docs/Final_Documentation.md` | Complete methodology & architecture doc | Module 8 |
| `README.md` | Project master index and quick-start guide | Module 8 |
