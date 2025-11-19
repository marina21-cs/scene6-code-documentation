# Correlation Analysis Summary

## Overview
This analysis examines the relationships between numerical variables in the online course completion dataset using Pearson and Spearman correlation coefficients.

---

## Correlation Tests Performed

### Test 1: Time Spent vs Age
**Methods Used:**
- Pearson Correlation (linear relationship)
- Spearman Correlation (monotonic relationship)

**Results:**
- **Pearson r = -0.0402** (p = 0.0660)
- **Spearman ρ = -0.0388** (p = 0.0760)
- **Significance:** NOT SIGNIFICANT (p > 0.05)
- **Strength:** NEGLIGIBLE
- **Direction:** Negative

**Interpretation:**
There is NO statistically significant correlation between time spent and age. The negligible correlation coefficient (-0.04) indicates that student age does not predict how much time they spend on the course. Both younger and older students spend similar amounts of time on course activities.

---

### Test 2: Time Spent vs Completion Status
**Methods Used:**
- Point-Biserial Correlation (Pearson for continuous vs binary)
- Spearman Correlation

**Results:**
- **Point-Biserial r = -0.0067** (p = 0.7589)
- **Spearman ρ = -0.0075** (p = 0.7308)
- **Significance:** NOT SIGNIFICANT (p > 0.05)
- **Strength:** NEGLIGIBLE
- **Direction:** Negative

**Interpretation:**
There is NO statistically significant correlation between time spent and course completion. The near-zero correlation (-0.007) indicates that students who complete the course spend approximately the same amount of time as those who don't complete it. Time investment alone does not predict completion success.

---

### Test 3: Age vs Completion Status
**Methods Used:**
- Point-Biserial Correlation
- Spearman Correlation

**Results:**
- **Point-Biserial r = -0.0018** (p = 0.9345)
- **Spearman ρ = -0.0023** (p = 0.9173)
- **Significance:** NOT SIGNIFICANT (p > 0.05)
- **Strength:** NEGLIGIBLE
- **Direction:** Negative

**Interpretation:**
There is NO statistically significant correlation between age and completion status. The near-zero correlation (-0.002) indicates that age is completely independent of course completion. Students of all ages have similar completion rates.

---

## Correlation Matrix Analysis

### Main Variables Correlation Summary

|                    | Time Spent | Age     | Completion |
|--------------------|-----------|---------|------------|
| **Time Spent**     | 1.0000    | -0.0402 | -0.0067    |
| **Age**            | -0.0402   | 1.0000  | -0.0018    |
| **Completion**     | -0.0067   | -0.0018 | 1.0000     |

### Key Observations:
1. All correlation coefficients between variables are very close to zero
2. No multicollinearity issues present
3. Variables are essentially independent of each other

### Categorical Variables (One-Hot Encoded):

**Course Type Correlations:**
- Business, Creative, and Technical course types show negligible correlations with Time Spent, Age, and Completion
- No course type shows a preference or disadvantage

**Device Type Correlations:**
- Desktop, Mobile, and Tablet devices show negligible correlations with Time Spent, Age, and Completion
- Note: Strong negative correlations between device types (-0.48 to -0.52) are expected due to one-hot encoding (mutually exclusive categories)

---

## Correlation Strength Interpretation Guide

| Coefficient (|r|) | Strength       |
|---------------|----------------|
| 0.0 - 0.1     | Negligible     |
| 0.1 - 0.3     | Weak           |
| 0.3 - 0.5     | Moderate       |
| 0.5 - 0.7     | Strong         |
| 0.7 - 1.0     | Very Strong    |

**All observed correlations in this dataset fall in the NEGLIGIBLE range.**

---

## Visual Outputs Generated

1. **corr1_time_vs_age.png**
   - Scatter plot with regression line
   - Hexbin density plot

2. **corr2_time_vs_completion.png**
   - Box plot comparing time by completion status
   - Violin plot showing distributions

3. **corr3_age_vs_completion.png**
   - Box plot comparing age by completion status
   - Histogram overlays by completion group

4. **correlation_matrix.png**
   - Full correlation heatmap (all variables)
   - Focused heatmap (main variables only)

5. **pairplot.png**
   - Comprehensive pairwise relationships
   - Color-coded by completion status
   - Includes scatter plots and KDE distributions

---

## Key Findings

### 1. Independence of Variables
All measured variables (Time Spent, Age, Course Type, Device Used) show negligible correlations with each other and with the completion outcome. This suggests:
- These variables operate independently
- Completion is not predicted by any single measured variable
- Other unmeasured factors likely drive completion

### 2. Consistency with Hypothesis Tests
These correlation results align perfectly with the hypothesis testing results:
- Two-sample t-test showed no difference in time spent by completion
- Chi-squared test showed course type is independent of completion
- ANOVA showed no difference in time spent across devices
- Proportion z-test showed age doesn't affect completion rate

### 3. Practical Implications
Since none of the measured variables correlate with completion:
- **Not useful for prediction:** These variables alone cannot predict who will complete the course
- **Equal accessibility:** The course is equally accessible across all age groups, device types, and course types
- **Hidden factors:** Success depends on unmeasured factors such as:
  - Student motivation and goals
  - Prior knowledge and skills
  - External life circumstances
  - Course quality and engagement
  - Support systems availability

### 4. Statistical Robustness
- Large sample size (N = 2,095) provides reliable estimates
- Both parametric (Pearson) and non-parametric (Spearman) methods agree
- Consistent negligible correlations across all variable pairs

---

## Recommendations

1. **Data Collection:** Consider measuring additional variables that might predict completion:
   - Prior experience/education
   - Motivation level
   - Employment status
   - Learning goals
   - Engagement metrics (logins, quiz attempts, forum participation)

2. **Feature Engineering:** Create new derived variables:
   - Time spent per week (rate of progress)
   - Completion velocity
   - Interaction patterns

3. **Qualitative Research:** Conduct surveys or interviews to understand:
   - Why students complete or don't complete courses
   - Barriers to completion
   - Success factors not captured in quantitative data

4. **Model Development:** Since linear correlations are negligible:
   - Consider non-linear relationships
   - Explore interaction effects between variables
   - Use machine learning for pattern discovery

---

## Statistical Methods Summary

| Test | Purpose | When to Use |
|------|---------|-------------|
| **Pearson Correlation** | Measures linear relationship | Both variables continuous, normally distributed |
| **Spearman Correlation** | Measures monotonic relationship | Ordinal data or non-normal distributions |
| **Point-Biserial Correlation** | Special case of Pearson | One continuous, one binary variable |

**Significance Level:** α = 0.05 used for all tests

---

## Conclusion

The correlation analysis reveals that Time Spent, Age, Course Type, and Device Used have **negligible correlations** with course completion. All correlation coefficients are very close to zero and statistically non-significant. This indicates that:

1. ✗ Time spent does not predict completion
2. ✗ Age does not predict completion  
3. ✗ Variables are independent of each other
4. ✓ Course is equally accessible across demographics
5. ✓ Results consistent with hypothesis testing

**Bottom Line:** Course completion is driven by factors beyond those measured in this dataset. Future research should focus on identifying and measuring the hidden variables that truly influence student success.
