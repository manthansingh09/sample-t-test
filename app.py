import numpy as np
from scipy.stats import t
import streamlit as st

def two_side_givendata(n1, n2, x1_bar, x2_bar, s1, s2, comparison):
    """
    Perform two-sample t-test with given data.
    
    Parameters:
    - n1: Sample 1 size
    - n2: Sample 2 size
    - x1_bar: Sample 1 mean
    - x2_bar: Sample 2 mean
    - s1: Sample 1 standard deviation
    - s2: Sample 2 standard deviation
    - comparison: "greater", "less", or "two-tailed"
    
    Returns: Dictionary with test results
    """
    
    # Standard Error
    SE = np.sqrt((s1**2 / n1) + (s2**2 / n2))
    
    # t statistic
    t_cal = (x1_bar - x2_bar) / SE
    
    # Degrees of freedom
    df = n1 + n2 - 2
    
    # Alpha level
    alpha = 0.01
    
    # Critical values and decision based on test type
    if comparison == 'two-tailed':
        # Two-tailed test: H₀: μ₁ = μ₂ vs H₁: μ₁ ≠ μ₂
        # Critical values at ±t_α/2 = ±t_0.005
        t_crit = t.ppf(1 - alpha/2, df)
        t_table_pos = t_crit
        t_table_neg = -t_crit
        # Reject if |t_cal| > t_crit, i.e., if t_cal > t_crit or t_cal < -t_crit
        decision = "Reject H0" if abs(t_cal) > t_crit else "Fail to Reject H0"
        
    elif comparison == 'greater':
        # Right-tailed test: H₀: μ₁ ≤ μ₂ vs H₁: μ₁ > μ₂
        # Critical value at t_α = t_0.01
        t_crit = t.ppf(1 - alpha, df)
        t_table_pos = t_crit
        t_table_neg = -t_crit
        # Reject if t_cal > t_crit
        decision = "Reject H0" if t_cal > t_crit else "Fail to Reject H0"
        
    else:  # comparison == 'less'
        # Left-tailed test: H₀: μ₁ ≥ μ₂ vs H₁: μ₁ < μ₂
        # Critical value at -t_α = -t_0.01
        t_crit = t.ppf(1 - alpha, df)
        t_table_pos = t_crit
        t_table_neg = -t_crit
        # Reject if t_cal < -t_crit
        decision = "Reject H0" if t_cal < -t_crit else "Fail to Reject H0"
    
    return {
        "t_statistic": t_cal,
        "degrees_freedom": df,
        "standard_error": SE,
        "critical_neg": t_table_neg,
        "critical_pos": t_table_pos,
        "decision": decision
    }


# Streamlit UI
st.set_page_config(page_title="Two-Sample t-Test Calculator", layout="wide")
st.title("Two-Sample t-Test Calculator")
st.write("This tool performs a two-sample t-test with given sample statistics.")

# Create input columns
col1, col2 = st.columns(2)

with col1:
    st.header("Sample 1")
    n1 = st.number_input("Sample 1 size (n1)", min_value=1, value=60)
    x1_bar = st.number_input("Sample 1 mean (x̄1)", value=86.0)
    s1 = st.number_input("Sample 1 standard deviation (s1)", min_value=0.0, value=6.0)

with col2:
    st.header("Sample 2")
    n2 = st.number_input("Sample 2 size (n2)", min_value=1, value=75)
    x2_bar = st.number_input("Sample 2 mean (x̄2)", value=82.0)
    s2 = st.number_input("Sample 2 standard deviation (s2)", min_value=0.0, value=9.0)

# Test type selection
st.subheader("Test Type")
comparison = st.radio(
    "Select the type of test:",
    options=["two-tailed", "greater", "less"],
    format_func=lambda x: {
        "two-tailed": "Two-Tailed (H₁: μ₁ ≠ μ₂)",
        "greater": "Right-Tailed (H₁: μ₁ > μ₂)",
        "less": "Left-Tailed (H₁: μ₁ < μ₂)"
    }[x],
    horizontal=True
)

# Calculate button
if st.button("Calculate t-Test", type="primary"):
    results = two_side_givendata(n1, n2, x1_bar, x2_bar, s1, s2, comparison)
    
    # Display results
    st.subheader("Results")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Calculated t-statistic", f"{results['t_statistic']:.4f}")
    with col2:
        st.metric("Degrees of Freedom", results['degrees_freedom'])
    with col3:
        st.metric("Standard Error", f"{results['standard_error']:.4f}")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Critical Value (Negative)", f"{results['critical_neg']:.4f}")
    with col2:
        st.metric("Critical Value (Positive)", f"{results['critical_pos']:.4f}")
    with col3:
        decision_color = "🟢" if "Fail" in results['decision'] else "🔴"
        st.metric("Decision", f"{decision_color} {results['decision']}")
    
    # Display detailed output
    st.divider()
    st.subheader("Detailed Output")
    output_text = f"""
    **Input Parameters:**
    - Sample 1 size (n1): {n1}
    - Sample 2 size (n2): {n2}
    - Sample 1 mean (x̄1): {x1_bar:.4f}
    - Sample 2 mean (x̄2): {x2_bar:.4f}
    - Sample 1 standard deviation (s1): {s1:.4f}
    - Sample 2 standard deviation (s2): {s2:.4f}
    - Test Type: {comparison.upper()}
    
    **Calculations:**
    - Standard Error (SE): {results['standard_error']:.4f}
    - Calculated t-statistic: {results['t_statistic']:.4f}
    - Degrees of Freedom: {results['degrees_freedom']}
    - Critical Values (α = 0.01): [{results['critical_neg']:.4f}, {results['critical_pos']:.4f}]
    - **Conclusion:** {results['decision']}
    """
    st.markdown(output_text)