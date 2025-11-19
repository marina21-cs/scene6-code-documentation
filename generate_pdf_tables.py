"""
Generate PDF Tables for All Statistical Test Results
Professional formatting with computation details
"""

import pandas as pd
import numpy as np
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway, ttest_ind, ttest_1samp
import warnings
warnings.filterwarnings('ignore')

# Load and clean data
df = pd.read_csv('scenario_6_Online_Course_Completion.xlsx.csv')
df_clean = df[df['Time_Spent_Hours'] >= 0].copy()
df_clean['Completed_Numeric'] = df_clean['Completed'].map({'No': 0, 'Yes': 1})

print("="*80)
print("GENERATING PDF TABLES FOR ALL OBJECTIVES")
print("="*80)

# Create PDF document
pdf_filename = "Statistical_Results_Tables.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
elements = []
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=16,
    textColor=colors.HexColor('#1f4788'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#2e5c8a'),
    spaceAfter=10,
    spaceBefore=15,
    fontName='Helvetica-Bold'
)

subheading_style = ParagraphStyle(
    'CustomSubHeading',
    parent=styles['Heading3'],
    fontSize=11,
    textColor=colors.HexColor('#444444'),
    spaceAfter=8,
    fontName='Helvetica-Bold'
)

normal_style = ParagraphStyle(
    'CustomNormal',
    parent=styles['Normal'],
    fontSize=10,
    spaceAfter=6
)

# Title
elements.append(Paragraph("STATISTICAL ANALYSIS RESULTS", title_style))
elements.append(Paragraph("Online Course Completion Study", styles['Normal']))
elements.append(Spacer(1, 0.2*inch))

# ============================================================================
# DATA SUMMARY
# ============================================================================

elements.append(Paragraph("DATA SUMMARY", heading_style))

data_summary = [
    ['Metric', 'Value'],
    ['Original Dataset Size', '2,100 rows'],
    ['Negative Time Values Removed', '5 rows (0.24%)'],
    ['Final Clean Dataset', '2,095 rows'],
    ['Completion Rate', f"{(df_clean['Completed']=='Yes').sum()} / {len(df_clean)} ({(df_clean['Completed']=='Yes').sum()/len(df_clean)*100:.2f}%)"],
    ['Average Time Spent', f"{df_clean['Time_Spent_Hours'].mean():.2f} hours"],
    ['Average Age', f"{df_clean['Age'].mean():.2f} years"]
]

table = Table(data_summary, colWidths=[3.5*inch, 3*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')])
]))
elements.append(table)
elements.append(Spacer(1, 0.3*inch))

# ============================================================================
# OBJECTIVE 2: TWO-SAMPLE T-TEST
# ============================================================================

elements.append(Paragraph("OBJECTIVE 2: COMPARE TIME SPENT BY COMPLETION STATUS", heading_style))
elements.append(Paragraph("Two-Sample T-Test (Independent Samples)", subheading_style))

time_completed = df_clean[df_clean['Completed'] == 'Yes']['Time_Spent_Hours']
time_not_completed = df_clean[df_clean['Completed'] == 'No']['Time_Spent_Hours']
t_stat, p_value = ttest_ind(time_completed, time_not_completed)

# Descriptive Statistics Table
desc_data = [
    ['Group', 'N', 'Mean (hours)', 'Std Dev', 'Min', 'Max'],
    ['Completed (Yes)', f"{len(time_completed)}", f"{time_completed.mean():.4f}", 
     f"{time_completed.std():.4f}", f"{time_completed.min():.4f}", f"{time_completed.max():.4f}"],
    ['Not Completed (No)', f"{len(time_not_completed)}", f"{time_not_completed.mean():.4f}", 
     f"{time_not_completed.std():.4f}", f"{time_not_completed.min():.4f}", f"{time_not_completed.max():.4f}"],
    ['Difference', '', f"{time_completed.mean() - time_not_completed.mean():.4f}", '', '', '']
]

table = Table(desc_data, colWidths=[1.5*inch, 0.8*inch, 1.2*inch, 1*inch, 0.9*inch, 0.9*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#ffe6e6'))
]))
elements.append(table)
elements.append(Spacer(1, 0.15*inch))

# Test Results Table
test_data = [
    ['Test Statistic', 'Value'],
    ['t-statistic', f"{t_stat:.4f}"],
    ['Degrees of Freedom', f"{len(time_completed) + len(time_not_completed) - 2}"],
    ['p-value (two-tailed)', f"{p_value:.4f}"],
    ['Significance Level (α)', "0.05"],
    ['Decision', "FAIL TO REJECT H₀" if p_value > 0.05 else "REJECT H₀"],
    ['Conclusion', "No significant difference" if p_value > 0.05 else "Significant difference exists"]
]

table = Table(test_data, colWidths=[3*inch, 3.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, 5), (-1, 6), colors.HexColor('#e6f7ff'))
]))
elements.append(table)
elements.append(Spacer(1, 0.25*inch))

# ============================================================================
# OBJECTIVE 3: ONE-SAMPLE T-TEST
# ============================================================================

elements.append(Paragraph("OBJECTIVE 3: TEST IF AVERAGE TIME EXCEEDS 15 HOURS", heading_style))
elements.append(Paragraph("One-Sample T-Test (vs. Benchmark from Previous Study)", subheading_style))

hypothesized_mean = 15.0
time_spent_all = df_clean['Time_Spent_Hours']
t_stat_one, p_value_two_tailed = ttest_1samp(time_spent_all, hypothesized_mean)
p_value_one_tailed = p_value_two_tailed / 2 if t_stat_one > 0 else 1 - (p_value_two_tailed / 2)

# Sample Statistics
sample_data = [
    ['Statistic', 'Value'],
    ['Sample Size (N)', f"{len(time_spent_all)}"],
    ['Sample Mean', f"{time_spent_all.mean():.4f} hours"],
    ['Sample Std Dev', f"{time_spent_all.std():.4f} hours"],
    ['Hypothesized Mean (μ₀)', f"{hypothesized_mean:.4f} hours"],
    ['Difference (x̄ - μ₀)', f"{time_spent_all.mean() - hypothesized_mean:.4f} hours"],
    ['Standard Error', f"{time_spent_all.std() / np.sqrt(len(time_spent_all)):.4f}"]
]

table = Table(sample_data, colWidths=[3*inch, 3.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, 4), (0, 5), colors.HexColor('#fff4e6'))
]))
elements.append(table)
elements.append(Spacer(1, 0.15*inch))

# Test Results
test_data = [
    ['Test Statistic', 'Value'],
    ['t-statistic', f"{t_stat_one:.4f}"],
    ['Degrees of Freedom', f"{len(time_spent_all) - 1}"],
    ['p-value (two-tailed)', f"{p_value_two_tailed:.4f}"],
    ['p-value (one-tailed)', f"{p_value_one_tailed:.4f}"],
    ['Significance Level (α)', "0.05"],
    ['Test Direction', "One-tailed (greater than)"],
    ['Decision', "REJECT H₀" if p_value_one_tailed < 0.05 else "FAIL TO REJECT H₀"],
    ['Conclusion', "Average EXCEEDS 15 hours" if p_value_one_tailed < 0.05 else "No evidence average exceeds 15 hours"]
]

table = Table(test_data, colWidths=[3*inch, 3.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, 7), (-1, 8), colors.HexColor('#e6ffe6'))
]))
elements.append(table)
elements.append(PageBreak())

# ============================================================================
# OBJECTIVE 4: CHI-SQUARED TEST
# ============================================================================

elements.append(Paragraph("OBJECTIVE 4: COMPARE COURSE TYPE BY COMPLETION STATUS", heading_style))
elements.append(Paragraph("Chi-Squared Test of Independence", subheading_style))

# Contingency Table
contingency_table = pd.crosstab(df_clean['Course_Type'], df_clean['Completed'])
chi2_stat, p_value_chi2, dof, expected_freq = chi2_contingency(contingency_table)

# Observed Frequencies
obs_data = [['Course Type', 'Not Completed', 'Completed', 'Total']]
for idx, row in contingency_table.iterrows():
    obs_data.append([idx, str(row['No']), str(row['Yes']), str(row['No'] + row['Yes'])])
obs_data.append(['Total', str(contingency_table['No'].sum()), 
                 str(contingency_table['Yes'].sum()), str(len(df_clean))])

table = Table(obs_data, colWidths=[1.8*inch, 1.5*inch, 1.5*inch, 1.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#e6f7ff')),
    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold')
]))
elements.append(Paragraph("Observed Frequencies:", subheading_style))
elements.append(table)
elements.append(Spacer(1, 0.15*inch))

# Expected Frequencies
exp_df = pd.DataFrame(expected_freq, index=contingency_table.index, columns=contingency_table.columns)
exp_data = [['Course Type', 'Not Completed', 'Completed', 'Total']]
for idx, row in exp_df.iterrows():
    total = row['No'] + row['Yes']
    exp_data.append([idx, f"{row['No']:.2f}", f"{row['Yes']:.2f}", f"{total:.2f}"])

table = Table(exp_data, colWidths=[1.8*inch, 1.5*inch, 1.5*inch, 1.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')])
]))
elements.append(Paragraph("Expected Frequencies:", subheading_style))
elements.append(table)
elements.append(Spacer(1, 0.15*inch))

# Test Results
test_data = [
    ['Test Statistic', 'Value'],
    ['Chi-Squared (χ²)', f"{chi2_stat:.4f}"],
    ['Degrees of Freedom', f"{dof}"],
    ['p-value', f"{p_value_chi2:.4f}"],
    ['Significance Level (α)', "0.05"],
    ['Decision', "FAIL TO REJECT H₀" if p_value_chi2 > 0.05 else "REJECT H₀"],
    ['Conclusion', "Variables are independent" if p_value_chi2 > 0.05 else "Variables are associated"]
]

table = Table(test_data, colWidths=[3*inch, 3.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, 5), (-1, 6), colors.HexColor('#e6f7ff'))
]))
elements.append(table)
elements.append(PageBreak())

# ============================================================================
# OBJECTIVE 5: ANOVA
# ============================================================================

elements.append(Paragraph("OBJECTIVE 5: COMPARE DEVICE USED BY TIME SPENT", heading_style))
elements.append(Paragraph("One-Way ANOVA (Analysis of Variance)", subheading_style))

time_by_device = {
    'Desktop': df_clean[df_clean['Device_Used'] == 'Desktop']['Time_Spent_Hours'],
    'Mobile': df_clean[df_clean['Device_Used'] == 'Mobile']['Time_Spent_Hours'],
    'Tablet': df_clean[df_clean['Device_Used'] == 'Tablet']['Time_Spent_Hours']
}

f_stat, p_value_anova = f_oneway(time_by_device['Desktop'], 
                                  time_by_device['Mobile'], 
                                  time_by_device['Tablet'])

# Descriptive Statistics by Device
desc_data = [['Device', 'N', 'Mean (hours)', 'Std Dev', 'Min', 'Max']]
for device, times in time_by_device.items():
    desc_data.append([device, f"{len(times)}", f"{times.mean():.4f}", 
                     f"{times.std():.4f}", f"{times.min():.4f}", f"{times.max():.4f}"])

table = Table(desc_data, colWidths=[1.3*inch, 0.8*inch, 1.3*inch, 1.1*inch, 1*inch, 1*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')])
]))
elements.append(table)
elements.append(Spacer(1, 0.15*inch))

# ANOVA Table (detailed breakdown)
# Calculate sums of squares
grand_mean = df_clean['Time_Spent_Hours'].mean()
ss_between = sum([len(times) * (times.mean() - grand_mean)**2 for times in time_by_device.values()])
ss_within = sum([((times - times.mean())**2).sum() for times in time_by_device.values()])
ss_total = ss_between + ss_within
df_between = len(time_by_device) - 1
df_within = len(df_clean) - len(time_by_device)
ms_between = ss_between / df_between
ms_within = ss_within / df_within

anova_table_data = [
    ['Source', 'Sum of Squares', 'df', 'Mean Square', 'F-statistic', 'p-value'],
    ['Between Groups', f"{ss_between:.4f}", f"{df_between}", f"{ms_between:.4f}", 
     f"{f_stat:.4f}", f"{p_value_anova:.4f}"],
    ['Within Groups', f"{ss_within:.4f}", f"{df_within}", f"{ms_within:.4f}", '', ''],
    ['Total', f"{ss_total:.4f}", f"{len(df_clean)-1}", '', '', '']
]

table = Table(anova_table_data, colWidths=[1.5*inch, 1.4*inch, 0.7*inch, 1.3*inch, 1.2*inch, 1.2*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#e6f7ff')),
    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold')
]))
elements.append(Paragraph("ANOVA Table:", subheading_style))
elements.append(table)
elements.append(Spacer(1, 0.15*inch))

# Test Results
test_data = [
    ['Test Statistic', 'Value'],
    ['F-statistic', f"{f_stat:.4f}"],
    ['p-value', f"{p_value_anova:.4f}"],
    ['Significance Level (α)', "0.05"],
    ['Decision', "FAIL TO REJECT H₀" if p_value_anova > 0.05 else "REJECT H₀"],
    ['Conclusion', "No significant difference across devices" if p_value_anova > 0.05 else "Significant difference exists"]
]

table = Table(test_data, colWidths=[3*inch, 3.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, 4), (-1, 5), colors.HexColor('#e6f7ff'))
]))
elements.append(table)
elements.append(PageBreak())

# ============================================================================
# OBJECTIVE 6: TWO-SAMPLE PROPORTION Z-TEST
# ============================================================================

elements.append(Paragraph("OBJECTIVE 6: TEST IF BELOW AVERAGE AGE HAS HIGHER COMPLETION", heading_style))
elements.append(Paragraph("Two-Sample Proportion Z-Test", subheading_style))

average_age = df_clean['Age'].mean()
df_clean['Age_Group'] = df_clean['Age'].apply(lambda x: 'Below Average' if x < average_age else 'Above Average')

below_avg = df_clean[df_clean['Age_Group'] == 'Below Average']
above_avg = df_clean[df_clean['Age_Group'] == 'Above Average']

n1 = len(below_avg)
n2 = len(above_avg)
x1 = (below_avg['Completed'] == 'Yes').sum()
x2 = (above_avg['Completed'] == 'Yes').sum()
p1 = x1 / n1
p2 = x2 / n2
p_pooled = (x1 + x2) / (n1 + n2)
se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))
z_stat = (p1 - p2) / se
p_value_z = 1 - stats.norm.cdf(z_stat)

# Proportions Table
prop_data = [
    ['Age Group', 'N', 'Completed', 'Not Completed', 'Proportion', 'Percentage'],
    ['Below Average', f"{n1}", f"{x1}", f"{n1-x1}", f"{p1:.4f}", f"{p1*100:.2f}%"],
    ['Above Average', f"{n2}", f"{x2}", f"{n2-x2}", f"{p2:.4f}", f"{p2*100:.2f}%"],
    ['Difference', '', '', '', f"{p1-p2:.4f}", f"{(p1-p2)*100:.2f}%"]
]

table = Table(prop_data, colWidths=[1.4*inch, 0.8*inch, 1.1*inch, 1.3*inch, 1.1*inch, 1.1*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
    ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#ffe6e6'))
]))
elements.append(table)
elements.append(Spacer(1, 0.15*inch))

# Test Results
test_data = [
    ['Test Statistic', 'Value'],
    ['Average Age Cutoff', f"{average_age:.2f} years"],
    ['Pooled Proportion (p̂)', f"{p_pooled:.4f}"],
    ['Standard Error', f"{se:.4f}"],
    ['z-statistic', f"{z_stat:.4f}"],
    ['p-value (one-tailed)', f"{p_value_z:.4f}"],
    ['Significance Level (α)', "0.05"],
    ['Test Direction', "One-tailed (greater than)"],
    ['Decision', "FAIL TO REJECT H₀" if p_value_z > 0.05 else "REJECT H₀"],
    ['Conclusion', "No evidence of higher completion for below-average age" if p_value_z > 0.05 
     else "Below-average age has significantly higher completion"]
]

table = Table(test_data, colWidths=[3*inch, 3.5*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, 8), (-1, 9), colors.HexColor('#e6f7ff'))
]))
elements.append(table)
elements.append(PageBreak())

# ============================================================================
# SUMMARY TABLE
# ============================================================================

elements.append(Paragraph("SUMMARY OF ALL STATISTICAL TESTS", heading_style))

summary_data = [
    ['Objective', 'Test Used', 'Test Statistic', 'p-value', 'Decision', 'Conclusion'],
    ['Obj 2: Time by\nCompletion', 'Two-Sample\nT-Test', f"t = {t_stat:.4f}", 
     f"{p_value:.4f}", "Fail to Reject H₀", "No significant\ndifference"],
    ['Obj 3: Time vs\n15 hours', 'One-Sample\nT-Test', f"t = {t_stat_one:.4f}", 
     f"{p_value_one_tailed:.4f}", "Reject H₀" if p_value_one_tailed < 0.05 else "Fail to Reject H₀", 
     "Significantly\nexceeds 15 hrs" if p_value_one_tailed < 0.05 else "No evidence"],
    ['Obj 4: Course Type\nby Completion', 'Chi-Squared\nTest', f"χ² = {chi2_stat:.4f}", 
     f"{p_value_chi2:.4f}", "Fail to Reject H₀", "Variables are\nindependent"],
    ['Obj 5: Device by\nTime Spent', 'One-Way\nANOVA', f"F = {f_stat:.4f}", 
     f"{p_value_anova:.4f}", "Fail to Reject H₀", "No significant\ndifference"],
    ['Obj 6: Age Group\nby Completion', 'Two-Sample\nProportion Z', f"z = {z_stat:.4f}", 
     f"{p_value_z:.4f}", "Fail to Reject H₀", "No significant\ndifference"]
]

table = Table(summary_data, colWidths=[1.3*inch, 1.1*inch, 1.1*inch, 0.9*inch, 1.2*inch, 1.2*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#e6ffe6'))  # Highlight rejected H0
]))
elements.append(table)
elements.append(Spacer(1, 0.2*inch))

# Footer
elements.append(Paragraph("<i>Note: Significance level α = 0.05 used for all tests. "
                         "Only Objective 3 (One-Sample T-Test) resulted in rejecting the null hypothesis.</i>", 
                         normal_style))

# Build PDF
doc.build(elements)

print(f"\n✓ PDF successfully generated: {pdf_filename}")
print(f"\nThe PDF contains:")
print("  - Data Summary Table")
print("  - Objective 2: Two-Sample T-Test (Descriptive Stats + Test Results)")
print("  - Objective 3: One-Sample T-Test (Sample Stats + Test Results)")
print("  - Objective 4: Chi-Squared Test (Observed + Expected Frequencies + Results)")
print("  - Objective 5: One-Way ANOVA (Descriptive Stats + ANOVA Table + Results)")
print("  - Objective 6: Two-Sample Proportion Z-Test (Proportions + Results)")
print("  - Summary Table of All Tests")
print("\n" + "="*80)
print("PDF GENERATION COMPLETE")
print("="*80)
