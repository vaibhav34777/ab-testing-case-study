import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, stats

# App title and context
st.title("Interactive A/B Testing Case Study")
st.markdown("Comparing the click-through rate (CTR) of two versions of a web page: control vs. experimental.")

# Sidebar inputs
st.sidebar.header("Input Parameters")
col1, col2 = st.sidebar.columns(2)
p_control = col1.number_input("Control CTR (0-1)", value=0.2, min_value=0.0, max_value=1.0, step=0.01)
p_experimental = col2.number_input("Experimental CTR (0-1)", value=0.3, min_value=0.0, max_value=1.0, step=0.01)
sample_size = st.sidebar.number_input("Sample size per group", value=10000, min_value=1)
alpha = st.sidebar.number_input("Significance level (alpha)", value=0.05, min_value=0.0, max_value=1.0, step=0.01)
mde = st.sidebar.number_input("Minimum Detectable Effect (MDE) in absolute terms (e.g., 0.05 for 5%)", value=0.1, min_value=0.0, max_value=1.0, step=0.01)

# Button to run analysis
def run_analysis():
    # Simulate counts
    success_con = int(sample_size * p_control)
    success_exp = int(sample_size * p_experimental)

    # Build DataFrame
    df = pd.DataFrame({
        'group': ['Control'] * sample_size + ['Experimental'] * sample_size,
        'click': [1] * success_con + [0] * (sample_size - success_con) +
                 [1] * success_exp + [0] * (sample_size - success_exp)
    })

    # Plot click counts with percentages
    st.subheader("Clicks / No Clicks per Group")
    fig1, ax1 = plt.subplots(figsize=(6, 5))
    palette = {1: 'orange', 0: 'blue'}
    hue_order = [0, 1]
    sns.countplot(x='group', hue='click', data=df, palette=palette, hue_order=hue_order, ax=ax1)
    ax1.set_xlabel('Group')
    ax1.set_ylabel('Count')
    ax1.set_title('Clicks/No Clicks for each group')
    ax1.legend(title='Click', labels=['No Click', 'Click'])
    for p in ax1.patches:
        count = p.get_height()
        pct = count / sample_size * 100
        x = p.get_x() + p.get_width() / 2
        ax1.text(x, count + sample_size * 0.01, f'{pct:.1f}%', ha='center', va='bottom')
    st.pyplot(fig1)

    # Statistical calculations
    p_pool = (success_con + success_exp) / (2 * sample_size)
    SE = np.sqrt(p_pool * (1 - p_pool) * (2 / sample_size))
    z_stat = (p_experimental - p_control) / SE
    p_value = 2 * (1 - norm.cdf(abs(z_stat)))

    # Confidence interval for difference in proportions
    diff = p_experimental - p_control
    z_crit = norm.ppf(1 - alpha/2)
    ci_low = diff - z_crit * SE
    ci_high = diff + z_crit * SE

    # Display results
    st.subheader("Statistical Test Results")
    st.write(f"**Z-statistic:** {z_stat:.3f}")
    st.write(f"**P-value:** {p_value:.4g}")
    st.write(f"**Confidence Interval ({100*(1-alpha):.0f}%):** [{ci_low:.3f}, {ci_high:.3f}]")
    stat_sig = p_value < alpha
    st.write(f"**Statistical significance (p < {alpha}):** {'Yes' if stat_sig else 'No'}")

    # Practical significance check using MDE
    practical_sig = ci_low > mde
    st.write(f"**Minimum Detectable Effect (MDE):** {mde:.3f}")
    st.write(f"**Practical significance (CI lower bound > MDE):** {'Yes' if practical_sig else 'No'}")

    # Distribution plot
    st.subheader("Z-Statistic vs. Standard Normal Distribution")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    z_values = np.linspace(-4, 4, 1000)
    pdf_values = norm.pdf(z_values)
    ax2.plot(z_values, pdf_values, color='black', label='Standard Normal PDF')
    ax2.fill_between(z_values, pdf_values, where=(z_values <= -z_crit), color='red', alpha=0.3)
    ax2.fill_between(z_values, pdf_values, where=(z_values >= z_crit), color='red', alpha=0.3)
    ax2.axvline(-z_crit, color='red', linestyle='--', label=f'-Z critical ({z_crit:.2f})')
    ax2.axvline(z_crit, color='red', linestyle='--', label=f'Z critical ({z_crit:.2f})')
    ax2.axvline(z_stat, color='blue', linestyle='--', label=f'Z stat ({z_stat:.2f})')
    ax2.set_xlabel('Z-value')
    ax2.set_ylabel('Probability Density')
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)

# Trigger analysis
if st.sidebar.button("Run Analysis"):
    run_analysis()

st.markdown("---")
st.write("Use the sidebar to adjust CTRs, sample size, alpha, and MDE to explore both statistical and practical significance in an A/B test.")
