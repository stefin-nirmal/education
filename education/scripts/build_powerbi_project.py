"""
Script to generate the complete Power BI Project (.pbip) folder structure:
- dashboard/EduVision_DV.pbip
- dashboard/EduVision_DV.Report/definition.pbir
- dashboard/EduVision_DV.Report/report.json
- dashboard/EduVision_DV.SemanticModel/definition.pbism
- dashboard/EduVision_DV.SemanticModel/model.bim
"""

import os
import json

base_dir = "dashboard"
pbip_path = os.path.join(base_dir, "EduVision_DV.pbip")
report_dir = os.path.join(base_dir, "EduVision_DV.Report")
model_dir = os.path.join(base_dir, "EduVision_DV.SemanticModel")

os.makedirs(report_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)

# 1. EduVision_DV.pbip
pbip_content = {
    "version": "1.0",
    "artifacts": [
        {
            "report": {
                "path": "EduVision_DV.Report"
            }
        }
    ]
}

with open(pbip_path, "w", encoding="utf-8") as f:
    json.dump(pbip_content, f, indent=2)

# 2. definition.pbir
pbir_content = {
    "version": "1.0",
    "datasetReference": {
        "byPath": {
            "path": "../EduVision_DV.SemanticModel"
        },
        "byConnection": None
    }
}

with open(os.path.join(report_dir, "definition.pbir"), "w", encoding="utf-8") as f:
    json.dump(pbir_content, f, indent=2)

# 3. definition.pbism
pbism_content = {
    "version": "1.0"
}

with open(os.path.join(model_dir, "definition.pbism"), "w", encoding="utf-8") as f:
    json.dump(pbism_content, f, indent=2)

# 4. model.bim (Tabular Model Schema)
# Escape backslashes for path in M expression
csv_path = os.path.abspath("data/university_final_dataset.csv").replace("\\", "\\\\")

model_bim = {
    "name": "EduVision_DV_Model",
    "compatibilityLevel": 1550,
    "model": {
        "culture": "en-US",
        "dataAccessOptions": {
            "legacyRedirects": True,
            "returnErrorValuesAsNull": True
        },
        "defaultPowerBIDataSourceVersion": "powerBI_V3",
        "tables": [
            {
                "name": "University_Performance",
                "columns": [
                    {"name": "global_rank", "dataType": "int64", "sourceColumn": "global_rank"},
                    {"name": "university_name", "dataType": "string", "sourceColumn": "university_name"},
                    {"name": "country", "dataType": "string", "sourceColumn": "country"},
                    {"name": "region", "dataType": "string", "sourceColumn": "region"},
                    {"name": "year", "dataType": "int64", "sourceColumn": "year"},
                    {"name": "subject_area", "dataType": "string", "sourceColumn": "subject_area"},
                    {"name": "overall_score_qs", "dataType": "double", "sourceColumn": "overall_score_qs"},
                    {"name": "overall_score_the", "dataType": "double", "sourceColumn": "overall_score_the"},
                    {"name": "overall_score_harmonized", "dataType": "double", "sourceColumn": "overall_score_harmonized"},
                    {"name": "academic_reputation_score", "dataType": "double", "sourceColumn": "academic_reputation_score"},
                    {"name": "employer_reputation_score", "dataType": "double", "sourceColumn": "employer_reputation_score"},
                    {"name": "citations_per_faculty_score", "dataType": "double", "sourceColumn": "citations_per_faculty_score"},
                    {"name": "faculty_count", "dataType": "int64", "sourceColumn": "faculty_count"},
                    {"name": "student_count", "dataType": "int64", "sourceColumn": "student_count"},
                    {"name": "international_students_pct", "dataType": "double", "sourceColumn": "international_students_pct"},
                    {"name": "publications_count", "dataType": "int64", "sourceColumn": "publications_count"},
                    {"name": "citations_total", "dataType": "int64", "sourceColumn": "citations_total"},
                    {"name": "industry_income_score", "dataType": "double", "sourceColumn": "industry_income_score"},
                    {"name": "kpi_global_ranking_score", "dataType": "double", "sourceColumn": "kpi_global_ranking_score"},
                    {"name": "kpi_research_impact_score", "dataType": "double", "sourceColumn": "kpi_research_impact_score"},
                    {"name": "faculty_to_student_ratio_numeric", "dataType": "double", "sourceColumn": "faculty_to_student_ratio_numeric"},
                    {"name": "kpi_faculty_student_ratio_display", "dataType": "string", "sourceColumn": "kpi_faculty_student_ratio_display"},
                    {"name": "kpi_international_student_pct", "dataType": "double", "sourceColumn": "kpi_international_student_pct"},
                    {"name": "international_student_count", "dataType": "int64", "sourceColumn": "international_student_count"},
                    {"name": "kpi_academic_reputation_score", "dataType": "double", "sourceColumn": "kpi_academic_reputation_score"},
                    {"name": "kpi_research_productivity_index", "dataType": "double", "sourceColumn": "kpi_research_productivity_index"},
                    {"name": "rank_tier", "dataType": "string", "sourceColumn": "rank_tier"},
                    {"name": "yoy_score_change", "dataType": "double", "sourceColumn": "yoy_score_change"},
                    {"name": "yoy_score_pct_change", "dataType": "double", "sourceColumn": "yoy_score_pct_change"},
                    {"name": "yoy_intl_pct_change", "dataType": "double", "sourceColumn": "yoy_intl_pct_change"},
                    {"name": "yoy_ratio_change", "dataType": "double", "sourceColumn": "yoy_ratio_change"},
                    {"name": "yoy_pubs_pct_change", "dataType": "double", "sourceColumn": "yoy_pubs_pct_change"}
                ],
                "partitions": [
                    {
                        "name": "University_Performance_Partition",
                        "mode": "import",
                        "source": {
                            "type": "m",
                            "expression": [
                                f'let Source = Csv.Document(File.Contents("{csv_path}"),[Delimiter=",", Columns=42, Encoding=65001, QuoteStyle=QuoteStyle.None]),',
                                '    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),',
                                '    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{',
                                '        {"global_rank", Int64.Type}, {"university_name", type text}, {"country", type text}, {"region", type text},',
                                '        {"year", Int64.Type}, {"subject_area", type text}, {"overall_score_qs", type number}, {"overall_score_the", type number},',
                                '        {"overall_score_harmonized", type number}, {"academic_reputation_score", type number}, {"employer_reputation_score", type number},',
                                '        {"citations_per_faculty_score", type number}, {"faculty_count", Int64.Type}, {"student_count", Int64.Type},',
                                '        {"international_students_pct", type number}, {"publications_count", Int64.Type}, {"citations_total", Int64.Type},',
                                '        {"industry_income_score", type number}, {"kpi_global_ranking_score", type number}, {"kpi_research_impact_score", type number},',
                                '        {"faculty_to_student_ratio_numeric", type number}, {"kpi_faculty_student_ratio_display", type text},',
                                '        {"kpi_international_student_pct", type number}, {"international_student_count", Int64.Type},',
                                '        {"kpi_academic_reputation_score", type number}, {"kpi_research_productivity_index", type number}, {"rank_tier", type text},',
                                '        {"yoy_score_change", type number}, {"yoy_score_pct_change", type number}, {"yoy_intl_pct_change", type number},',
                                '        {"yoy_ratio_change", type number}, {"yoy_pubs_pct_change", type number}',
                                '    })',
                                'in #"Changed Type"'
                            ]
                        }
                    }
                ]
            },
            {
                "name": "_DAX_Measures",
                "columns": [
                    {
                        "name": "Placeholder",
                        "dataType": "string",
                        "isHidden": True,
                        "sourceColumn": "Placeholder"
                    }
                ],
                "partitions": [
                    {
                        "name": "_DAX_Measures_Partition",
                        "mode": "import",
                        "source": {
                            "type": "m",
                            "expression": [
                                'let Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Placeholder = _t]) in Source'
                            ]
                        }
                    }
                ],
                "measures": [
                    {
                        "name": "Total Universities",
                        "expression": "DISTINCTCOUNT(University_Performance[university_name])",
                        "formatString": "#,##0"
                    },
                    {
                        "name": "Total Universities Display",
                        "expression": "FORMAT([Total Universities], \"#,##0\") & \" Ranked Universities\""
                    },
                    {
                        "name": "Avg Overall Score",
                        "expression": "ROUND(AVERAGE(University_Performance[kpi_global_ranking_score]), 1)",
                        "formatString": "0.0"
                    },
                    {
                        "name": "Avg International Students Pct",
                        "expression": "ROUND(AVERAGE(University_Performance[kpi_international_student_pct]), 1)",
                        "formatString": "0.0"
                    },
                    {
                        "name": "Avg International Students Pct Display",
                        "expression": "FORMAT([Avg International Students Pct] / 100, \"0.0%\")"
                    },
                    {
                        "name": "Faculty to Student Ratio Numeric",
                        "expression": "ROUND(AVERAGE(University_Performance[faculty_to_student_ratio_numeric]), 1)",
                        "formatString": "0.0"
                    },
                    {
                        "name": "Faculty to Student Ratio Display",
                        "expression": "\"1 : \" & FORMAT([Faculty to Student Ratio Numeric], \"0.0\")"
                    },
                    {
                        "name": "Total Publications",
                        "expression": "SUM(University_Performance[publications_count])",
                        "formatString": "#,##0"
                    },
                    {
                        "name": "Total Publications Display",
                        "expression": "VAR PubCount = [Total Publications] RETURN IF(PubCount >= 1000000, FORMAT(PubCount / 1000000, \"0.00\") & \"M\", IF(PubCount >= 1000, FORMAT(PubCount / 1000, \"0\") & \"K\", FORMAT(PubCount, \"#,##0\")))"
                    },
                    {
                        "name": "Top Ranked Institution",
                        "expression": "CALCULATE(FIRSTNONBLANK(University_Performance[university_name], 1), FILTER(University_Performance, University_Performance[global_rank] = 1))"
                    },
                    {
                        "name": "Top Global Ranking Display",
                        "expression": "\"#1 \" & [Top Ranked Institution]"
                    },
                    {
                        "name": "Total Citations",
                        "expression": "SUM(University_Performance[citations_total])",
                        "formatString": "#,##0"
                    },
                    {
                        "name": "Total Citations Display",
                        "expression": "VAR CitCount = [Total Citations] RETURN IF(CitCount >= 1000000, FORMAT(CitCount / 1000000, \"0.00\") & \"M\", FORMAT(CitCount / 1000, \"0.0\") & \"K\")"
                    },
                    {
                        "name": "Avg Research Impact Score",
                        "expression": "ROUND(AVERAGE(University_Performance[kpi_research_impact_score]), 1)",
                        "formatString": "0.0"
                    },
                    {
                        "name": "Avg Academic Reputation Score",
                        "expression": "ROUND(AVERAGE(University_Performance[kpi_academic_reputation_score]), 1)",
                        "formatString": "0.0"
                    },
                    {
                        "name": "Avg Research Productivity Index",
                        "expression": "ROUND(AVERAGE(University_Performance[kpi_research_productivity_index]), 1)",
                        "formatString": "0.0"
                    },
                    {
                        "name": "Total Students",
                        "expression": "SUM(University_Performance[student_count])",
                        "formatString": "#,##0"
                    },
                    {
                        "name": "Total International Students",
                        "expression": "SUM(University_Performance[international_student_count])",
                        "formatString": "#,##0"
                    }
                ]
            }
        ]
    }
}

with open(os.path.join(model_dir, "model.bim"), "w", encoding="utf-8") as f:
    json.dump(model_bim, f, indent=2)

# 5. report.json
# Load theme config
with open("dashboard/EduVision_Theme.json", "r", encoding="utf-8") as f:
    theme_obj = json.load(f)

report_json = {
    "config": json.dumps({
        "version": "5.50",
        "themeCollection": {
            "baseTheme": {
                "name": "EduVision Modern Dark",
                "version": "1.0",
                "type": 2
            }
        }
    }),
    "layoutOptimization": 0,
    "sections": [
        {
            "name": "ReportSectionOverview",
            "displayName": "University Overview",
            "filters": "[]",
            "ordinal": 0,
            "width": 1280,
            "height": 720,
            "config": json.dumps({}),
            "visualContainers": []
        },
        {
            "name": "ReportSectionResearch",
            "displayName": "Research Analytics",
            "filters": "[]",
            "ordinal": 1,
            "width": 1280,
            "height": 720,
            "config": json.dumps({}),
            "visualContainers": []
        },
        {
            "name": "ReportSectionStudent",
            "displayName": "Student Analytics",
            "filters": "[]",
            "ordinal": 2,
            "width": 1280,
            "height": 720,
            "config": json.dumps({}),
            "visualContainers": []
        },
        {
            "name": "ReportSectionCountry",
            "displayName": "Country Comparison",
            "filters": "[]",
            "ordinal": 3,
            "width": 1280,
            "height": 720,
            "config": json.dumps({}),
            "visualContainers": []
        }
    ]
}

with open(os.path.join(report_dir, "report.json"), "w", encoding="utf-8") as f:
    json.dump(report_json, f, indent=2)

print("Successfully constructed Power BI Project (.pbip) in dashboard/EduVision_DV.pbip")
