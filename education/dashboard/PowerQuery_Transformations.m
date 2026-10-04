// ==============================================================================
// EduVision DV - Power Query (M) Transformation Scripts
// Author: Antigravity Team
// Architecture: Higher Education Performance Analytics
// Usage: Copy and paste into Power BI Desktop > Transform Data > Advanced Editor
// ==============================================================================

// ------------------------------------------------------------------------------
// Query 1: University_Performance (Primary Fact Table)
// ------------------------------------------------------------------------------
let
    // Dynamically locate the data file relative to workspace or provide absolute fallback
    SourcePath = "c:\Users\stefi\Desktop\education\data\university_final_dataset.xlsx",
    Source = Excel.Workbook(File.Contents(SourcePath), null, true),
    University_Sheet = Source{[Item="University_Performance",Kind="Sheet"]}[Data],
    PromotedHeaders = Table.PromoteHeaders(University_Sheet, [PromoteAllScalars=true]),
    
    // Explicit Type Conversions
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders,{
        {"global_rank", Int64.Type},
        {"university_name", type text},
        {"country", type text},
        {"region", type text},
        {"year", Int64.Type},
        {"subject_area", type text},
        {"overall_score_qs", type number},
        {"overall_score_the", type number},
        {"overall_score_harmonized", type number},
        {"academic_reputation_score", type number},
        {"employer_reputation_score", type number},
        {"citations_per_faculty_score", type number},
        {"faculty_count", Int64.Type},
        {"student_count", Int64.Type},
        {"international_students_pct", type number},
        {"publications_count", Int64.Type},
        {"citations_total", Int64.Type},
        {"industry_income_score", type number},
        {"kpi_global_ranking_score", type number},
        {"kpi_research_impact_score", type number},
        {"faculty_to_student_ratio_numeric", type number},
        {"kpi_faculty_student_ratio_display", type text},
        {"kpi_international_student_pct", type number},
        {"international_student_count", Int64.Type},
        {"kpi_academic_reputation_score", type number},
        {"kpi_research_productivity_index", type number},
        {"rank_tier", type text},
        {"yoy_score_change", type number},
        {"yoy_score_pct_change", type number},
        {"yoy_intl_pct_change", type number},
        {"yoy_ratio_change", type number},
        {"yoy_pubs_pct_change", type number}
    })
in
    ChangedTypes

// ------------------------------------------------------------------------------
// Query 2: Regional_Benchmarks (Dimension & Benchmark Table)
// ------------------------------------------------------------------------------
let
    SourcePath = "c:\Users\stefi\Desktop\education\data\university_final_dataset.xlsx",
    Source = Excel.Workbook(File.Contents(SourcePath), null, true),
    Regional_Sheet = Source{[Item="Regional_Benchmarks",Kind="Sheet"]}[Data],
    PromotedHeaders = Table.PromoteHeaders(Regional_Sheet, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders,{
        {"region", type text},
        {"university_count", Int64.Type},
        {"avg_overall_score", type number},
        {"avg_intl_students_pct", type number},
        {"avg_faculty_student_ratio", type number},
        {"avg_academic_reputation", type number},
        {"avg_research_impact", type number},
        {"total_publications", Int64.Type},
        {"total_students", Int64.Type}
    })
in
    ChangedTypes

// ------------------------------------------------------------------------------
// Query 3: Country_Benchmarks (Dimension & Benchmark Table)
// ------------------------------------------------------------------------------
let
    SourcePath = "c:\Users\stefi\Desktop\education\data\university_final_dataset.xlsx",
    Source = Excel.Workbook(File.Contents(SourcePath), null, true),
    Country_Sheet = Source{[Item="Country_Benchmarks",Kind="Sheet"]}[Data],
    PromotedHeaders = Table.PromoteHeaders(Country_Sheet, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders,{
        {"region", type text},
        {"country", type text},
        {"university_count", Int64.Type},
        {"top_rank", Int64.Type},
        {"avg_score", type number},
        {"avg_intl_pct", type number},
        {"total_publications", Int64.Type}
    })
in
    ChangedTypes

// ------------------------------------------------------------------------------
// Query 4: _DAX_Measures (Measure Repository Table)
// ------------------------------------------------------------------------------
let
    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
    #"Removed Columns" = Table.RemoveColumns(Source,{"Column1"})
in
    #"Removed Columns"
