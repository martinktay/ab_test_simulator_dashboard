# A/B Testing Dashboard with Streamlit

A clean, interactive dashboard for analyzing A/B test results using Python and Streamlit.

## 📊 Project Overview

This dashboard provides comprehensive analysis of A/B test data including:
- **Conversion Rate Analysis**: Compare conversion rates between test groups
- **Statistical Significance Testing**: Z-test and chi-square test results
- **Segmentation Analysis**: Breakdown by device, channel, and region
- **Interactive Visualizations**: Charts and tables for data exploration

## 🚀 Features

- **Real-time Data Analysis**: Load and process A/B test data instantly
- **Statistical Testing**: Automated significance testing with clear results
- **Multi-dimensional Segmentation**: Analyze results across different user segments
- **Responsive Design**: Clean, minimalist interface optimized for insights
- **Interactive Charts**: Plotly-based visualizations for better user experience

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
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
└── .gitignore              # Git ignore file
```

## 📊 Dashboard Screenshots

*[Screenshots will be added after dashboard completion]*

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

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or issues, please open an issue on GitHub. 