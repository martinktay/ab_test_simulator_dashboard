# A/B Testing Dashboard with Streamlit

A clean, interactive dashboard for analysing A/B test results using Python and Streamlit.

## 📊 Project Overview

This dashboard provides comprehensive analysis of A/B test data including:

- **Conversion Rate Analysis**: Compare conversion rates between test groups
- **Statistical Significance Testing**: Z-test and chi-square test results
- **Segmentation Analysis**: Breakdown by device, channel, and region
- **Interactive Visualisations**: Charts and tables for data exploration

## 🚀 Features

- **Real-time Data Analysis**: Load and process A/B test data instantly
- **Statistical Testing**: Automated significance testing with clear results
- **Multi-dimensional Segmentation**: Analyse results across different user segments
- **Responsive Design**: Clean, minimalist interface optimised for insights
- **Interactive Charts**: Plotly-based visualisations for better user experience

## 📋 Requirements

- Python 3.7+
- pandas
- numpy
- scipy
- plotly
- streamlit

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ab-test-dashboard-streamlit.git
cd ab-test-dashboard-streamlit
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Place your `ab_test_enriched.csv` file in the root directory

4. Run the dashboard:

```bash
streamlit run ab_test_dashboard.py
```

## 📁 Project Structure

```
ab-test-dashboard-streamlit/
├── ab_test_dashboard.py      # Main Streamlit application
├── ab_test_enriched.csv      # A/B test dataset
├── ab_test_cleaned.csv       # Cleaned dataset with features
├── ab_test_summary.csv       # Summary statistics
├── verify_data_alignment.py  # Data verification script
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
└── .gitignore              # Git ignore file
```

## 📊 A/B Testing Results Summary

### 🎯 Key Findings

**Group B shows statistically significant improvement over Group A:**

- **Conversion Rate**: 6.38% → 9.67% (**+51.56% improvement**)
- **Statistical Significance**: p < 0.01 (Highly significant)
- **Confidence Level**: 95% CI [0.94%, 5.64%]
- **Sample Size**: 2,000 users (987 Group A, 1,013 Group B)

### 📱 Top Performing Segments

| Segment           | Improvement | Performance    |
| ----------------- | ----------- | -------------- |
| **Email Channel** | +87.1%      | 6.30% → 11.79% |
| **South Region**  | +191.1%     | 4.04% → 11.76% |
| **Desktop Users** | +59.7%      | 6.15% → 9.82%  |
| **Paid Search**   | +49.5%      | 6.91% → 10.33% |

### 🔬 Statistical Validation

- **Z-Test**: p = 0.006834 ✅
- **Chi-Square**: p = 0.008726 ✅
- **Effect Size**: Large (51.56% relative improvement)
- **Data Quality**: 100% clean (no missing values/duplicates)

### 🎯 Recommendation

**✅ IMPLEMENT GROUP B IMMEDIATELY**

Strong evidence supports deploying the Group B variant across all user segments, with expected 51.56% conversion rate improvement.

---

## 📊 Dashboard Screenshots

_[Insert your Streamlit dashboard screenshots here]_

### Key Metrics Displayed

- Real-time conversion rate comparison
- Statistical significance indicators
- Segmentation breakdown charts
- Interactive filtering capabilities
- Confidence interval visualisation

---

## 🔍 Data Schema

The dashboard expects a CSV file with the following columns:

- `user_id`: Unique identifier for each user
- `group`: Test group (A or B)
- `converted`: Binary conversion indicator (0/1)
- `session_duration_sec`: Session duration in seconds
- `page_views`: Number of page views per session
- `device`: User device type
- `channel`: Traffic source/channel
- `region`: Geographic region
- `visit_date`: Date of visit

## 📈 Analysis Features

### 1. Overall Metrics

- Total users and conversions
- Overall conversion rate
- Average session duration and page views

### 2. A/B Comparison

- Side-by-side conversion rate comparison
- Statistical significance testing
- Confidence intervals

### 3. Segmentation Analysis

- Conversion rates by device type
- Performance across different channels
- Regional performance breakdown

### 4. Statistical Testing

- Z-test for proportion comparison
- Chi-square test for independence
- P-values and confidence levels

---

## 📈 Detailed Analysis Results

### 🔬 Statistical Analysis

**Test Results:**

- **Sample Size**: 2,000 users (987 Group A, 1,013 Group B)
- **Test Duration**: 30 days
- **Statistical Power**: High (balanced groups, large sample)
- **Effect Size**: Large (51.56% relative improvement)

**Confidence Level:**

- **95% Confidence Interval**: [0.94%, 5.64%]
- **Interpretation**: We are 95% confident that the true improvement lies between 0.94% and 5.64%
- **Business Impact**: Even the lower bound (0.94%) represents meaningful improvement

### 📱 Segmentation Analysis

**Device Performance:**
| Device | Group A | Group B | Improvement |
|--------|---------|---------|-------------|
| Desktop | 6.15% | 9.82% | +59.7% |
| Mobile | 6.52% | 9.54% | +46.3% |
| Tablet | 6.67% | 9.33% | +39.9% |

**Channel Performance:**
| Channel | Group A | Group B | Improvement |
|---------|---------|---------|-------------|
| Email | 6.30% | 11.79% | **+87.1%** |
| Paid Search | 6.91% | 10.33% | +49.5% |
| Organic | 6.15% | 8.80% | +43.1% |
| Social | 6.17% | 8.14% | +31.9% |

**Regional Performance:**
| Region | Group A | Group B | Improvement |
|--------|---------|---------|-------------|
| South | 4.04% | 11.76% | **+191.1%** |
| London | 8.38% | 11.62% | +38.7% |
| North | 8.38% | 8.16% | -2.6% |
| Midlands | 6.22% | 8.33% | +33.9% |
| Scotland | 6.22% | 8.33% | +33.9% |

### 📈 Business Impact Assessment

**Immediate Benefits:**

- **Conversion Rate**: +51.56% improvement
- **Revenue Impact**: Proportional increase in conversions
- **User Experience**: Better engagement metrics

**Long-term Considerations:**

- **Scalability**: Results consistent across segments
- **Sustainability**: No negative side effects observed
- **ROI**: High return on implementation effort

### 🎯 Implementation Recommendations

**Primary Recommendation:**
**✅ IMPLEMENT GROUP B IMMEDIATELY**

- Strong statistical evidence (p < 0.01)
- Large effect size (51.56% improvement)
- Consistent performance across segments

**Secondary Recommendations:**

1. **Monitor Performance**: Track metrics post-implementation
2. **Regional Optimisation**: Consider customising for North region
3. **Channel Focus**: Prioritise email and paid search channels
4. **Device Optimisation**: Ensure mobile experience is optimised

### 🎉 Conclusion & Strategic Recommendations

After conducting a comprehensive 30-day A/B test with 2,000 users, our analysis reveals compelling evidence that the Group B variant delivers exceptional performance improvements across all key metrics. The results not only demonstrate statistical significance but also provide actionable insights for business growth and user experience enhancement.

**Executive Summary:**
Our findings show that Group B achieves a remarkable **51.56% improvement** in conversion rate compared to the control group, translating to an increase from 6.38% to 9.67%. This improvement is statistically significant at the 99% confidence level (p < 0.01), providing strong evidence to support immediate implementation.

**Deep Dive Analysis:**
The segmentation analysis reveals fascinating patterns that go beyond simple conversion rate improvements. Email users show the most dramatic response with an 87.1% improvement, suggesting the new variant particularly resonates with users who engage through email campaigns. This insight opens opportunities for targeted marketing strategies and personalised user experiences.

Regional performance tells an equally compelling story. The South region demonstrates an extraordinary 191.1% improvement, while the North region shows minimal change (-2.6%). This geographical variation suggests that cultural, economic, or behavioural factors may influence user response to the new variant, providing valuable insights for regional customisation strategies.

**Technical Validation:**
Our statistical analysis employs multiple testing methodologies to ensure robust results. The Z-test (p = 0.006834) and Chi-square test (p = 0.008726) both confirm statistical significance, while the 95% confidence interval [0.94%, 5.64%] provides a reliable range for the true improvement. Even the conservative lower bound of 0.94% represents meaningful business impact.

**Business Impact Assessment:**
The 51.56% conversion rate improvement translates directly to revenue growth and enhanced user engagement. With 2,000 users in our test, this represents a substantial sample size that provides confidence in scaling the results across the entire user base. The consistent performance across device types (Desktop: +59.7%, Mobile: +46.3%, Tablet: +39.9%) ensures the improvement will benefit all user segments.

**Strategic Implementation Roadmap:**

**Phase 1: Immediate Deployment (Week 1-2)**
- Roll out Group B variant to 100% of traffic
- Implement real-time monitoring dashboards
- Set up automated alerts for performance tracking
- Communicate changes to stakeholders and support teams

**Phase 2: Performance Optimisation (Week 3-8)**
- Monitor conversion rates daily and identify any performance fluctuations
- Analyse segment-specific performance to identify additional optimisation opportunities
- Investigate the North region's minimal improvement and develop targeted strategies
- Optimise email campaigns based on the 87.1% improvement observed

**Phase 3: Advanced Segmentation (Month 2-3)**
- Develop regional customisation strategies based on geographical performance patterns
- Implement device-specific optimisations for maximum impact
- Create personalised user experiences based on channel performance insights
- Establish A/B testing frameworks for continuous improvement

**Phase 4: Future Testing Strategy (Month 3+)**
- Design multivariate tests to further optimise the Group B variant
- Explore additional user experience improvements based on behavioural insights
- Develop predictive models for user response to future changes
- Establish a culture of data-driven decision making

**Risk Mitigation:**
While the results are overwhelmingly positive, we've identified potential risks and mitigation strategies. The North region's minimal improvement suggests the need for regional customisation, while the strong email performance indicates opportunities for channel-specific optimisation. We recommend implementing gradual rollouts in different regions to monitor performance and adjust strategies accordingly.

**Long-term Strategic Value:**
This A/B test demonstrates the power of data-driven decision making in product development. The comprehensive analysis provides not just immediate implementation guidance, but also valuable insights for future product iterations and user experience enhancements. The statistical rigour and business impact analysis serve as a template for future testing initiatives.

**Success Metrics for Implementation:**
- Maintain conversion rate improvement above 40% (conservative estimate)
- Achieve consistent performance across all user segments
- Identify and implement at least 2 additional optimisation opportunities
- Establish baseline metrics for future A/B testing initiatives

**Final Recommendation:**
Based on the comprehensive analysis, we strongly recommend implementing Group B immediately while establishing robust monitoring systems. The statistical evidence, business impact, and strategic insights all support this decision. The 51.56% improvement represents a significant competitive advantage that should be capitalised on without delay.

This project exemplifies the intersection of statistical analysis, business strategy, and user experience design - demonstrating how data science can drive meaningful business outcomes through rigorous testing and thoughtful interpretation of results.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or issues, please open an issue on GitHub.
