"""
Generates the publication-grade docs/dashboard_storyboard.pdf using ReportLab.
Covers all 4 dashboard pages with layouts, wireframes, color palettes, visual specs,
KPI definitions, and interactive behaviors.
"""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 570, "EduVision DV — Higher Education Performance Dashboard Storyboard & Specs")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 562, 738, 562)

        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(738, 30, page_str)
        self.drawString(54, 30, "CONFIDENTIAL & PROPRIETARY — EDUVISION ANALYTICS ARCHITECTURE")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 42, 738, 42)
        self.restoreState()

def build_pdf():
    pdf_path = "docs/dashboard_storyboard.pdf"
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    # Landscape Letter: 11 x 8.5 inches (792 x 612 pt)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(letter),
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#475569'),
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=10,
        spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#334155'),
        spaceBefore=6,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=6
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1E3A8A'),
        backColor=colors.HexColor('#EFF6FF'),
        borderColor=colors.HexColor('#BFDBFE'),
        borderWidth=1,
        borderPadding=6,
        spaceAfter=10
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_body_style = ParagraphStyle(
        'TableBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1E293B')
    )

    story = []

    # ================= PAGE 1: TITLE & EXECUTIVE SUMMARY =================
    story.append(Paragraph("EduVision DV: Higher Education Performance Dashboard", title_style))
    story.append(Paragraph("<b>Milestone 2 & 4: Dashboard Storyboard, Layout Blueprint & Technical Specifications</b>", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#7C5CFC"), spaceAfter=12))

    summary_text = """
    <b>Executive Summary:</b><br/>
    The EduVision DV analytics suite transforms complex global higher education metrics from QS World University Rankings 
    and Times Higher Education (THE) into an executive-ready Power BI reporting platform. The suite features four interconnected, 
    highly responsive analytical views designed for academic leadership, institutional researchers, policy analysts, and prospective students.
    """
    story.append(Paragraph(summary_text, body_style))

    # Architecture Overview Table
    arch_data = [
        [Paragraph("Dashboard View", table_header_style), Paragraph("Primary Target Audience", table_header_style), Paragraph("Core Analytical Objective", table_header_style), Paragraph("Key Visual Deliverables", table_header_style)],
        [
            Paragraph("<b>1. University Overview</b>", table_body_style),
            Paragraph("Provosts, Presidents, Global Strategy Teams", table_body_style),
            Paragraph("Executive benchmarking, institutional standing, macro regional distributions, and top-tier score evolutions.", table_body_style),
            Paragraph("6 KPI Cards, Global Rank Top 10, Score Trend (2020-2024), Regional Donut, Top 5 Pubs, Map, Faculty Ratio.", table_body_style)
        ],
        [
            Paragraph("<b>2. Research Analytics</b>", table_body_style),
            Paragraph("VPs of Research, Grant Officers, Deans", table_body_style),
            Paragraph("Publication productivity, citation impact, researcher output elasticity, and discipline benchmarking.", table_body_style),
            Paragraph("Research Impact vs Volume Quadrants, Citations/Faculty Scatter, Subject Area Treemap, Top Research Hubs.", table_body_style)
        ],
        [
            Paragraph("<b>3. Student Analytics</b>", table_body_style),
            Paragraph("Deans of Admissions, Student Affairs, HR", table_body_style),
            Paragraph("Internationalization percentages, faculty-to-student ratios, diversity distribution, enrollment capacity.", table_body_style),
            Paragraph("Global Student Heatmap, Faculty-to-Student Ratio Bar Chart, International Student %, Enrollment Trends.", table_body_style)
        ],
        [
            Paragraph("<b>4. Country Comparison</b>", table_body_style),
            Paragraph("Government Ministries, Policy Analysts", table_body_style),
            Paragraph("Sovereign higher-ed capacity, regional excellence concentration, top-100 density, cross-border competitiveness.", table_body_style),
            Paragraph("Country Benchmark Matrix, Sovereign Score Radar, Regional Distribution Treemap, Multi-Country Ranking.", table_body_style)
        ]
    ]

    t_arch = Table(arch_data, colWidths=[120, 140, 240, 184])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_arch)
    story.append(Spacer(1, 10))

    # Design System Specs
    story.append(Paragraph("Design System & UI Color Tokens (High-Contrast Modern Dark Theme)", h1_style))
    palette_data = [
        [
            Paragraph("<b>Canvas Canvas:</b> #0B0E1B<br/>Deep Space Navy", table_body_style),
            Paragraph("<b>Surface Card:</b> #1B1F38<br/>Elevation Fill", table_body_style),
            Paragraph("<b>Primary Accent:</b> #7C5CFC<br/>Electric Indigo / Violet", table_body_style),
            Paragraph("<b>Secondary Accent:</b> #3B82F6<br/>Vibrant Azure Blue", table_body_style)
        ],
        [
            Paragraph("<b>Cyan Accent:</b> #06B6D4<br/>High-Impact Teal", table_body_style),
            Paragraph("<b>Positive KPI:</b> #10B981<br/>Emerald Growth Indicator", table_body_style),
            Paragraph("<b>Warning/Highlight:</b> #F59E0B<br/>Amber Benchmark Marker", table_body_style),
            Paragraph("<b>Typography:</b> Segoe UI / Inter<br/>#FFFFFF & #94A3B8 Secondary", table_body_style)
        ]
    ]
    t_palette = Table(palette_data, colWidths=[171, 171, 171, 171])
    t_palette.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_palette)

    # ================= PAGE 2: VIEW 1 - UNIVERSITY OVERVIEW =================
    story.append(PageBreak())
    story.append(Paragraph("Page 1: University Overview Dashboard (Wireframe & Visual Architecture)", h1_style))
    story.append(Paragraph("<b>Exact match to design layout requirements: Dark Canvas (1920x1080 / 16:9), Header Slicers, Left Nav, 6 KPI Cards, and 6 Deep Visuals</b>", subtitle_style))

    view1_wireframe = [
        [
            Paragraph("<b>HEADER:</b> EduVision DV | Year: [2024 ▼] | Region: [All ▼] | Country: [All ▼] | Discipline: [All Disciplines ▼] | [Reset Filters] | Home, Analytics, About", table_body_style)
        ]
    ]
    t_wf_head = Table(view1_wireframe, colWidths=[684])
    t_wf_head.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1E293B')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#334155')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_wf_head)
    story.append(Spacer(1, 4))

    # Top KPI Row (6 Cards)
    kpis = [
        [
            Paragraph("<b>#1 MIT</b><br/><font size=7 color='#64748B'>Top Global Rank</font>", table_body_style),
            Paragraph("<b>1,503</b><br/><font size=7 color='#64748B'>Total Ranked Univs</font>", table_body_style),
            Paragraph("<b>72.6</b> <font size=7 color='#10B981'>▲+2.4%</font><br/><font size=7 color='#64748B'>Avg Overall Score</font>", table_body_style),
            Paragraph("<b>28.7%</b> <font size=7 color='#10B981'>▲+1.8%</font><br/><font size=7 color='#64748B'>Intl Students %</font>", table_body_style),
            Paragraph("<b>1 : 17.3</b> <font size=7 color='#EF4444'>▼-0.6</font><br/><font size=7 color='#64748B'>Faculty Ratio</font>", table_body_style),
            Paragraph("<b>2.45M</b> <font size=7 color='#10B981'>▲+6.3%</font><br/><font size=7 color='#64748B'>Total Publications</font>", table_body_style)
        ]
    ]
    t_kpis = Table(kpis, colWidths=[114, 114, 114, 114, 114, 114])
    t_kpis.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#7C5CFC')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_kpis)
    story.append(Spacer(1, 4))

    # Main Grid (Sidebar + 2 rows of visuals)
    grid_layout = [
        [
            Paragraph("<b>LEFT NAV & FILTERS</b><br/><br/>• [Overview (Active)]<br/>• [Research Analytics]<br/>• [Student Analytics]<br/>• [Country Comparison]<br/><br/><i>Slicers:</i><br/>Year (2024)<br/>Region (All)<br/>Country (All)<br/>Subject (All)<br/><br/><b>[Reset Filters]</b>", table_body_style),
            Paragraph("<b>VISUAL 1: Top 10 Universities by Global Ranking</b><br/>Columns: Rank | University | Country | Score<br/>1. MIT (USA) - 100.0<br/>2. Cambridge (UK) - 98.7<br/>3. Oxford (UK) - 97.9<br/>4. Harvard (USA) - 97.1<br/>5. Stanford (USA) - 96.8<br/>6. Imperial (UK) - 95.4<br/>7. ETH Zurich (CH) - 93.7<br/>8. NUS (SG) - 92.9<br/>9. UCL (UK) - 91.8<br/>10. UC Berkeley (USA) - 90.8", table_body_style),
            Paragraph("<b>VISUAL 2: Top 10 Univs Score Trend (2020-2024)</b><br/>Multi-Line Chart:<br/>• X-Axis: 2020, 2021, 2022, 2023, 2024<br/>• Y-Axis: Overall Score (80 - 100)<br/>• Lines: MIT (#7C5CFC), Cambridge (#3B82F6), Oxford (#06B6D4), Harvard (#EC4899), Stanford (#F59E0B)<br/>• Cross-highlight on click", table_body_style),
            Paragraph("<b>VISUAL 3: Universities by Region</b><br/>Donut Chart (Total: 1,503):<br/>• Europe: 37.6% (565)<br/>• North America: 28.3% (425)<br/>• Asia: 24.8% (373)<br/>• Oceania: 6.1% (92)<br/>• South America: 3.2% (48)", table_body_style)
        ],
        [
            Paragraph("<b>DATA FOOTER:</b><br/>Source: QS & THE 2024<br/>Updated: Oct 2026", table_body_style),
            Paragraph("<b>VISUAL 4: Publications by Top 5 Universities</b><br/>Horizontal Bar Chart:<br/>• Harvard: 208K<br/>• Stanford: 189K<br/>• MIT: 186K<br/>• Oxford: 163K<br/>• Cambridge: 150K", table_body_style),
            Paragraph("<b>VISUAL 5: International Students % by Region</b><br/>Filled Global Map / Choropleth:<br/>Color gradient: 10% (Dark Blue) to 45% (Bright Orange)<br/>Oceania (39.0%), Europe (32.0%), N. America (21.5%), Asia (16.5%), S. America (6.5%)", table_body_style),
            Paragraph("<b>VISUAL 6: Faculty to Student Ratio by Region</b><br/>Clustered Column Chart (Students per Faculty):<br/>• North America: 1:25.0<br/>• Europe: 1:21.4<br/>• Asia: 1:18.7<br/>• Oceania: 1:16.2<br/>• South America: 1:14.3", table_body_style)
        ]
    ]
    t_grid = Table(grid_layout, colWidths=[114, 190, 200, 180])
    t_grid.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (0,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_grid)

    # ================= PAGE 3: VIEW 2 - RESEARCH ANALYTICS =================
    story.append(PageBreak())
    story.append(Paragraph("Page 2: Research Analytics Dashboard (Wireframe & Visual Architecture)", h1_style))
    story.append(Paragraph("<b>Focus: Publications output, Citation velocity, Research impact vs productivity quadrants, and Discipline breakdown</b>", subtitle_style))

    res_kpis = [
        [
            Paragraph("<b>2.45M</b><br/><font size=7 color='#64748B'>Total Indexed Publications</font>", table_body_style),
            Paragraph("<b>12.8M</b><br/><font size=7 color='#64748B'>Cumulative Citations</font>", table_body_style),
            Paragraph("<b>71.6</b><br/><font size=7 color='#64748B'>Avg Research Impact Score</font>", table_body_style),
            Paragraph("<b>5.2</b><br/><font size=7 color='#64748B'>Avg Citations / Publication</font>", table_body_style),
            Paragraph("<b>Harvard University</b><br/><font size=7 color='#64748B'>Top Volume Leader (208K)</font>", table_body_style),
            Paragraph("<b>Caltech (100.0)</b><br/><font size=7 color='#64748B'>Top Citation Impact Leader</font>", table_body_style)
        ]
    ]
    t_res_kpis = Table(res_kpis, colWidths=[114, 114, 114, 114, 114, 114])
    t_res_kpis.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#3B82F6')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_res_kpis)
    story.append(Spacer(1, 6))

    res_grid = [
        [
            Paragraph("<b>VISUAL 1: Research Impact vs Publications (Scatter Plot)</b><br/>• X-Axis: Publications Volume (0 - 250K)<br/>• Y-Axis: Research Impact Score (0 - 100)<br/>• Bubble Size: Total Faculty Count<br/>• Bubble Color: Continental Region<br/>• Quadrant Lines: Median Publications & Impact<br/><i>Highlights elite powerhouses in upper-right quadrant.</i>", table_body_style),
            Paragraph("<b>VISUAL 2: Research Output by Subject Area (Treemap)</b><br/>• Discipline breakdown:<br/>  - Engineering & Technology (32%)<br/>  - Life Sciences & Medicine (28%)<br/>  - Natural Sciences (22%)<br/>  - Social Sciences & Management (12%)<br/>  - Arts & Humanities (6%)<br/>• Tooltip reveals average citations per faculty.", table_body_style)
        ],
        [
            Paragraph("<b>VISUAL 3: Top 15 Research Universities (Horizontal Stacked Bar)</b><br/>• Institutional ranking showing Publications volume breakdown by Discipline.<br/>• Direct institutional filtering and cross-highlighting on click.<br/>• Top 5: Harvard, Toronto, Stanford, MIT, Tsinghua.", table_body_style),
            Paragraph("<b>VISUAL 4: Research Productivity Index Trend (2020-2024)</b><br/>• Area / Line chart showing research productivity (publications per faculty) compound annual growth rate (CAGR).<br/>• Demonstrates regional acceleration in East Asia and stable efficiency in Western Europe.", table_body_style)
        ]
    ]
    t_res_grid = Table(res_grid, colWidths=[342, 342])
    t_res_grid.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_res_grid)

    # ================= PAGE 4: VIEW 3 - STUDENT ANALYTICS =================
    story.append(PageBreak())
    story.append(Paragraph("Page 3: Student Analytics Dashboard (Wireframe & Visual Architecture)", h1_style))
    story.append(Paragraph("<b>Focus: Student diversity, international student mobility, faculty-to-student ratios, and institutional capacity</b>", subtitle_style))

    stu_kpis = [
        [
            Paragraph("<b>32.8M</b><br/><font size=7 color='#64748B'>Total Student Population</font>", table_body_style),
            Paragraph("<b>7.89M</b><br/><font size=7 color='#64748B'>Total International Students</font>", table_body_style),
            Paragraph("<b>28.7%</b><br/><font size=7 color='#64748B'>Avg International Ratio</font>", table_body_style),
            Paragraph("<b>1 : 17.3</b><br/><font size=7 color='#64748B'>Global Avg Faculty Ratio</font>", table_body_style),
            Paragraph("<b>Imperial College (60.2%)</b><br/><font size=7 color='#64748B'>Highest International %</font>", table_body_style),
            Paragraph("<b>Caltech (1 : 1.9)</b><br/><font size=7 color='#64748B'>Best Faculty-Student Ratio</font>", table_body_style)
        ]
    ]
    t_stu_kpis = Table(stu_kpis, colWidths=[114, 114, 114, 114, 114, 114])
    t_stu_kpis.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#06B6D4')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_stu_kpis)
    story.append(Spacer(1, 6))

    stu_grid = [
        [
            Paragraph("<b>VISUAL 1: International Student Concentration Map</b><br/>• Bubble Map showing destination intensity for international scholars.<br/>• UK and Australian universities exhibit >40% average international cohort.<br/>• Slicer allows filtering by study discipline.", table_body_style),
            Paragraph("<b>VISUAL 2: Faculty-to-Student Ratio Distribution (Histogram / Bar)</b><br/>• Distribution curve showing institutional staffing density.<br/>• Bins: 1:1-10 (Elite research), 1:10-20 (Standard high-tier), 1:20-30 (Large state universities), >1:30 (Mass enrollment).", table_body_style)
        ],
        [
            Paragraph("<b>VISUAL 3: International Cohort vs Total Enrollment (Scatter)</b><br/>• X-Axis: Total Student Headcount (Log scale: 1K - 100K)<br/>• Y-Axis: International Students % (0% - 70%)<br/>• Reveals institutional internationalization strategies across boutique vs mega-universities.", table_body_style),
            Paragraph("<b>VISUAL 4: Student Body Growth & International % Trend (2020-2024)</b><br/>• Dual-Axis Line & Clustered Column:<br/>  - Primary Axis: Total Headcount Growth (Columns)<br/>  - Secondary Axis: International Student % (Line with markers)<br/>• Tracks post-pandemic international mobility recovery.", table_body_style)
        ]
    ]
    t_stu_grid = Table(stu_grid, colWidths=[342, 342])
    t_stu_grid.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_stu_grid)

    # ================= PAGE 5: VIEW 4 - COUNTRY COMPARISON =================
    story.append(PageBreak())
    story.append(Paragraph("Page 4: Country Comparison Dashboard (Wireframe & Visual Architecture)", h1_style))
    story.append(Paragraph("<b>Focus: Cross-national performance benchmarking, top-100 density, regional excellence, and sovereign capacity</b>", subtitle_style))

    cntry_kpis = [
        [
            Paragraph("<b>38</b><br/><font size=7 color='#64748B'>Sovereign Nations Evaluated</font>", table_body_style),
            Paragraph("<b>United States (28)</b><br/><font size=7 color='#64748B'>Most Top 100 Univs</font>", table_body_style),
            Paragraph("<b>United Kingdom (17)</b><br/><font size=7 color='#64748B'>2nd Most Top 100 Univs</font>", table_body_style),
            Paragraph("<b>Switzerland (84.2)</b><br/><font size=7 color='#64748B'>Highest National Avg Score</font>", table_body_style),
            Paragraph("<b>Australia (41.8%)</b><br/><font size=7 color='#64748B'>Highest Avg Intl Ratio</font>", table_body_style),
            Paragraph("<b>Singapore (90.2)</b><br/><font size=7 color='#64748B'>Highest Academic Rep Avg</font>", table_body_style)
        ]
    ]
    t_cntry_kpis = Table(cntry_kpis, colWidths=[114, 114, 114, 114, 114, 114])
    t_cntry_kpis.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#10B981')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cntry_kpis)
    story.append(Spacer(1, 6))

    cntry_grid = [
        [
            Paragraph("<b>VISUAL 1: Country Benchmark Matrix (Matrix / Heatmap Table)</b><br/>• Rows: Sovereign Country (USA, UK, Australia, China, Germany, Switzerland...)<br/>• Values: Total Universities, Top 100 Count, Avg Score, Avg Citations, Avg Intl %, Faculty Ratio.<br/>• Conditional data bars and background color heatmaps.", table_body_style),
            Paragraph("<b>VISUAL 2: Regional Performance Radar / Grouped Bar Comparison</b><br/>• Multi-metric comparison across Europe, North America, Asia, Oceania, and South America.<br/>• Compares Overall Score, Research Impact, Internationalization, and Faculty Density on a common 0-100 scale.", table_body_style)
        ],
        [
            Paragraph("<b>VISUAL 3: Top 100 Concentration by Country (Treemap / Bar)</b><br/>• Visualizes geographic clustering of world-class universities.<br/>• USA (28%), UK (17%), Australia (9%), China (7%), Germany (6%), Switzerland (4%), Canada (4%).<br/>• Click-to-filter dynamically controls surrounding visuals.", table_body_style),
            Paragraph("<b>VISUAL 4: Country-level Internationalization vs Research Impact</b><br/>• Bubble chart plotting Sovereign Avg Intl Student % (X-axis) vs Sovereign Avg Research Impact Score (Y-axis).<br/>• Identifies global models: Highly internationalized UK/Australia vs Volume-driven East Asian leaders.", table_body_style)
        ]
    ]
    t_cntry_grid = Table(cntry_grid, colWidths=[342, 342])
    t_cntry_grid.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_cntry_grid)

    # ================= PAGE 6: INTERACTIVITY & TECHNICAL SPECS =================
    story.append(PageBreak())
    story.append(Paragraph("Technical Specifications: Navigation, Slicers, Bookmarks & DAX Model", h1_style))
    story.append(Paragraph("<b>End-to-End Enterprise Power BI Implementation Blueprint</b>", subtitle_style))

    tech_specs = [
        [Paragraph("Feature Area", table_header_style), Paragraph("Power BI Implementation Mechanism", table_header_style), Paragraph("User Interaction & Behavior", table_header_style)],
        [
            Paragraph("<b>Cross-Page Navigation</b>", table_body_style),
            Paragraph("Left vertical navigation rail with 4 button objects configured with Action = Page Navigation.", table_body_style),
            Paragraph("Instant single-click switching between Overview, Research, Student, and Country views while preserving slicer state.", table_body_style)
        ],
        [
            Paragraph("<b>Slicer Synchronization</b>", table_body_style),
            Paragraph("Sync Slicers pane active for Year, Region, Country, and Subject Area across all 4 pages.", table_body_style),
            Paragraph("Selecting 'Europe' on Overview persists across Research, Student, and Country views without manual reselection.", table_body_style)
        ],
        [
            Paragraph("<b>Reset Filters</b>", table_body_style),
            Paragraph("Bookmark created with Default State (All filters cleared) tied to a 'Reset Filters' icon button.", table_body_style),
            Paragraph("Restores all 4 global slicers to default aggregated view across all visual cards.", table_body_style)
        ],
        [
            Paragraph("<b>Drill-Through Actions</b>", table_body_style),
            Paragraph("Drill-through target page configured with University Name filter parameter.", table_body_style),
            Paragraph("Right-clicking any institution in Top 10 or Scatter plots opens deep individual institutional profile.", table_body_style)
        ],
        [
            Paragraph("<b>Theme Customization</b>", table_body_style),
            Paragraph("Custom JSON Theme (`EduVision_Theme.json`) loaded into Power BI Desktop.", table_body_style),
            Paragraph("Applies universal dark canvas `#0B0E1B`, card containers `#1B1F38`, Segoe UI font, and high-contrast color palette.", table_body_style)
        ],
        [
            Paragraph("<b>Data Model</b>", table_body_style),
            Paragraph("Star Schema: `University_Performance` (Fact Table) joined to `Regional_Benchmarks` and `Country_Benchmarks`.", table_body_style),
            Paragraph("High query efficiency with single-direction 1:* relationships and dedicated `DAX_Measures` table.", table_body_style)
        ]
    ]

    t_tech = Table(tech_specs, colWidths=[120, 240, 324])
    t_tech.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_tech)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {pdf_path}")

if __name__ == "__main__":
    build_pdf()
