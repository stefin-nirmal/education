# EduVision DV — Power BI Dashboard Development & Implementation Guide

## Executive Overview
This guide provides the complete, field-by-field implementation protocol for the **EduVision DV (Higher Education Performance Analytics)** dashboard suite inside **Microsoft Power BI Desktop**. 

The project delivers four interconnected dashboards matching the dark theme layout specification:
1. **University Overview**
2. **Research Analytics**
3. **Student Analytics**
4. **Country Comparison**

---

## 1. Quick Launch Options

### Option A: Launching via Power BI Project (`.pbip`) — Recommended
1. Locate the file: `dashboard/EduVision_DV.pbip`.
2. Double-click the file (or open Microsoft Power BI Desktop -> **File** -> **Open Report** -> select `dashboard/EduVision_DV.pbip`).
3. Power BI Desktop will automatically load the Tabular Semantic Model (`EduVision_DV.SemanticModel/model.bim`), ingest the 7,515 records from `data/university_final_dataset.csv`, instantiate the data model, and wire all 18 core DAX measures into the field pane.

### Option B: Building from Scratch via Excel & Power Query
If importing into an existing `.pbix` session:
1. In Power BI Desktop, click **Get Data** -> **Excel Workbook** -> select `data/university_final_dataset.xlsx`.
2. Select sheets:
   - `University_Performance` (Fact Table)
   - `Regional_Benchmarks` (Dimension Table)
   - `Country_Benchmarks` (Dimension Table)
3. Open **Transform Data** -> **Advanced Editor** and paste the transformations from `dashboard/PowerQuery_Transformations.m`.
4. Click **Close & Apply**.
5. In **View** tab -> **Themes** -> **Browse for themes** -> select `dashboard/EduVision_Theme.json`.

---

## 2. Global Canvas & Theme Configuration

- **Canvas Size:** 16:9 Widescreen (1280 × 720 px or 1920 × 1080 px).
- **Page Background:** `#0B0E1B` (100% Opacity, Fit: Normal).
- **Container Card Background:** `#1B1F38` with border `#282F54` and corner radius `8px`.
- **Primary Text:** `#FFFFFF` (Segoe UI / Segoe UI Semibold).
- **Secondary Text / Subtitles:** `#94A3B8`.
- **Theme Palette Tokens:**
  - Accent Violet: `#7C5CFC`
  - Azure Blue: `#3B82F6`
  - Teal/Cyan: `#06B6D4`
  - Emerald Green: `#10B981`
  - Amber Orange: `#F59E0B`
  - Rose/Magenta: `#EC4899`

---

## 3. Global Header, Navigation Rail & Slicers

### Header Strip (Top `Y: 0`, `Height: 65px`, `Width: 1280px`)
- **Logo / Brand:** Text box: `"EduVision DV"` (`16pt Bold #FFFFFF`), subtitle `"Higher Education Performance Dashboard"` (`9pt #94A3B8`).
- **Icons:** Home, Analytics, About SVG buttons on the top right.

### Global Slicers (Top Ribbon or Left Rail)
- **Year Slicer:**
  - Visual: Dropdown / Single Select
  - Field: `University_Performance[year]`
  - Default Value: `2024`
- **Region Slicer:**
  - Visual: Dropdown
  - Field: `University_Performance[region]`
  - Default: `(All)`
- **Country Slicer:**
  - Visual: Dropdown
  - Field: `University_Performance[country]`
  - Default: `(All)`
- **Subject Area Slicer:**
  - Visual: Dropdown
  - Field: `University_Performance[subject_area]`
  - Default: `All Disciplines`
- **Reset Filters Button:**
  - Action: Bookmark -> `"Reset_All_Filters"` (Restores slicers to 2024 All).

### Left Navigation Bar (`Width: 140px`)
Four button controls with Action: **Page Navigation**:
1. `Overview` (Navigate to Page 1: University Overview)
2. `Research Analytics` (Navigate to Page 2: Research Analytics)
3. `Student Analytics` (Navigate to Page 3: Student Analytics)
4. `Country Comparison` (Navigate to Page 4: Country Comparison)

---

## 4. Page 1: University Overview

### Top KPI Banner (6 Multi-Row / Card Visuals across `Y: 75`, `Height: 80px`)
1. **Top Global Ranking:**
   - Visual: Card
   - Fields: Measure `[Top Global Ranking Display]`
   - Display: `#1 Massachusetts Institute of Technology (USA)`
2. **Total Universities:**
   - Visual: Card
   - Fields: Measure `[Total Universities Display]`
   - Display: `1,503 Ranked Universities`
3. **Avg Overall Score:**
   - Visual: Card with Callout Value
   - Main Value: Measure `[Avg Overall Score]` (`72.6`)
   - Sub-label: Measure `[Score YoY Display]` (`▲ +2.4% vs 2023`, Font Color: `#10B981`)
4. **International Students %:**
   - Visual: Card
   - Main Value: Measure `[Avg International Students Pct Display]` (`28.7%`)
   - Sub-label: Measure `[Intl Students YoY Display]` (`▲ +1.8% vs 2023`, Font Color: `#10B981`)
5. **Faculty Ratio:**
   - Visual: Card
   - Main Value: Measure `[Faculty to Student Ratio Display]` (`1 : 17.3`)
   - Sub-label: Measure `[Faculty Ratio YoY Display]` (`▼ -0.6 vs 2023`, Font Color: `#EF4444`)
6. **Total Publications:**
   - Visual: Card
   - Main Value: Measure `[Total Publications Display]` (`2.45M`)
   - Sub-label: Measure `[Publications YoY Display]` (`▲ +6.3% vs 2023`, Font Color: `#10B981`)

### Grid Visuals (6 Visuals)
1. **Top 10 Universities by Global Ranking:**
   - **Type:** Table (`tableEx`)
   - **Values:** `global_rank`, `university_name`, `country`, `kpi_global_ranking_score`
   - **Filter:** Top N -> by `global_rank` Top 10
   - **Formatting:** Alternating row colors (`#1B1F38` / `#161A30`), font color `#FFFFFF`.
2. **Top 10 Universities by Overall Score Trend:**
   - **Type:** Line Chart (`lineChart`)
   - **X-Axis:** `year` (Categorical: 2020, 2021, 2022, 2023, 2024)
   - **Y-Axis:** `AVERAGE(kpi_global_ranking_score)` (Min: 80, Max: 100)
   - **Legend:** `university_name` (Filtered to Top 5: MIT, Cambridge, Oxford, Harvard, Stanford)
   - **Line Colors:** `#7C5CFC`, `#3B82F6`, `#06B6D4`, `#EC4899`, `#F59E0B`.
3. **Universities by Region:**
   - **Type:** Donut Chart (`donutChart`)
   - **Legend:** `region`
   - **Values:** `COUNT(university_name)`
   - **Center KPI Label:** `1,503 Total`
   - **Data Colors:** Europe (`#7C5CFC`), North America (`#3B82F6`), Asia (`#06B6D4`), Oceania (`#10B981`), South America (`#F59E0B`).
4. **Publications by Top 5 Universities:**
   - **Type:** Clustered Bar Chart (`clusteredBarChart` - Horizontal)
   - **Y-Axis:** `university_name`
   - **X-Axis:** `SUM(publications_count)`
   - **Filter:** Top N -> Top 5 by Publications
   - **Bar Color:** `#7C5CFC` gradient.
5. **International Students % by Region:**
   - **Type:** Filled Map / Shape Map (`shapeMap` / `map`)
   - **Location:** `region` / `country`
   - **Color Saturation:** Measure `[Avg International Students Pct]` (Gradient from `#1E293B` to `#F59E0B`).
6. **Faculty to Student Ratio by Region:**
   - **Type:** Clustered Column Chart (`clusteredColumnChart`)
   - **X-Axis:** `region`
   - **Y-Axis:** `AVERAGE(faculty_to_student_ratio_numeric)`
   - **Data Labels:** ON (`1:25.0`, `1:21.4`, `1:18.7`, `1:16.2`, `1:14.3`).
   - **Color:** `#3B82F6`.

---

## 5. Page 2: Research Analytics

### Research Visuals
1. **Research Impact vs. Publications Volume (Scatter Chart):**
   - **X-Axis:** `SUM(publications_count)` (Linear, 0 - 250K)
   - **Y-Axis:** `AVERAGE(kpi_research_impact_score)` (0 - 100)
   - **Size:** `SUM(faculty_count)`
   - **Legend:** `region`
   - **Details:** `university_name`
   - **Analytics Lines:** X-Axis Median Reference Line, Y-Axis Median Reference Line (Creates 4 Performance Quadrants).
2. **Publications Output by Subject Area (Treemap):**
   - **Category:** `subject_area`
   - **Values:** `SUM(publications_count)`
   - **Color Saturation:** `AVERAGE(citations_per_faculty_score)`
3. **Top 15 Research Universities (Horizontal Stacked Bar Chart):**
   - **Y-Axis:** `university_name`
   - **X-Axis:** `SUM(publications_count)`
   - **Legend:** `rank_tier`
4. **Research Productivity Index Trend (Line Chart):**
   - **X-Axis:** `year`
   - **Y-Axis:** `AVERAGE(kpi_research_productivity_index)`
   - **Legend:** `region`

---

## 6. Page 3: Student Analytics

### Student Visuals
1. **International Student Concentration Map:**
   - **Location:** `country`
   - **Size:** `SUM(international_student_count)`
   - **Color Saturation:** `AVERAGE(kpi_international_student_pct)`
2. **Faculty-to-Student Ratio Distribution (Clustered Column):**
   - **X-Axis:** Binned Ratio (`1-10`, `11-20`, `21-30`, `31+`)
   - **Y-Axis:** `COUNT(university_name)`
   - **Color:** `#06B6D4`
3. **International Student Cohort vs Total Enrollment (Scatter):**
   - **X-Axis:** `SUM(student_count)`
   - **Y-Axis:** `AVERAGE(kpi_international_student_pct)`
   - **Size:** `SUM(faculty_count)`
   - **Legend:** `region`
4. **Student Enrollment & Internationalization Trend (Line & Clustered Column):**
   - **Shared X-Axis:** `year`
   - **Column Y-Axis:** `SUM(student_count)` (Total Headcount)
   - **Line Y-Axis:** `AVERAGE(kpi_international_student_pct)`

---

## 7. Page 4: Country Comparison

### Country Visuals
1. **Country Benchmark Heatmap Matrix:**
   - **Rows:** `country`
   - **Columns / Values:**
     - `Count of Universities`
     - `Top 100 Count`
     - `Avg Overall Score` (with background color conditional formatting)
     - `Avg Intl %` (with data bars)
     - `Avg Faculty-Student Ratio`
2. **Regional Performance Multi-Metric Comparison (Grouped Bar):**
   - **Y-Axis:** `region`
   - **X-Axis:** Values: `[Avg Overall Score]`, `[Avg Research Impact Score]`, `[Avg International Students Pct]`
3. **Top 100 Concentration by Sovereign Nation (Treemap):**
   - **Group:** `country`
   - **Values:** Measure `[Top 100 Universities Count]`
4. **Country-Level Internationalization vs Research Impact (Scatter):**
   - **X-Axis:** `AVERAGE(kpi_international_student_pct)`
   - **Y-Axis:** `AVERAGE(kpi_research_impact_score)`
   - **Details:** `country`
   - **Size:** `COUNT(university_name)`

---

## 8. Slicer Synchronization & Interactive Behavior Matrix

| Slicer Name | Field Name | Overview Page | Research Analytics | Student Analytics | Country Comparison |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Year** | `University_Performance[year]` | **Visible / Synced** | **Visible / Synced** | **Visible / Synced** | **Visible / Synced** |
| **Region** | `University_Performance[region]` | **Visible / Synced** | **Visible / Synced** | **Visible / Synced** | **Visible / Synced** |
| **Country** | `University_Performance[country]` | **Visible / Synced** | **Visible / Synced** | **Visible / Synced** | **Visible / Synced** |
| **Subject Area** | `University_Performance[subject_area]`| **Visible / Synced** | **Visible / Synced** | **Visible / Synced** | **Visible / Synced** |

### Interaction Settings
- **Edit Interactions:** All visuals set to **Cross-highlight** or **Filter**.
- **Page Tooltips:** Configured with dynamic tooltips displaying institutional profile cards on hover.
