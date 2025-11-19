# Statistical Tests Justification and Selection

## Overview

This document explains why specific statistical tests were chosen for each research objective and provides detailed justification for their use.

---

## 1. Two-Sample T-Test (Independent Samples)

### **When Used in This Analysis**
**Objective 2:** Compare time spent by completion status

### **What It Tests**
Compares the means of two independent groups to determine if there is a statistically significant difference between them.

### **Why We Used It**

#### **1. Research Question Alignment**
- We needed to compare **two independent groups**: students who completed (Yes) vs. not completed (No)
- We wanted to know if the average **time spent differs** between these groups
- This is a classic two-group comparison scenario

#### **2. Data Characteristics**
- **Dependent variable:** Time_Spent_Hours (continuous, numerical)
- **Independent variable:** Completed (categorical with 2 levels: Yes/No)
- **Independence:** The two groups are independent—each student belongs to only one completion status
- **Sample size:** Large (N = 2,095), providing good statistical power

#### **3. Statistical Assumptions Met**
- ✓ **Continuous outcome:** Time spent is measured in hours (interval scale)
- ✓ **Independent groups:** No student belongs to both groups simultaneously
- ✓ **Approximate normality:** Large sample size (N > 30) satisfies Central Limit Theorem
- ✓ **Homogeneity of variance:** Preliminary tests showed acceptable variance equality

#### **4. Advantages Over Alternatives**
| Alternative | Why Not Used |
|-------------|-------------|
| **Mann-Whitney U Test** | Parametric t-test is more powerful with large samples; data approximately normal |
| **Chi-squared Test** | Only for categorical variables; time spent is continuous |
| **Correlation** | Would only show linear relationship; t-test directly compares means |

### **Hypothesis Structure**
```
H₀: μ_completed = μ_not_completed (no difference in mean time spent)
Hₐ: μ_completed ≠ μ_not_completed (there is a difference)

Formula: t = (x̄₁ - x̄₂) / √[s₁²/n₁ + s₂²/n₂]
```

### **Interpretation Guide**
- If **p-value < 0.05**: Reject H₀ → significant difference exists
- If **p-value ≥ 0.05**: Fail to reject H₀ → no significant difference

### **Our Results**
- **t-statistic = -0.3069**
- **p-value = 0.7589**
- **Decision:** FAIL TO REJECT H₀
- **Conclusion:** No significant difference in time spent between completion groups

---

## 2. One-Sample T-Test

### **When Used in This Analysis**
**Objective 3:** Test if average time spent exceeds 15 hours (benchmark from previous study)

### **What It Tests**
Compares a sample mean against a known/hypothesized population mean to test if there's a significant difference.

### **Why We Used It**

#### **1. Research Question Alignment**
- We had a **specific hypothesized value** (15 hours) from previous research
- We wanted to test if the **current sample mean differs** from this benchmark
- This is one-sample inference—comparing one group to a fixed value

#### **2. Data Characteristics**
- **Sample variable:** Time_Spent_Hours (continuous, numerical)
- **Known/hypothesized value:** μ₀ = 15 hours (from literature)
- **Sample size:** Large (N = 2,095)
- **Single group:** All students measured on same variable

#### **3. Statistical Assumptions Met**
- ✓ **Continuous outcome:** Time spent measured in hours
- ✓ **Independence:** Each observation is independent
- ✓ **Approximate normality:** Large sample size (N > 30) invokes Central Limit Theorem
- ✓ **Random sampling:** Data collected systematically

#### **4. Advantages Over Alternatives**
| Alternative | Why Not Used |
|-------------|-------------|
| **Z-test** | t-test is more conservative with sample variance estimation |
| **Wilcoxon Signed-Rank Test** | Parametric t-test appropriate with large samples |
| **Confidence Interval Only** | t-test provides hypothesis test + formal decision |

### **Hypothesis Structure**
```
H₀: μ = 15 (average time equals benchmark)
Hₐ: μ > 15 (average time exceeds benchmark) [one-tailed]

Formula: t = (x̄ - μ₀) / (s / √n)
Where: x̄ = sample mean, μ₀ = hypothesized mean, s = sample SD, n = sample size
```

### **Interpretation Guide**
- **One-tailed test:** Tests direction (greater than or less than)
- If **p-value < 0.05**: Reject H₀ → sample mean significantly differs from benchmark
- If **p-value ≥ 0.05**: Fail to reject H₀ → insufficient evidence of difference

### **Our Results**
- **Sample Mean = 15.19 hours**
- **Hypothesized Mean = 15.0 hours**
- **t-statistic = 1.7659**
- **p-value (one-tailed) = 0.0388**
- **Decision:** REJECT H₀
- **Conclusion:** Average time spent SIGNIFICANTLY EXCEEDS 15 hours

### **Practical Significance**
The 0.19-hour difference (≈11 minutes) while statistically significant may have modest practical significance due to large sample size. This demonstrates the difference between statistical and practical significance.

---

## 3. Chi-Squared Test of Independence

### **When Used in This Analysis**
**Objective 4:** Compare course type by completion status

### **What It Tests**
Determines whether two categorical variables are independent or associated with each other.

### **Why We Used It**

#### **1. Research Question Alignment**
- We needed to test **association between two categorical variables**
- **Variable 1:** Course_Type (categorical: Business, Creative, Technical)
- **Variable 2:** Completed (categorical: Yes, No)
- We wanted to know if completion rates **differ by course type**

#### **2. Data Characteristics**
- **Both variables are categorical:** No continuous measurements
- **Multiple categories:** Course type has 3 levels; Completion has 2 levels
- **Contingency table:** Data naturally organized in 3 × 2 table
- **Sample size:** Large (N = 2,095), satisfying minimum expected frequencies

#### **3. Statistical Assumptions Met**
- ✓ **Categorical data:** Both variables are categorical/nominal
- ✓ **Independence:** Each student counted once only
- ✓ **Expected frequencies:** All cells have expected frequency ≥ 5
- ✓ **Random sampling:** Data collected systematically

#### **4. Advantages Over Alternatives**
| Alternative | Why Not Used |
|-------------|-------------|
| **Fisher's Exact Test** | Better for small samples; chi-squared appropriate here (large N) |
| **T-test** | Can't use parametric tests on categorical variables |
| **Correlation** | Pearson correlation inappropriate for categorical variables |
| **Proportion Tests** | Chi-squared tests overall association; more powerful than multiple pairwise tests |

### **Hypothesis Structure**
```
H₀: Course type and completion status are independent
Hₐ: Course type and completion status are associated/dependent

Formula: χ² = Σ [(Observed - Expected)² / Expected]
Degrees of freedom = (rows - 1) × (columns - 1) = (3-1)(2-1) = 2
```

### **Contingency Table Setup**
```
                Completed
Course Type     No      Yes     Total
Business        373     346     719
Creative        355     311     666
Technical       361     349     710
Total           1089    1006    2095
```

### **Interpretation Guide**
- **Expected frequencies:** Calculated under assumption of independence
- If **p-value < 0.05**: Reject H₀ → variables are associated
- If **p-value ≥ 0.05**: Fail to reject H₀ → variables are independent

### **Our Results**
- **χ² statistic = 0.8366**
- **Degrees of freedom = 2**
- **p-value = 0.6582**
- **Decision:** FAIL TO REJECT H₀
- **Conclusion:** Course type and completion are independent; type doesn't affect completion rate

### **Effect Size**
- **Cramér's V** (effect size) would be very small, indicating negligible practical association
- Observed and expected frequencies are very similar

---

## 4. One-Way ANOVA (Analysis of Variance)

### **When Used in This Analysis**
**Objective 5:** Compare device used by time spent

### **What It Tests**
Compares means across three or more independent groups to determine if at least one group mean differs significantly from the others.

### **Why We Used It**

#### **1. Research Question Alignment**
- We needed to compare **three independent groups**: Desktop, Mobile, and Tablet
- **Dependent variable:** Time_Spent_Hours (continuous)
- **Independent variable:** Device_Used (categorical with 3+ levels)
- We wanted to test if **time spent differs by device type**

#### **2. Data Characteristics**
- **Continuous outcome:** Time spent (measured in hours)
- **Three independent groups:** Desktop (N=713), Mobile (N=657), Tablet (N=725)
- **Unequal group sizes:** Acceptable for ANOVA
- **Large sample:** Total N = 2,095

#### **3. Statistical Assumptions Met**
- ✓ **Continuous dependent variable:** Time spent is numerical
- ✓ **Independent groups:** No student uses multiple devices simultaneously
- ✓ **Approximate normality:** Large sample size satisfies CLT
- ✓ **Homogeneity of variance:** Similar variances across device groups (all SD ≈ 4.9)
- ✓ **Independence of observations:** Each measurement is independent

#### **4. Why Not Other Tests**

| Alternative | Why Not Used |
|-------------|-------------|
| **Three Separate T-tests** | Multiple comparisons inflate Type I error; ANOVA controls family-wise error |
| **Kruskal-Wallis** | Nonparametric alternative; less powerful with large normal samples |
| **Correlation** | Tests linear relationship; ANOVA directly compares group means |
| **Chi-squared** | Only for categorical outcomes |

### **Hypothesis Structure**
```
H₀: μ_Desktop = μ_Mobile = μ_Tablet (all devices have equal mean time)
Hₐ: At least one device group has a different mean

Formula: F = [MS_Between] / [MS_Within] = [Σn(x̄ᵢ - x̄)²/(k-1)] / [Σ(xᵢⱼ - x̄ᵢ)²/(N-k)]
Where: k = number of groups, N = total sample size
```

### **Why ANOVA With 3+ Groups**

**Problem with multiple t-tests:**
- 1 t-test: α = 0.05 (5% Type I error)
- 3 pairwise t-tests: α ≈ 0.14 (14% combined Type I error)
- ANOVA: α = 0.05 (controls overall error rate)

**ANOVA Solution:**
- Single test comparing all groups simultaneously
- Controls family-wise error rate at α = 0.05
- More powerful than multiple t-tests

### **Interpretation Guide**
- **F-statistic:** Ratio of between-group to within-group variance
- **Large F:** Groups are different (variance between groups > variance within)
- **Small F:** Groups are similar (variance between ≈ variance within)
- If **p-value < 0.05**: Reject H₀ → at least one group differs
- If **p-value ≥ 0.05**: Fail to reject H₀ → no significant differences

### **Our Results**
- **F-statistic = 0.6966**
- **p-value = 0.4984**
- **Decision:** FAIL TO REJECT H₀
- **Conclusion:** No significant difference in time spent across devices

### **Group Means**
- Desktop: 15.17 hours (SD = 4.87)
- Mobile: 15.03 hours (SD = 4.82)
- Tablet: 15.35 hours (SD = 5.08)

All means are very similar, explaining the high p-value.

### **Post-Hoc Testing Note**
Since H₀ was not rejected (p = 0.4984), post-hoc tests (Tukey, Bonferroni) are not needed. We don't have evidence to justify pairwise comparisons.

---

## 5. Two-Sample Proportion Z-Test

### **When Used in This Analysis**
**Objective 6:** Test if below average age has higher completion rate

### **What It Tests**
Compares proportions (percentages) between two independent groups to determine if there's a significant difference.

### **Why We Used It**

#### **1. Research Question Alignment**
- We needed to compare **two independent groups**: Below-average age vs. Above-average age
- **Outcome variable:** Completion status (categorical: Yes/No) → converted to proportion
- We wanted to test if **completion rate differs by age group**
- Age groups are based on median split (below/above average)

#### **2. Data Characteristics**
- **Binary outcome:** Completion (Yes = 1, No = 0)
- **Two independent groups:** Below average age (N=1,039), Above average age (N=1,056)
- **Proportions compared:** p₁ = 48.22%, p₂ = 47.82%
- **Large sample:** Total N = 2,095 (sufficient for normal approximation)

#### **3. Statistical Assumptions Met**
- ✓ **Binary outcome:** Completion is Yes/No
- ✓ **Independent groups:** No person in both groups
- ✓ **Large sample:** N₁ × p₁ = 501 > 5, N₁ × (1-p₁) = 538 > 5 ✓
- ✓ **Large sample:** N₂ × p₂ = 505 > 5, N₂ × (1-p₂) = 551 > 5 ✓
- ✓ **Random sampling:** Data collected systematically

#### **4. Advantages Over Alternatives**
| Alternative | Why Not Used |
|-------------|-------------|
| **Chi-Squared Test** | Also valid; z-test more interpretable for 2 proportions |
| **T-test on Binary Data** | Inappropriate; designed for continuous variables |
| **Fisher's Exact Test** | Better for small samples; z-test appropriate here (large N) |
| **Logistic Regression** | More complex; z-test simpler for single binary predictor |

### **Hypothesis Structure**
```
H₀: p₁ ≤ p₂ (below-average age does NOT have higher completion)
Hₐ: p₁ > p₂ (below-average age HAS higher completion) [one-tailed]

Formula: z = (p₁ - p₂) / √[p̂(1-p̂)(1/n₁ + 1/n₂)]
Where: p̂ = (x₁ + x₂)/(n₁ + n₂) = pooled proportion
```

### **Why One-Tailed Test**
- Directional hypothesis: "higher completion rate" suggests one-tailed
- Tests if one specific group exceeds the other (not just differs)
- More powerful when direction is known a priori

### **Interpretation Guide**
- **z-statistic:** Number of standard errors from zero
- **Large |z|:** Proportions are substantially different
- **Small |z|:** Proportions are similar
- If **p-value < 0.05** (one-tailed): Reject H₀ → significant difference in predicted direction
- If **p-value ≥ 0.05**: Fail to reject H₀ → no significant difference

### **Our Results**
- **Below-average age proportion:** p₁ = 501/1,039 = 0.4822 (48.22%)
- **Above-average age proportion:** p₂ = 505/1,056 = 0.4782 (47.82%)
- **Pooled proportion:** p̂ = 1,006/2,095 = 0.4802
- **Standard error:** SE = 0.0218
- **z-statistic = 0.1821**
- **p-value (one-tailed) = 0.4278**
- **Decision:** FAIL TO REJECT H₀
- **Conclusion:** No significant evidence that below-average age has higher completion rate

### **Effect Size Consideration**
The difference between 48.22% and 47.82% is only 0.4 percentage points:
- **Practical significance:** Nearly identical completion rates
- **Statistical significance:** Small sample difference, high p-value
- **Real-world meaning:** Age-based grouping shows no meaningful effect on completion

---

## Summary Table: Test Selection Decision Tree

| **Scenario** | **Data Type** | **Test Used** | **When to Use** |
|--|--|--|--|
| Compare continuous variable across 2 independent groups | Continuous + Categorical (2 levels) | **Two-Sample T-Test** | Difference between group means |
| Compare continuous variable against known value | Continuous + Known/Hypothesized value | **One-Sample T-Test** | Deviation from benchmark |
| Compare categorical variable across categorical groups | Categorical + Categorical | **Chi-Squared Test** | Association between categories |
| Compare continuous variable across 3+ independent groups | Continuous + Categorical (3+ levels) | **One-Way ANOVA** | Differences among 3+ group means |
| Compare proportions across 2 independent groups | Binary + Categorical (2 levels) | **Two-Sample Proportion Z-Test** | Difference between percentages |

---

## Key Principles in Test Selection

### **1. Match Test to Data Type**
- **Continuous outcome + categorical predictor** → t-test or ANOVA
- **Categorical outcome + categorical predictor** → Chi-squared
- **Binary outcome + categorical predictor** → Proportion z-test

### **2. Account for Sample Size**
- **Small samples (n < 30):** Use t-test or nonparametric alternatives
- **Large samples (n > 30):** Parametric tests are robust (CLT applies)
- **Our study:** N = 2,095 → large sample enables parametric tests

### **3. Number of Groups Matters**
- **2 groups:** Two-sample t-test
- **3+ groups:** ANOVA (not multiple t-tests)
- **Prevents multiple comparison inflation**

### **4. Directional vs. Non-Directional**
- **Two-tailed (non-directional):** Tests if different (≠), uses α/2 in each tail
- **One-tailed (directional):** Tests if greater (>) or less (<), uses full α in one tail
- **Our study:** Used one-tailed for objective 3 and 6 based on theory

### **5. Independence Assumption**
- All tests require independent observations
- No student should appear in multiple groups
- Our data structure satisfied this requirement

---

## Robustness and Sensitivity Checks

### **Tests Performed**
1. **Parametric + Non-parametric:** Compared t-test with Mann-Whitney U
2. **Equal variance assumption:** Welch's t-test verified results
3. **Outlier analysis:** Verified results robust to extreme values
4. **Sample size:** Large N provides statistical power

### **Why Our Choice of Tests Was Robust**
- ✓ Large sample size (N = 2,095)
- ✓ Central Limit Theorem applies → normality assumption reasonable
- ✓ Parametric tests appropriate and powerful
- ✓ Results aligned with non-parametric alternatives
- ✓ Effect sizes consistent with test results

---

## Conclusion

Each statistical test was carefully selected to:
1. **Match the research question** being addressed
2. **Align with data types** being analyzed
3. **Satisfy statistical assumptions** based on sample characteristics
4. **Control for error rates** and multiple comparison issues
5. **Maximize statistical power** for reliable conclusions

The combination of these five tests provides comprehensive coverage of the research objectives, from basic comparisons (t-tests) to complex associations (ANOVA), while maintaining rigorous statistical standards.
