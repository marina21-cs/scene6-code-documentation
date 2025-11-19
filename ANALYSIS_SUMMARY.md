# Online Course Completion - Statistical Analysis Summary

## Data Cleaning
- **Original dataset**: 2,100 rows
- **Negative time values removed**: 5 rows
- **Final clean dataset**: 2,095 rows

---

## Test Results Summary

### Test 2: Compare Time Spent by Completion Status (Two-Sample T-Test)
**Hypothesis:**
- H₀: μ_completed = μ_not_completed (no difference in mean time spent)
- Hₐ: μ_completed ≠ μ_not_completed (there is a difference)

**Results:**
- Completed: Mean = 15.16 hours (N = 1,006)
- Not Completed: Mean = 15.22 hours (N = 1,089)
- t-statistic = -0.3069
- **p-value = 0.7589**

**Decision:** ✅ **FAIL TO REJECT H₀**

**Interpretation:** There is NO statistically significant difference in time spent between students who completed the course and those who did not. This suggests that completion is not driven by the amount of time spent on the course.

---

### Test 3: Test if Average Time Spent Exceeds 15 Hours (One-Sample T-Test)
**Hypothesis:**
- H₀: μ = 15.0 hours (average equals the previous study's finding)
- Hₐ: μ > 15.0 hours (average exceeds 15 hours)

**Results:**
- Sample Mean = 15.19 hours (N = 2,095)
- Hypothesized Mean = 15.0 hours (from previous study)
- t-statistic = 1.7659
- **p-value (one-tailed) = 0.0388**

**Decision:** ❌ **REJECT H₀**

**Interpretation:** The average time spent (15.19 hours) significantly EXCEEDS the 15 hours reported in the previous study at the 5% significance level. This represents a statistically significant increase in course engagement time compared to historical data.

---

### Test 4: Compare Course Type by Completion Status (Chi-Squared Test)
**Hypothesis:**
- H₀: Course type and completion status are independent
- Hₐ: Course type and completion status are NOT independent

**Results:**
- Chi-squared statistic = 0.8366
- Degrees of freedom = 2
- **p-value = 0.6582**

**Observed Frequencies:**
| Course Type | Not Completed | Completed | Total |
|-------------|---------------|-----------|-------|
| Business    | 373           | 346       | 719   |
| Creative    | 355           | 311       | 666   |
| Technical   | 361           | 349       | 710   |

**Decision:** ✅ **FAIL TO REJECT H₀**

**Interpretation:** Course type and completion status are independent. The type of course (Business, Creative, or Technical) does NOT significantly affect whether students complete the course. All course types have similar completion rates (~48%).

---

### Test 5: Compare Device Used by Time Spent (One-Way ANOVA)
**Hypothesis:**
- H₀: μ_Desktop = μ_Mobile = μ_Tablet (all devices have equal mean time)
- Hₐ: At least one device has a different mean time spent

**Results:**
- Desktop: Mean = 15.17 hours (N = 713)
- Mobile: Mean = 15.03 hours (N = 657)
- Tablet: Mean = 15.35 hours (N = 725)
- F-statistic = 0.6966
- **p-value = 0.4984**

**Decision:** ✅ **FAIL TO REJECT H₀**

**Interpretation:** There is NO statistically significant difference in time spent across different devices. Students spend similar amounts of time on the course regardless of whether they use Desktop, Mobile, or Tablet devices. Device choice does not impact engagement time.

---

### Test 6: Test if Below Average Age Has Higher Completion Rate (Two-Sample Proportion Z-Test)
**Hypothesis:**
- H₀: p_below ≤ p_above (below average age does NOT have higher completion rate)
- Hₐ: p_below > p_above (below average age HAS higher completion rate)

**Results:**
- Average Age = 38.61 years
- Below Average Age: Completion Rate = 48.22% (501/1,039)
- Above Average Age: Completion Rate = 47.82% (505/1,056)
- z-statistic = 0.1821
- **p-value (one-tailed) = 0.4278**

**Decision:** ✅ **FAIL TO REJECT H₀**

**Interpretation:** There is insufficient evidence to conclude that students below average age have a higher completion rate. Age does not appear to be a significant factor in course completion, with both age groups showing nearly identical completion rates (~48%).

---

## Key Findings

### Statistically Significant Results:
1. **Test 3 Only**: Average time spent (15.19 hours) significantly exceeds the 15-hour benchmark from previous research.

### Non-Significant Results:
2. **Test 2**: Completion status does not differ by time spent
3. **Test 4**: Course type is independent of completion status
4. **Test 5**: Device type does not affect time spent
5. **Test 6**: Age group does not affect completion rate

---

## Practical Implications

1. **Time Investment**: Students are spending more time on courses than in previous studies, suggesting increased engagement or possibly more complex content.

2. **Completion Factors**: Since time spent, course type, device used, and age don't significantly predict completion, other factors (not measured in this dataset) likely drive course completion, such as:
   - Course quality/design
   - Student motivation
   - Support resources
   - Personal circumstances

3. **Universal Appeal**: The lack of differences across course types, devices, and age groups suggests the courses are equally accessible and engaging across different demographics and platforms.

4. **Focus Areas**: To improve completion rates, consider factors beyond time, device, age, or course type - such as learning support, content difficulty, feedback mechanisms, or student engagement strategies.

---

## Visualizations Generated

1. `test2_time_by_completion.png` - Box and violin plots comparing time spent by completion status
2. `test3_one_sample_ttest.png` - Histogram and box plot showing time distribution vs. 15-hour benchmark
3. `test4_chi_squared.png` - Stacked and percentage bar charts of course type by completion
4. `test5_anova.png` - Box and violin plots comparing time spent across devices
5. `test6_proportion_ztest.png` - Bar charts showing completion rates by age group

---

## Statistical Notes

- **Significance level (α)**: 0.05 used for all tests
- **Data quality**: 5 negative time values were removed (0.24% of data)
- **Sample size**: Large sample (N = 2,095) provides good statistical power
- **Test assumptions**: Appropriate tests selected based on data types and research questions
