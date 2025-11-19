"""
Online Course Completion Analysis
Statistical Tests and Visualizations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway, ttest_ind, ttest_1samp
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ============================================================================
# DATA LOADING AND CLEANING
# ============================================================================

print("="*80)
print("ONLINE COURSE COMPLETION ANALYSIS")
print("="*80)

# Load data
df = pd.read_csv('scenario_6_Online_Course_Completion.xlsx.csv')
print(f"\nOriginal dataset: {len(df)} rows")

# Check for negative time values
negative_time_count = (df['Time_Spent_Hours'] < 0).sum()
print(f"Negative time values found: {negative_time_count}")

# Clean data - remove negative time values
df_clean = df[df['Time_Spent_Hours'] >= 0].copy()
print(f"After removing negative values: {len(df_clean)} rows")
print(f"Rows removed: {len(df) - len(df_clean)}")

print("\n" + "="*80)
print("DATA SUMMARY")
print("="*80)
print(f"\n{df_clean.describe()}")
print(f"\nCompletion Status Distribution:\n{df_clean['Completed'].value_counts()}")
print(f"\nCourse Type Distribution:\n{df_clean['Course_Type'].value_counts()}")
print(f"\nDevice Used Distribution:\n{df_clean['Device_Used'].value_counts()}")

# ============================================================================
# TEST 2: COMPARE TIME SPENT BY COMPLETION STATUS (Two-Sample T-Test)
# ============================================================================

print("\n" + "="*80)
print("TEST 2: COMPARE TIME SPENT BY COMPLETION STATUS")
print("Two-Sample T-Test")
print("="*80)

# Separate data by completion status
time_completed = df_clean[df_clean['Completed'] == 'Yes']['Time_Spent_Hours']
time_not_completed = df_clean[df_clean['Completed'] == 'No']['Time_Spent_Hours']

print(f"\nCompleted Courses (Yes):")
print(f"  N = {len(time_completed)}")
print(f"  Mean = {time_completed.mean():.2f} hours")
print(f"  Std Dev = {time_completed.std():.2f} hours")

print(f"\nNot Completed Courses (No):")
print(f"  N = {len(time_not_completed)}")
print(f"  Mean = {time_not_completed.mean():.2f} hours")
print(f"  Std Dev = {time_not_completed.std():.2f} hours")

# Perform two-sample t-test
t_stat, p_value = ttest_ind(time_completed, time_not_completed)

print(f"\nHypothesis Test:")
print(f"  H0: μ_completed = μ_not_completed (no difference in mean time spent)")
print(f"  Ha: μ_completed ≠ μ_not_completed (there is a difference)")
print(f"\n  t-statistic = {t_stat:.4f}")
print(f"  p-value = {p_value:.4f}")
print(f"  Significance level α = 0.05")

if p_value > 0.05:
    print(f"\n  Decision: FAIL TO REJECT H0 (p-value = {p_value:.4f} > 0.05)")
    print(f"  Interpretation: There is NO statistically significant difference in time spent")
    print(f"  between completed and not completed courses at the 5% significance level.")
else:
    print(f"\n  Decision: REJECT H0 (p-value = {p_value:.4f} ≤ 0.05)")
    print(f"  Interpretation: There IS a statistically significant difference in time spent")
    print(f"  between completed and not completed courses.")

# Visualization for Test 2
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot
axes[0].boxplot([time_not_completed, time_completed], labels=['Not Completed', 'Completed'])
axes[0].set_ylabel('Time Spent (Hours)', fontsize=12)
axes[0].set_xlabel('Completion Status', fontsize=12)
axes[0].set_title('Time Spent by Completion Status\n(Box Plot)', fontsize=14, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Violin plot with means
parts = axes[1].violinplot([time_not_completed, time_completed], positions=[1, 2], 
                           showmeans=True, showmedians=True)
axes[1].set_xticks([1, 2])
axes[1].set_xticklabels(['Not Completed', 'Completed'])
axes[1].set_ylabel('Time Spent (Hours)', fontsize=12)
axes[1].set_xlabel('Completion Status', fontsize=12)
axes[1].set_title('Time Spent Distribution by Completion Status\n(Violin Plot)', 
                  fontsize=14, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('test2_time_by_completion.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: test2_time_by_completion.png")
plt.close()

# ============================================================================
# TEST 3: TEST IF AVERAGE TIME SPENT EXCEEDS 15 HOURS (One-Sample T-Test)
# ============================================================================

print("\n" + "="*80)
print("TEST 3: TEST IF AVERAGE TIME SPENT EXCEEDS 15 HOURS")
print("One-Sample T-Test")
print("="*80)

hypothesized_mean = 15.0  # From previous study
time_spent_all = df_clean['Time_Spent_Hours']

print(f"\nSample Statistics:")
print(f"  N = {len(time_spent_all)}")
print(f"  Sample Mean = {time_spent_all.mean():.2f} hours")
print(f"  Sample Std Dev = {time_spent_all.std():.2f} hours")
print(f"  Hypothesized Mean (from previous study) = {hypothesized_mean} hours")

# Perform one-sample t-test (one-tailed: greater than)
t_stat_one, p_value_two_tailed = ttest_1samp(time_spent_all, hypothesized_mean)
p_value_one_tailed = p_value_two_tailed / 2 if t_stat_one > 0 else 1 - (p_value_two_tailed / 2)

print(f"\nHypothesis Test:")
print(f"  H0: μ = {hypothesized_mean} (average time spent equals 15 hours)")
print(f"  Ha: μ > {hypothesized_mean} (average time spent exceeds 15 hours)")
print(f"\n  t-statistic = {t_stat_one:.4f}")
print(f"  p-value (one-tailed) = {p_value_one_tailed:.4f}")
print(f"  Significance level α = 0.05")

if p_value_one_tailed < 0.05:
    print(f"\n  Decision: REJECT H0 (p-value = {p_value_one_tailed:.4f} < 0.05)")
    print(f"  Interpretation: The average time spent ({time_spent_all.mean():.2f} hours)")
    print(f"  significantly EXCEEDS 15 hours at the 5% significance level.")
    print(f"  This represents an increase from the previous study's finding.")
else:
    print(f"\n  Decision: FAIL TO REJECT H0 (p-value = {p_value_one_tailed:.4f} ≥ 0.05)")
    print(f"  Interpretation: There is insufficient evidence to conclude that")
    print(f"  the average time spent exceeds 15 hours.")

# Visualization for Test 3
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram with vertical lines
axes[0].hist(time_spent_all, bins=30, edgecolor='black', alpha=0.7, color='skyblue')
axes[0].axvline(time_spent_all.mean(), color='red', linestyle='--', linewidth=2, 
                label=f'Sample Mean = {time_spent_all.mean():.2f}')
axes[0].axvline(hypothesized_mean, color='green', linestyle='--', linewidth=2, 
                label=f'Hypothesized Mean = {hypothesized_mean}')
axes[0].set_xlabel('Time Spent (Hours)', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)
axes[0].set_title('Distribution of Time Spent\n(vs. Hypothesized Mean)', 
                  fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Box plot with reference line
axes[1].boxplot(time_spent_all, vert=True)
axes[1].axhline(hypothesized_mean, color='green', linestyle='--', linewidth=2, 
                label=f'Hypothesized Mean = {hypothesized_mean}')
axes[1].axhline(time_spent_all.mean(), color='red', linestyle='--', linewidth=2, 
                label=f'Sample Mean = {time_spent_all.mean():.2f}')
axes[1].set_ylabel('Time Spent (Hours)', fontsize=12)
axes[1].set_title('Time Spent Distribution\n(Box Plot with Reference)', 
                  fontsize=14, fontweight='bold')
axes[1].legend()
axes[1].set_xticks([])
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('test3_one_sample_ttest.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: test3_one_sample_ttest.png")
plt.close()

# ============================================================================
# TEST 4: COMPARE COURSE TYPE BY COMPLETION STATUS (Chi-Squared Test)
# ============================================================================

print("\n" + "="*80)
print("TEST 4: COMPARE COURSE TYPE BY COMPLETION STATUS")
print("Chi-Squared Test of Independence")
print("="*80)

# Create contingency table
contingency_table = pd.crosstab(df_clean['Course_Type'], df_clean['Completed'])
print(f"\nContingency Table (Observed Frequencies):")
print(contingency_table)

# Add row and column totals for display
contingency_with_totals = contingency_table.copy()
contingency_with_totals['Total'] = contingency_with_totals.sum(axis=1)
contingency_with_totals.loc['Total'] = contingency_with_totals.sum()
print(f"\nContingency Table with Totals:")
print(contingency_with_totals)

# Perform chi-squared test
chi2_stat, p_value_chi2, dof, expected_freq = chi2_contingency(contingency_table)

print(f"\nExpected Frequencies:")
expected_df = pd.DataFrame(expected_freq, 
                           index=contingency_table.index, 
                           columns=contingency_table.columns)
print(expected_df)

print(f"\nHypothesis Test:")
print(f"  H0: Course type and completion status are independent")
print(f"  Ha: Course type and completion status are NOT independent")
print(f"\n  Chi-squared statistic = {chi2_stat:.4f}")
print(f"  Degrees of freedom = {dof}")
print(f"  p-value = {p_value_chi2:.4f}")
print(f"  Significance level α = 0.05")

if p_value_chi2 < 0.05:
    print(f"\n  Decision: REJECT H0 (p-value = {p_value_chi2:.4f} < 0.05)")
    print(f"  Interpretation: Course type and completion status are significantly associated.")
    print(f"  The type of course affects the likelihood of completion.")
else:
    print(f"\n  Decision: FAIL TO REJECT H0 (p-value = {p_value_chi2:.4f} ≥ 0.05)")
    print(f"  Interpretation: Course type and completion status are independent.")
    print(f"  The type of course does NOT significantly affect completion rates.")

# Visualization for Test 4
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Stacked bar chart
contingency_table.plot(kind='bar', stacked=True, ax=axes[0], color=['#ff9999', '#66b3ff'])
axes[0].set_xlabel('Course Type', fontsize=12)
axes[0].set_ylabel('Count', fontsize=12)
axes[0].set_title('Completion Status by Course Type\n(Stacked Bar Chart)', 
                  fontsize=14, fontweight='bold')
axes[0].legend(title='Completed', loc='upper right')
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45, ha='right')
axes[0].grid(True, alpha=0.3, axis='y')

# Grouped bar chart with percentages
contingency_pct = contingency_table.div(contingency_table.sum(axis=1), axis=0) * 100
contingency_pct.plot(kind='bar', ax=axes[1], color=['#ff9999', '#66b3ff'])
axes[1].set_xlabel('Course Type', fontsize=12)
axes[1].set_ylabel('Percentage (%)', fontsize=12)
axes[1].set_title('Completion Rate by Course Type\n(Percentage)', 
                  fontsize=14, fontweight='bold')
axes[1].legend(title='Completed', loc='upper right')
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, ha='right')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('test4_chi_squared.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: test4_chi_squared.png")
plt.close()

# ============================================================================
# TEST 5: COMPARE DEVICE USED BY TIME SPENT (ANOVA)
# ============================================================================

print("\n" + "="*80)
print("TEST 5: COMPARE DEVICE USED BY TIME SPENT")
print("One-Way ANOVA")
print("="*80)

# Separate data by device
time_by_device = {
    'Desktop': df_clean[df_clean['Device_Used'] == 'Desktop']['Time_Spent_Hours'],
    'Mobile': df_clean[df_clean['Device_Used'] == 'Mobile']['Time_Spent_Hours'],
    'Tablet': df_clean[df_clean['Device_Used'] == 'Tablet']['Time_Spent_Hours']
}

print(f"\nDescriptive Statistics by Device:")
for device, times in time_by_device.items():
    print(f"\n{device}:")
    print(f"  N = {len(times)}")
    print(f"  Mean = {times.mean():.2f} hours")
    print(f"  Std Dev = {times.std():.2f} hours")
    print(f"  Min = {times.min():.2f}, Max = {times.max():.2f}")

# Perform one-way ANOVA
f_stat, p_value_anova = f_oneway(time_by_device['Desktop'], 
                                  time_by_device['Mobile'], 
                                  time_by_device['Tablet'])

print(f"\nHypothesis Test:")
print(f"  H0: μ_Desktop = μ_Mobile = μ_Tablet (all devices have equal mean time)")
print(f"  Ha: At least one device has a different mean time spent")
print(f"\n  F-statistic = {f_stat:.4f}")
print(f"  p-value = {p_value_anova:.4f}")
print(f"  Significance level α = 0.05")

if p_value_anova < 0.05:
    print(f"\n  Decision: REJECT H0 (p-value = {p_value_anova:.4f} < 0.05)")
    print(f"  Interpretation: There IS a statistically significant difference in time spent")
    print(f"  across different devices at the 5% significance level.")
    print(f"  Post-hoc tests would be needed to identify which specific devices differ.")
else:
    print(f"\n  Decision: FAIL TO REJECT H0 (p-value = {p_value_anova:.4f} ≥ 0.05)")
    print(f"  Interpretation: There is NO statistically significant difference in time spent")
    print(f"  across different devices. Device type does not affect time spent.")

# Visualization for Test 5
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot by device
df_clean.boxplot(column='Time_Spent_Hours', by='Device_Used', ax=axes[0])
axes[0].set_xlabel('Device Used', fontsize=12)
axes[0].set_ylabel('Time Spent (Hours)', fontsize=12)
axes[0].set_title('Time Spent by Device Type\n(Box Plot)', fontsize=14, fontweight='bold')
axes[0].get_figure().suptitle('')  # Remove default title
axes[0].grid(True, alpha=0.3)

# Violin plot by device
devices_list = ['Desktop', 'Mobile', 'Tablet']
positions = [1, 2, 3]
data_for_violin = [time_by_device[device].values for device in devices_list]
parts = axes[1].violinplot(data_for_violin, positions=positions, showmeans=True, showmedians=True)
axes[1].set_xticks(positions)
axes[1].set_xticklabels(devices_list)
axes[1].set_xlabel('Device Used', fontsize=12)
axes[1].set_ylabel('Time Spent (Hours)', fontsize=12)
axes[1].set_title('Time Spent Distribution by Device\n(Violin Plot)', 
                  fontsize=14, fontweight='bold')
axes[1].grid(True, alpha=0.3)

# Add mean values as text
for i, device in enumerate(devices_list):
    mean_val = time_by_device[device].mean()
    axes[1].text(positions[i], mean_val, f'{mean_val:.1f}', 
                ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.savefig('test5_anova.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: test5_anova.png")
plt.close()

# ============================================================================
# TEST 6: TEST IF BELOW AVERAGE AGE HAVE HIGHER COMPLETION STATUS
# Two-Sample Proportion Z-Test
# ============================================================================

print("\n" + "="*80)
print("TEST 6: TEST IF BELOW AVERAGE AGE HAVE HIGHER COMPLETION RATE")
print("Two-Sample Proportion Z-Test")
print("="*80)

# Calculate average age
average_age = df_clean['Age'].mean()
print(f"\nAverage Age: {average_age:.2f} years")

# Create age groups
df_clean['Age_Group'] = df_clean['Age'].apply(lambda x: 'Below Average' if x < average_age else 'Above Average')

# Calculate completion proportions for each age group
below_avg = df_clean[df_clean['Age_Group'] == 'Below Average']
above_avg = df_clean[df_clean['Age_Group'] == 'Above Average']

n1 = len(below_avg)
n2 = len(above_avg)
x1 = (below_avg['Completed'] == 'Yes').sum()
x2 = (above_avg['Completed'] == 'Yes').sum()
p1 = x1 / n1
p2 = x2 / n2

print(f"\nBelow Average Age Group:")
print(f"  N = {n1}")
print(f"  Completed = {x1}")
print(f"  Completion Rate = {p1:.4f} ({p1*100:.2f}%)")

print(f"\nAbove Average Age Group:")
print(f"  N = {n2}")
print(f"  Completed = {x2}")
print(f"  Completion Rate = {p2:.4f} ({p2*100:.2f}%)")

# Two-sample proportion z-test
p_pooled = (x1 + x2) / (n1 + n2)
se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))
z_stat = (p1 - p2) / se
p_value_z = 1 - stats.norm.cdf(z_stat)  # One-tailed test (greater than)

print(f"\nHypothesis Test:")
print(f"  H0: p_below ≤ p_above (below average age does NOT have higher completion rate)")
print(f"  Ha: p_below > p_above (below average age HAS higher completion rate)")
print(f"\n  Pooled proportion = {p_pooled:.4f}")
print(f"  Standard error = {se:.4f}")
print(f"  z-statistic = {z_stat:.4f}")
print(f"  p-value (one-tailed) = {p_value_z:.4f}")
print(f"  Significance level α = 0.05")

if p_value_z < 0.05:
    print(f"\n  Decision: REJECT H0 (p-value = {p_value_z:.4f} < 0.05)")
    print(f"  Interpretation: Individuals below average age have a significantly HIGHER")
    print(f"  completion rate ({p1*100:.2f}%) compared to those above average age ({p2*100:.2f}%)")
    print(f"  at the 5% significance level.")
else:
    print(f"\n  Decision: FAIL TO REJECT H0 (p-value = {p_value_z:.4f} ≥ 0.05)")
    print(f"  Interpretation: There is insufficient evidence to conclude that")
    print(f"  below average age individuals have a higher completion rate.")

# Visualization for Test 6
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart of completion rates
age_groups = ['Below Average\nAge', 'Above Average\nAge']
completion_rates = [p1 * 100, p2 * 100]
colors = ['#66b3ff', '#ff9999']
bars = axes[0].bar(age_groups, completion_rates, color=colors, edgecolor='black', alpha=0.7)
axes[0].set_ylabel('Completion Rate (%)', fontsize=12)
axes[0].set_xlabel('Age Group', fontsize=12)
axes[0].set_title('Completion Rate by Age Group\n(Bar Chart)', fontsize=14, fontweight='bold')
axes[0].set_ylim([0, 100])
axes[0].grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bar, rate in zip(bars, completion_rates):
    height = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width()/2., height,
                f'{rate:.2f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)

# Stacked bar chart showing counts
age_completion = pd.crosstab(df_clean['Age_Group'], df_clean['Completed'])
age_completion = age_completion.reindex(['Below Average', 'Above Average'])
age_completion.plot(kind='bar', stacked=True, ax=axes[1], color=['#ff9999', '#66b3ff'])
axes[1].set_xlabel('Age Group', fontsize=12)
axes[1].set_ylabel('Count', fontsize=12)
axes[1].set_title('Completion Status by Age Group\n(Stacked Bar Chart)', 
                  fontsize=14, fontweight='bold')
axes[1].legend(title='Completed', loc='upper right')
axes[1].set_xticklabels(['Below Average', 'Above Average'], rotation=45, ha='right')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('test6_proportion_ztest.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: test6_proportion_ztest.png")
plt.close()

# ============================================================================
# SUMMARY REPORT
# ============================================================================

print("\n" + "="*80)
print("SUMMARY OF ALL STATISTICAL TESTS")
print("="*80)

print(f"""
1. Data Cleaning:
   - Original data: {len(df)} rows
   - Negative time values removed: {negative_time_count}
   - Final clean data: {len(df_clean)} rows

2. Time Spent by Completion Status (Two-Sample T-Test):
   - Result: {"FAIL TO REJECT H0" if p_value > 0.05 else "REJECT H0"}
   - p-value: {p_value:.4f}
   - Conclusion: {"No significant difference" if p_value > 0.05 else "Significant difference"}

3. Average Time Exceeds 15 Hours (One-Sample T-Test):
   - Result: {"REJECT H0" if p_value_one_tailed < 0.05 else "FAIL TO REJECT H0"}
   - p-value: {p_value_one_tailed:.4f}
   - Sample mean: {time_spent_all.mean():.2f} hours
   - Conclusion: {"Average significantly exceeds 15 hours" if p_value_one_tailed < 0.05 else "No significant evidence that average exceeds 15 hours"}

4. Course Type and Completion Status (Chi-Squared Test):
   - Result: {"REJECT H0" if p_value_chi2 < 0.05 else "FAIL TO REJECT H0"}
   - p-value: {p_value_chi2:.4f}
   - Conclusion: {"Significant association" if p_value_chi2 < 0.05 else "No significant association"}

5. Device Used and Time Spent (One-Way ANOVA):
   - Result: {"REJECT H0" if p_value_anova < 0.05 else "FAIL TO REJECT H0"}
   - p-value: {p_value_anova:.4f}
   - Conclusion: {"Significant difference across devices" if p_value_anova < 0.05 else "No significant difference across devices"}

6. Below Average Age and Completion Rate (Proportion Z-Test):
   - Result: {"REJECT H0" if p_value_z < 0.05 else "FAIL TO REJECT H0"}
   - p-value: {p_value_z:.4f}
   - Below avg completion rate: {p1*100:.2f}%
   - Above avg completion rate: {p2*100:.2f}%
   - Conclusion: {"Below average age has higher completion rate" if p_value_z < 0.05 else "No significant difference in completion rates"}
""")

print("="*80)
print("ANALYSIS COMPLETE - All plots saved")
print("="*80)
