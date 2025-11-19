# Correlation Analysis

This folder contains comprehensive correlation analysis for the Online Course Completion dataset.

## Files

### Scripts
- **correlation_tests.py** - Python script performing all correlation tests

### Documentation
- **CORRELATION_SUMMARY.md** - Detailed summary with interpretations and insights

### Visualizations
- **corr1_time_vs_age.png** - Time Spent vs Age (scatter plot + hexbin)
- **corr2_time_vs_completion.png** - Time Spent vs Completion (box + violin plots)
- **corr3_age_vs_completion.png** - Age vs Completion (box plot + histograms)
- **correlation_matrix.png** - Comprehensive correlation heatmaps
- **pairplot.png** - Pairwise relationships with distributions

## Quick Results

All correlations are **NEGLIGIBLE** and **NOT SIGNIFICANT**:

| Variables | Pearson r | p-value | Significance |
|-----------|-----------|---------|--------------|
| Time Spent vs Age | -0.0402 | 0.0660 | ✗ No |
| Time Spent vs Completion | -0.0067 | 0.7589 | ✗ No |
| Age vs Completion | -0.0018 | 0.9345 | ✗ No |

## Run the Analysis

```bash
python correlation_analysis/correlation_tests.py
```

## Key Insight

None of the measured variables show meaningful correlations with course completion, suggesting that success is driven by factors not captured in this dataset.
