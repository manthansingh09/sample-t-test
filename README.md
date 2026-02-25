# Two-Sample t-Test Calculator

A Streamlit-based web application for performing statistical hypothesis testing using the two-sample t-test with given sample statistics.

## Overview

This application allows you to conduct a two-sample t-test by providing sample statistics (size, mean, and standard deviation) for two samples. The calculator supports three types of hypothesis tests:
- **Two-Tailed Test**: Testing if two population means are different
- **Right-Tailed Test**: Testing if the first population mean is greater than the second
- **Left-Tailed Test**: Testing if the first population mean is less than the second

## Features

- **Interactive Input Fields**: Easy-to-use form for entering sample statistics
- **Multiple Test Types**: Support for two-tailed, right-tailed, and left-tailed tests
- **Detailed Results**: Displays calculated t-statistic, degrees of freedom, standard error, and critical values
- **Visual Decision Indicator**: Color-coded result showing whether to reject or fail to reject the null hypothesis
- **Comprehensive Output**: Captures all input parameters and calculations for reference

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone or download the project files to your local machine

2. Navigate to the project directory:
```bash
cd path/to/SSDI
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### How to Use

1. **Enter Sample 1 Data**:
   - Sample 1 size (n1)
   - Sample 1 mean (x̄1)
   - Sample 1 standard deviation (s1)

2. **Enter Sample 2 Data**:
   - Sample 2 size (n2)
   - Sample 2 mean (x̄2)
   - Sample 2 standard deviation (s2)

3. **Select Test Type**:
   - Two-Tailed (H₁: μ₁ ≠ μ₂)
   - Right-Tailed (H₁: μ₁ > μ₂)
   - Left-Tailed (H₁: μ₁ < μ₂)

4. **Click "Calculate t-Test"** to see results

5. Results include:
   - Calculated t-statistic
   - Degrees of freedom
   - Standard error
   - Critical values (α = 0.01)
   - Statistical decision (Reject H0 / Fail to Reject H0)

## Example

Default values are provided:
- Sample 1: n₁ = 60, x̄₁ = 86, s₁ = 6
- Sample 2: n₂ = 75, x̄₂ = 82, s₂ = 9
- Test Type: Left-Tailed

Simply click "Calculate t-Test" to see the results with these values.

## Technical Details

### Calculations

The application performs the following calculations:

1. **Standard Error (SE)**:
   ```
   SE = √((s₁²/n₁) + (s₂²/n₂))
   ```

2. **t-statistic**:
   ```
   t = (x̄₁ - x̄₂) / SE
   ```

3. **Degrees of Freedom**:
   ```
   df = n₁ + n₂ - 2
   ```

4. **Critical Values** (at α = 0.01):
   - Uses t-distribution with calculated degrees of freedom
   - Two-tailed: ±t₀.₀₀₅
   - One-tailed: ±t₀.₀₁

## Requirements

- numpy==2.4.2
- scipy==1.17.1
- streamlit==1.28.1

## Files

- `app.py`: Main application file containing the Streamlit UI and t-test logic
- `requirements.txt`: Python package dependencies
- `README.md`: This file
- `SSDI.ipynb`: Jupyter notebook (if applicable)

## Notes

- The significance level (α) is fixed at 0.01
- The application uses independent samples t-test assumption (two populations)
- Results are displayed with 4 decimal places for precision

## License

This project is provided as-is for educational and statistical analysis purposes.

## Support

For issues or questions about the calculations, please refer to statistical hypothesis testing documentation or consult your instructional materials.
