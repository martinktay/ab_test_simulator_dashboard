import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="A/B Testing Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    /* Professional Dark Theme Dashboard */
    
    /* Global Styles */
    .main {
        background: #0a0a0a;
        min-height: 100vh;
        color: #ffffff;
    }
    
    .stApp {
        background: #0a0a0a;
    }
    
    /* Header Styling */
    .main-header {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border: 1px solid #333333;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
        margin-bottom: 1rem;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #00d4ff, #0099cc);
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(0, 212, 255, 0.2);
        border-color: #00d4ff;
    }
    
    /* Statistical Results */
    .statistical-result {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        margin-bottom: 1rem;
        border: 1px solid #333333;
        position: relative;
        overflow: hidden;
    }
    
    .statistical-result::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #ff6b6b, #ee5a24);
    }
    
    /* Section Headers */
    .section-header {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: #ffffff;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #00d4ff;
        display: inline-block;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: #1a1a1a;
        border-right: 1px solid #333333;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
        color: #000000;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.4);
    }
    
    /* Chart Containers */
    .chart-container {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        margin: 1rem 0;
        border: 1px solid #333333;
    }
    
    /* Dataframe Styling */
    .dataframe {
        background: #1a1a1a;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        border: 1px solid #333333;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #888888;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-size: 0.9rem;
    }
    
    /* Custom metric styling */
    .metric-value {
        color: #00d4ff !important;
        font-weight: 700 !important;
    }
    
    .metric-label {
        color: #cccccc !important;
        font-weight: 500 !important;
    }
    
    .metric-delta {
        color: #00ff88 !important;
        font-weight: 600 !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #1a1a1a;
        border-radius: 8px;
        padding: 4px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #2d2d2d;
        border-radius: 6px;
        color: #cccccc;
        border: 1px solid #333333;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%);
        color: #000000;
        font-weight: 600;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        
        .metric-card {
            padding: 1rem;
        }
        
        .statistical-result {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    """Load and cache the A/B test data"""
    try:
        # Try to load the CSV file
        df = pd.read_csv('ab_test_enriched.csv')
    except FileNotFoundError:
        # If file doesn't exist, generate sample data
        st.info("📁 Sample data file not found. Generating sample A/B test data...")
        df = generate_sample_data()

    return df


def generate_sample_data():
    """Generate sample A/B test data for demonstration"""
    np.random.seed(42)
    n_users = 10000

    # To create user IDs
    user_ids = [f"user_{i:06d}" for i in range(1, n_users + 1)]

    # Randomly assign groups (A/B)
    groups = np.random.choice(['A', 'B'], size=n_users, p=[0.5, 0.5])

    # Generate conversion data with different rates for A and B
    conversions = []
    for group in groups:
        if group == 'A':
            # Group A has 12% conversion rate
            conversions.append(np.random.choice([0, 1], p=[0.88, 0.12]))
        else:
            # Group B has 15% conversion rate (25% improvement)
            conversions.append(np.random.choice([0, 1], p=[0.85, 0.15]))

    # Generate session duration (in seconds)
    session_durations = np.random.exponential(300, n_users)
    session_durations = np.clip(session_durations, 30, 1800)

    # Generate page views
    page_views = np.random.poisson(8, n_users)
    page_views = np.clip(page_views, 1, 50)

    # Generate device types
    devices = np.random.choice(
        ['Desktop', 'Mobile', 'Tablet'], size=n_users, p=[0.6, 0.35, 0.05])

    # Generate channels
    channels = np.random.choice(['Organic', 'Paid', 'Direct', 'Social', 'Email'],
                                size=n_users, p=[0.4, 0.25, 0.2, 0.1, 0.05])

    # Generate regions
    regions = np.random.choice(['North America', 'Europe', 'Asia', 'South America', 'Africa'],
                               size=n_users, p=[0.4, 0.3, 0.2, 0.08, 0.02])

    # Generate visit dates (last 30 days)
    from datetime import datetime, timedelta
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    visit_dates = [
        start_date + timedelta(days=np.random.randint(0, 31)) for _ in range(n_users)]
    visit_dates = [date.strftime('%Y-%m-%d') for date in visit_dates]

    # Create DataFrame
    df = pd.DataFrame({
        'user_id': user_ids,
        'group': groups,
        'converted': conversions,
        'session_duration_sec': session_durations,
        'page_views': page_views,
        'device': devices,
        'channel': channels,
        'region': regions,
        'visit_date': visit_dates
    })

    return df


def perform_statistical_tests(df):
    """Perform statistical tests for A/B comparison"""
    # Group data
    group_a = df[df['group'] == 'A']['converted']
    group_b = df[df['group'] == 'B']['converted']

    # Z-test for proportions
    n_a, n_b = len(group_a), len(group_b)
    p_a, p_b = group_a.mean(), group_b.mean()

    # Pooled proportion
    p_pooled = (group_a.sum() + group_b.sum()) / (n_a + n_b)

    # Standard error
    se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n_a + 1/n_b))

    # Z-statistic
    z_stat = (p_b - p_a) / se

    # P-value (two-tailed)
    p_value_z = 2 * (1 - stats.norm.cdf(abs(z_stat)))

    # Chi-square test
    contingency_table = pd.crosstab(df['group'], df['converted'])
    chi2_stat, p_value_chi2, dof, expected = stats.chi2_contingency(
        contingency_table)

    # Confidence interval for difference
    diff = p_b - p_a
    ci_lower = diff - 1.96 * se
    ci_upper = diff + 1.96 * se

    return {
        'z_statistic': z_stat,
        'p_value_z': p_value_z,
        'chi2_statistic': chi2_stat,
        'p_value_chi2': p_value_chi2,
        'difference': diff,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'relative_improvement': (p_b - p_a) / p_a * 100
    }


def create_conversion_comparison_chart(df):
    """Create conversion rate comparison chart"""
    conversion_rates = df.groupby('group')['converted'].agg(
        ['mean', 'count']).reset_index()
    conversion_rates.columns = ['Group', 'Conversion Rate', 'Sample Size']

    fig = px.bar(
        conversion_rates,
        x='Group',
        y='Conversion Rate',
        text=conversion_rates['Conversion Rate'].apply(lambda x: f'{x:.3f}'),
        color='Group',
        color_discrete_map={'A': '#00d4ff', 'B': '#ff6b6b'},
        title='Conversion Rate Comparison: Group A vs Group B'
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(
        yaxis_title='Conversion Rate',
        showlegend=False,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"),
        title_font_size=18,
        title_font_color='#ffffff'
    )

    return fig


def create_segmentation_charts(df):
    """Create segmentation analysis charts"""
    # Device segmentation
    device_conv = df.groupby(['device', 'group'])[
        'converted'].mean().reset_index()
    device_fig = px.bar(
        device_conv,
        x='device',
        y='converted',
        color='group',
        barmode='group',
        title='Conversion Rate by Device Type',
        color_discrete_map={'A': '#00d4ff', 'B': '#ff6b6b'}
    )
    device_fig.update_layout(
        yaxis_title='Conversion Rate',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"),
        title_font_size=16,
        title_font_color='#ffffff'
    )

    # Channel segmentation
    channel_conv = df.groupby(['channel', 'group'])[
        'converted'].mean().reset_index()
    channel_fig = px.bar(
        channel_conv,
        x='channel',
        y='converted',
        color='group',
        barmode='group',
        title='Conversion Rate by Channel',
        color_discrete_map={'A': '#00d4ff', 'B': '#ff6b6b'}
    )
    channel_fig.update_layout(
        yaxis_title='Conversion Rate',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"),
        title_font_size=16,
        title_font_color='#ffffff'
    )

    # Region segmentation
    region_conv = df.groupby(['region', 'group'])[
        'converted'].mean().reset_index()
    region_fig = px.bar(
        region_conv,
        x='region',
        y='converted',
        color='group',
        barmode='group',
        title='Conversion Rate by Region',
        color_discrete_map={'A': '#00d4ff', 'B': '#ff6b6b'}
    )
    region_fig.update_layout(
        yaxis_title='Conversion Rate',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"),
        title_font_size=16,
        title_font_color='#ffffff'
    )

    return device_fig, channel_fig, region_fig


def create_distribution_charts(df):
    """Create distribution charts for session duration and page views"""
    # Session duration distribution
    fig_duration = px.histogram(
        df,
        x='session_duration_sec',
        color='group',
        nbins=30,
        title='Session Duration Distribution',
        color_discrete_map={'A': '#00d4ff', 'B': '#ff6b6b'},
        opacity=0.7
    )
    fig_duration.update_layout(
        xaxis_title='Session Duration (seconds)',
        yaxis_title='Count',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"),
        title_font_size=16,
        title_font_color='#ffffff'
    )

    # Page views distribution
    fig_pages = px.histogram(
        df,
        x='page_views',
        color='group',
        nbins=20,
        title='Page Views Distribution',
        color_discrete_map={'A': '#00d4ff', 'B': '#ff6b6b'},
        opacity=0.7
    )
    fig_pages.update_layout(
        xaxis_title='Page Views',
        yaxis_title='Count',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"),
        title_font_size=16,
        title_font_color='#ffffff'
    )

    return fig_duration, fig_pages


def main():
    """Main dashboard function"""
    # Header with modern styling
    st.markdown('<h1 class="main-header">📊 A/B Testing Dashboard</h1>',
                unsafe_allow_html=True)

    # Load data
    df = load_data()

    # Sidebar filters with modern styling
    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); 
                color: #00d4ff; 
                padding: 1rem; 
                border-radius: 12px; 
                margin-bottom: 1rem;
                border: 1px solid #333333;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);">
        <h3 style="margin: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 600;">🔍 Filters</h3>
    </div>
    """, unsafe_allow_html=True)

    # Date filter
    if 'visit_date' in df.columns:
        df['visit_date'] = pd.to_datetime(df['visit_date'])
        date_range = st.sidebar.date_input(
            "Select Date Range",
            value=(df['visit_date'].min(), df['visit_date'].max()),
            min_value=df['visit_date'].min(),
            max_value=df['visit_date'].max()
        )
        if len(date_range) == 2:
            df = df[(df['visit_date'].dt.date >= date_range[0]) &
                    (df['visit_date'].dt.date <= date_range[1])]

    # Device filter
    devices = ['All'] + list(df['device'].unique())
    selected_device = st.sidebar.selectbox("Device Type", devices)
    if selected_device != 'All':
        df = df[df['device'] == selected_device]

    # Channel filter
    channels = ['All'] + list(df['channel'].unique())
    selected_channel = st.sidebar.selectbox("Channel", channels)
    if selected_channel != 'All':
        df = df[df['channel'] == selected_channel]

    # Region filter
    regions = ['All'] + list(df['region'].unique())
    selected_region = st.sidebar.selectbox("Region", regions)
    if selected_region != 'All':
        df = df[df['region'] == selected_region]

    # Display data summary
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📈 Data Summary")
    st.sidebar.metric("Total Users", f"{len(df):,}")
    st.sidebar.metric("Group A Users", f"{len(df[df['group']=='A']):,}")
    st.sidebar.metric("Group B Users", f"{len(df[df['group']=='B']):,}")

    # Main content
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Overall Conversion Rate",
            f"{df['converted'].mean():.3f}",
            f"{df['converted'].sum():,} conversions"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        group_a_conv = df[df['group'] == 'A']['converted'].mean()
        st.metric(
            "Group A Conversion Rate",
            f"{group_a_conv:.3f}",
            f"{df[df['group']=='A']['converted'].sum():,} conversions"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        group_b_conv = df[df['group'] == 'B']['converted'].mean()
        st.metric(
            "Group B Conversion Rate",
            f"{group_b_conv:.3f}",
            f"{df[df['group']=='B']['converted'].sum():,} conversions"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        improvement = ((group_b_conv - group_a_conv) / group_a_conv) * 100
        st.metric(
            "Relative Improvement",
            f"{improvement:+.1f}%",
            f"Group B vs Group A"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # Statistical tests
    st.markdown("---")
    st.markdown('<h2 class="section-header">🔬 Statistical Analysis</h2>',
                unsafe_allow_html=True)

    stats_results = perform_statistical_tests(df)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="statistical-result">', unsafe_allow_html=True)
        st.markdown("**Z-Test Results**")
        st.write(f"Z-statistic: {stats_results['z_statistic']:.3f}")
        st.write(f"P-value: {stats_results['p_value_z']:.4f}")
        st.write(
            f"Significant: {'Yes' if stats_results['p_value_z'] < 0.05 else 'No'}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="statistical-result">', unsafe_allow_html=True)
        st.markdown("**Chi-Square Test Results**")
        st.write(f"Chi²-statistic: {stats_results['chi2_statistic']:.3f}")
        st.write(f"P-value: {stats_results['p_value_chi2']:.4f}")
        st.write(
            f"Significant: {'Yes' if stats_results['p_value_chi2'] < 0.05 else 'No'}")
        st.markdown('</div>', unsafe_allow_html=True)

    # Confidence interval
    st.markdown('<div class="statistical-result">', unsafe_allow_html=True)
    st.markdown("**Confidence Interval (95%)**")
    st.write(f"Difference (B - A): {stats_results['difference']:.4f}")
    st.write(
        f"Confidence Interval: [{stats_results['ci_lower']:.4f}, {stats_results['ci_upper']:.4f}]")
    st.write(
        f"Relative Improvement: {stats_results['relative_improvement']:.1f}%")
    st.markdown('</div>', unsafe_allow_html=True)

    # Conversion comparison chart
    st.markdown("---")
    st.markdown('<h2 class="section-header">📊 Conversion Rate Comparison</h2>',
                unsafe_allow_html=True)
    conv_chart = create_conversion_comparison_chart(df)
    st.plotly_chart(conv_chart, use_container_width=True)

    # Segmentation analysis
    st.markdown("---")
    st.markdown('<h2 class="section-header">🎯 Segmentation Analysis</h2>',
                unsafe_allow_html=True)

    device_fig, channel_fig, region_fig = create_segmentation_charts(df)

    tab1, tab2, tab3 = st.tabs(["Device", "Channel", "Region"])

    with tab1:
        st.plotly_chart(device_fig, use_container_width=True)

    with tab2:
        st.plotly_chart(channel_fig, use_container_width=True)

    with tab3:
        st.plotly_chart(region_fig, use_container_width=True)

    # Distribution analysis
    st.markdown("---")
    st.markdown('<h2 class="section-header">📈 Distribution Analysis</h2>',
                unsafe_allow_html=True)

    fig_duration, fig_pages = create_distribution_charts(df)

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_duration, use_container_width=True)

    with col2:
        st.plotly_chart(fig_pages, use_container_width=True)

    # Detailed metrics table
    st.markdown("---")
    st.markdown('<h2 class="section-header">📋 Detailed Metrics</h2>',
                unsafe_allow_html=True)

    metrics_df = df.groupby('group').agg({
        'converted': ['count', 'sum', 'mean'],
        'session_duration_sec': ['mean', 'std'],
        'page_views': ['mean', 'std']
    }).round(3)

    metrics_df.columns = ['Users', 'Conversions', 'Conv_Rate', 'Avg_Session_Duration',
                          'Std_Session_Duration', 'Avg_Page_Views', 'Std_Page_Views']
    st.dataframe(metrics_df, use_container_width=True)

    # Footer with modern styling
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <p>📊 Dashboard created with Streamlit • 🔬 Data analysis powered by Python • 🎨 Modern UI Design</p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem;">Built with ❤️ for data-driven decision making</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
