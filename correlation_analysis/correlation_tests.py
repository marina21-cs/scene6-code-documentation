"""
Online Course Completion - Correlation Analysis
Examining relationships between numerical variables
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import pearsonr, spearmanr
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ============================================================================
# DATA LOADING AND PREPARATION
# ============================================================================

print("="*80)
print("CORRELATION ANALYSIS - ONLINE COURSE COMPLETION")
print("="*80)

# Load data
df = pd.read_csv('scenario_6_Online_Course_Completion.xlsx.csv')
print(f"\nOriginal dataset: {len(df)} rows")

# Clean data - remove negative time values
df_clean = df[df['Time_Spent_Hours'] >= 0].copy()
print(f"After removing negative values: {len(df_clean)} rows")

# Convert categorical variables to numerical for correlation analysis
df_clean['Completed_Numeric'] = df_clean['Completed'].map({'No': 0, 'Yes': 1})
df_clean['Course_Type_Business'] = (df_clean['Course_Type'] == 'Business').astype(int)
df_clean['Course_Type_Creative'] = (df_clean['Course_Type'] == 'Creative').astype(int)
df_clean['Course_Type_Technical'] = (df_clean['Course_Type'] == 'Technical').astype(int)
df_clean['Device_Desktop'] = (df_clean['Device_Used'] == 'Desktop').astype(int)
df_clean['Device_Mobile'] = (df_clean['Device_Used'] == 'Mobile').astype(int)
df_clean['Device_Tablet'] = (df_clean['Device_Used'] == 'Tablet').astype(int)

print("\n" + "="*80)
print("NUMERICAL VARIABLES FOR CORRELATION ANALYSIS")
print("="*80)
print("""
Primary Variables:
  - Time_Spent_Hours: Continuous variable (hours spent on course)
  - Age: Continuous variable (student age in years)
  - Completed_Numeric: Binary (0 = No, 1 = Yes)

Categorical Variables (One-Hot Encoded):
  - Course_Type: Business, Creative, Technical
  - Device_Used: Desktop, Mobile, Tablet
""")

# ============================================================================
# CORRELATION TEST 1: TIME SPENT vs AGE (Pearson & Spearman)
# ============================================================================

print("\n" + "="*80)
print("CORRELATION TEST 1: TIME SPENT vs AGE")
print("="*80)

time_spent = df_clean['Time_Spent_Hours']
age = df_clean['Age']

# Pearson correlation (measures linear relationship)
pearson_corr, pearson_pval = pearsonr(time_spent, age)

# Spearman correlation (measures monotonic relationship, robust to outliers)
spearman_corr, spearman_pval = spearmanr(time_spent, age)

print(f"\nPearson Correlation Coefficient:")
print(f"  r = {pearson_corr:.4f}")
print(f"  p-value = {pearson_pval:.4f}")
print(f"  Interpretation: {'Significant' if pearson_pval < 0.05 else 'Not significant'} linear relationship")

print(f"\nSpearman Correlation Coefficient:")
print(f"  ρ (rho) = {spearman_corr:.4f}")
print(f"  p-value = {spearman_pval:.4f}")
print(f"  Interpretation: {'Significant' if spearman_pval < 0.05 else 'Not significant'} monotonic relationship")

# Interpret correlation strength
def interpret_correlation(r):
    r_abs = abs(r)
    if r_abs < 0.1:
        return "negligible"
    elif r_abs < 0.3:
        return "weak"
    elif r_abs < 0.5:
        return "moderate"
    elif r_abs < 0.7:
        return "strong"
    else:
        return "very strong"

print(f"\nCorrelation Strength: {interpret_correlation(pearson_corr)}")
print(f"Direction: {'Positive' if pearson_corr > 0 else 'Negative'}")

if pearson_pval < 0.05:
    print(f"\n✓ There IS a statistically significant correlation between time spent and age.")
    if pearson_corr > 0:
        print(f"  As age increases, time spent tends to increase slightly.")
    else:
        print(f"  As age increases, time spent tends to decrease slightly.")
else:
    print(f"\n✗ There is NO statistically significant correlation between time spent and age.")
    print(f"  Time spent on the course is independent of student age.")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Scatter plot with regression line
axes[0].scatter(age, time_spent, alpha=0.4, s=20, color='steelblue')
z = np.polyfit(age, time_spent, 1)
p = np.poly1d(z)
axes[0].plot(age, p(age), "r--", linewidth=2, label=f'y = {z[0]:.3f}x + {z[1]:.2f}')
axes[0].set_xlabel('Age (years)', fontsize=12)
axes[0].set_ylabel('Time Spent (hours)', fontsize=12)
axes[0].set_title(f'Time Spent vs Age\nPearson r = {pearson_corr:.4f}, p = {pearson_pval:.4f}', 
                  fontsize=14, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Hexbin plot for density
hexbin = axes[1].hexbin(age, time_spent, gridsize=25, cmap='YlOrRd', mincnt=1)
axes[1].set_xlabel('Age (years)', fontsize=12)
axes[1].set_ylabel('Time Spent (hours)', fontsize=12)
axes[1].set_title('Time Spent vs Age\n(Density Plot)', fontsize=14, fontweight='bold')
plt.colorbar(hexbin, ax=axes[1], label='Count')

plt.tight_layout()
plt.savefig('correlation_analysis/corr1_time_vs_age.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: correlation_analysis/corr1_time_vs_age.png")
plt.close()

# ============================================================================
# CORRELATION TEST 2: TIME SPENT vs COMPLETION STATUS
# ============================================================================

print("\n" + "="*80)
print("CORRELATION TEST 2: TIME SPENT vs COMPLETION STATUS")
print("="*80)

completed_numeric = df_clean['Completed_Numeric']

# Point-biserial correlation (special case of Pearson for continuous vs binary)
pearson_corr_comp, pearson_pval_comp = pearsonr(time_spent, completed_numeric)

# Spearman correlation
spearman_corr_comp, spearman_pval_comp = spearmanr(time_spent, completed_numeric)

print(f"\nPoint-Biserial Correlation (Pearson for binary):")
print(f"  r = {pearson_corr_comp:.4f}")
print(f"  p-value = {pearson_pval_comp:.4f}")
print(f"  Interpretation: {'Significant' if pearson_pval_comp < 0.05 else 'Not significant'} relationship")

print(f"\nSpearman Correlation:")
print(f"  ρ (rho) = {spearman_corr_comp:.4f}")
print(f"  p-value = {spearman_pval_comp:.4f}")

print(f"\nCorrelation Strength: {interpret_correlation(pearson_corr_comp)}")
print(f"Direction: {'Positive' if pearson_corr_comp > 0 else 'Negative'}")

if pearson_pval_comp < 0.05:
    print(f"\n✓ There IS a statistically significant correlation between time spent and completion.")
    if pearson_corr_comp > 0:
        print(f"  Higher time spent is associated with higher completion rates.")
    else:
        print(f"  Higher time spent is associated with lower completion rates.")
else:
    print(f"\n✗ There is NO statistically significant correlation between time spent and completion.")
    print(f"  Time spent does not predict course completion status.")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot
df_clean.boxplot(column='Time_Spent_Hours', by='Completed', ax=axes[0])
axes[0].set_xlabel('Completion Status', fontsize=12)
axes[0].set_ylabel('Time Spent (hours)', fontsize=12)
axes[0].set_title(f'Time Spent vs Completion\nPoint-Biserial r = {pearson_corr_comp:.4f}, p = {pearson_pval_comp:.4f}', 
                  fontsize=14, fontweight='bold')
axes[0].get_figure().suptitle('')

# Violin plot with points
parts = axes[1].violinplot([df_clean[df_clean['Completed']=='No']['Time_Spent_Hours'],
                            df_clean[df_clean['Completed']=='Yes']['Time_Spent_Hours']], 
                           positions=[0, 1], showmeans=True, showmedians=True)
axes[1].set_xticks([0, 1])
axes[1].set_xticklabels(['Not Completed', 'Completed'])
axes[1].set_ylabel('Time Spent (hours)', fontsize=12)
axes[1].set_xlabel('Completion Status', fontsize=12)
axes[1].set_title('Time Spent Distribution by Completion', fontsize=14, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('correlation_analysis/corr2_time_vs_completion.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: correlation_analysis/corr2_time_vs_completion.png")
plt.close()

# ============================================================================
# CORRELATION TEST 3: AGE vs COMPLETION STATUS
# ============================================================================

print("\n" + "="*80)
print("CORRELATION TEST 3: AGE vs COMPLETION STATUS")
print("="*80)

# Point-biserial correlation
pearson_corr_age, pearson_pval_age = pearsonr(age, completed_numeric)
spearman_corr_age, spearman_pval_age = spearmanr(age, completed_numeric)

print(f"\nPoint-Biserial Correlation (Pearson for binary):")
print(f"  r = {pearson_corr_age:.4f}")
print(f"  p-value = {pearson_pval_age:.4f}")
print(f"  Interpretation: {'Significant' if pearson_pval_age < 0.05 else 'Not significant'} relationship")

print(f"\nSpearman Correlation:")
print(f"  ρ (rho) = {spearman_corr_age:.4f}")
print(f"  p-value = {spearman_pval_age:.4f}")

print(f"\nCorrelation Strength: {interpret_correlation(pearson_corr_age)}")
print(f"Direction: {'Positive' if pearson_corr_age > 0 else 'Negative'}")

if pearson_pval_age < 0.05:
    print(f"\n✓ There IS a statistically significant correlation between age and completion.")
    if pearson_corr_age > 0:
        print(f"  Older students tend to have higher completion rates.")
    else:
        print(f"  Younger students tend to have higher completion rates.")
else:
    print(f"\n✗ There is NO statistically significant correlation between age and completion.")
    print(f"  Age does not predict course completion status.")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot
df_clean.boxplot(column='Age', by='Completed', ax=axes[0])
axes[0].set_xlabel('Completion Status', fontsize=12)
axes[0].set_ylabel('Age (years)', fontsize=12)
axes[0].set_title(f'Age vs Completion\nPoint-Biserial r = {pearson_corr_age:.4f}, p = {pearson_pval_age:.4f}', 
                  fontsize=14, fontweight='bold')
axes[0].get_figure().suptitle('')

# Histogram by completion status
df_clean[df_clean['Completed']=='No']['Age'].hist(bins=20, alpha=0.6, label='Not Completed', 
                                                    color='#ff9999', ax=axes[1])
df_clean[df_clean['Completed']=='Yes']['Age'].hist(bins=20, alpha=0.6, label='Completed', 
                                                     color='#66b3ff', ax=axes[1])
axes[1].set_xlabel('Age (years)', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)
axes[1].set_title('Age Distribution by Completion Status', fontsize=14, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('correlation_analysis/corr3_age_vs_completion.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: correlation_analysis/corr3_age_vs_completion.png")
plt.close()

# ============================================================================
# COMPREHENSIVE CORRELATION MATRIX
# ============================================================================

print("\n" + "="*80)
print("COMPREHENSIVE CORRELATION MATRIX")
print("="*80)

# Select numerical variables for correlation matrix
corr_vars = ['Time_Spent_Hours', 'Age', 'Completed_Numeric', 
             'Course_Type_Business', 'Course_Type_Creative', 'Course_Type_Technical',
             'Device_Desktop', 'Device_Mobile', 'Device_Tablet']

corr_matrix = df_clean[corr_vars].corr()

print("\nPearson Correlation Matrix:")
print(corr_matrix.round(4))

# Visualization - Correlation Heatmap
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Full heatmap
sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='coolwarm', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=axes[0],
            vmin=-1, vmax=1)
axes[0].set_title('Correlation Matrix - All Variables\n(Pearson Correlation)', 
                  fontsize=14, fontweight='bold')

# Focus on main variables
main_vars = ['Time_Spent_Hours', 'Age', 'Completed_Numeric']
corr_matrix_main = df_clean[main_vars].corr()
sns.heatmap(corr_matrix_main, annot=True, fmt='.4f', cmap='coolwarm', center=0, 
            square=True, linewidths=2, cbar_kws={"shrink": 0.8}, ax=axes[1],
            vmin=-1, vmax=1, annot_kws={'size': 14})
axes[1].set_title('Correlation Matrix - Main Variables\n(Time, Age, Completion)', 
                  fontsize=14, fontweight='bold')
axes[1].set_xticklabels(['Time Spent', 'Age', 'Completed'], rotation=45, ha='right')
axes[1].set_yticklabels(['Time Spent', 'Age', 'Completed'], rotation=0)

plt.tight_layout()
plt.savefig('correlation_analysis/correlation_matrix.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: correlation_analysis/correlation_matrix.png")
plt.close()

# ============================================================================
# PAIRWISE CORRELATION PLOT
# ============================================================================

print("\n" + "="*80)
print("PAIRWISE RELATIONSHIPS VISUALIZATION")
print("="*80)

# Create pairplot for main numerical variables
pairplot_data = df_clean[['Time_Spent_Hours', 'Age', 'Completed']].copy()
pairplot_data.columns = ['Time Spent (hrs)', 'Age (years)', 'Completed']

g = sns.pairplot(pairplot_data, hue='Completed', palette={'No': '#ff9999', 'Yes': '#66b3ff'},
                 diag_kind='kde', plot_kws={'alpha': 0.6, 's': 20}, 
                 diag_kws={'shade': True, 'alpha': 0.6})
g.fig.suptitle('Pairwise Relationships - Time, Age, and Completion', 
               y=1.02, fontsize=16, fontweight='bold')
plt.savefig('correlation_analysis/pairplot.png', dpi=300, bbox_inches='tight')
print(f"\n  Plot saved: correlation_analysis/pairplot.png")
plt.close()

# ============================================================================
# SUMMARY REPORT
# ============================================================================

print("\n" + "="*80)
print("CORRELATION ANALYSIS SUMMARY")
print("="*80)

print(f"""
1. TIME SPENT vs AGE:
   Pearson r = {pearson_corr:.4f} (p = {pearson_pval:.4f})
   Spearman ρ = {spearman_corr:.4f} (p = {spearman_pval:.4f})
   Result: {'SIGNIFICANT' if pearson_pval < 0.05 else 'NOT SIGNIFICANT'}
   Strength: {interpret_correlation(pearson_corr).upper()}
   
2. TIME SPENT vs COMPLETION:
   Point-Biserial r = {pearson_corr_comp:.4f} (p = {pearson_pval_comp:.4f})
   Spearman ρ = {spearman_corr_comp:.4f} (p = {spearman_pval_comp:.4f})
   Result: {'SIGNIFICANT' if pearson_pval_comp < 0.05 else 'NOT SIGNIFICANT'}
   Strength: {interpret_correlation(pearson_corr_comp).upper()}
   
3. AGE vs COMPLETION:
   Point-Biserial r = {pearson_corr_age:.4f} (p = {pearson_pval_age:.4f})
   Spearman ρ = {spearman_corr_age:.4f} (p = {spearman_pval_age:.4f})
   Result: {'SIGNIFICANT' if pearson_pval_age < 0.05 else 'NOT SIGNIFICANT'}
   Strength: {interpret_correlation(pearson_corr_age).upper()}

KEY INSIGHTS:
- The variables show generally weak correlations with each other
- Course completion appears to be influenced by factors not measured in this dataset
- Time spent, age, and device type have minimal correlation with completion
- This supports the hypothesis testing results showing no significant relationships
""")

print("="*80)
print("CORRELATION ANALYSIS COMPLETE - All plots saved in correlation_analysis/")
print("="*80)
