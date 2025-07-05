# A/B Testing Case Study

A simulation that simulates and visualizes an A/B test comparing click‑through rates (CTR) between two versions of a web page (control vs. experimental). The app allows users to adjust input parameters (control CTR, experimental CTR, sample size, significance level, and Minimum Detectable Effect) and instantly see:

* A bar chart of clicks vs. no-clicks with percentage annotations
* Statistical test results (z‑statistic, p‑value)
* Confidence interval for the difference in proportions
* Practical significance assessment against the user‑defined MDE
* A standard normal distribution plot with rejection regions and the observed z‑statistic

---

##  Features

* **Simulation** of binary click data for two groups
* **Powerful controls** for CTR inputs, sample size, α, and MDE
* **Automated statistical analysis** using z‑test for proportions
* **Dynamic visualizations** built with Matplotlib and Seaborn
* **Interactive UI** powered by Streamlit

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vaibhav34777/ab-testing-case-study.git
   cd ab-testing-case-study
   ```
2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\\Scripts\\activate  # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

##  Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Adjust the **sidebar** sliders and inputs to set your control and experimental CTRs, sample size, significance level, and MDE.
* Click **Run Analysis** to generate updated plots and results.

---

##  Repository Structure

```
ab-testing-case-study/
│
├── app.py                 # Streamlit application
├── requirements.txt       # Python package dependencies
├── ab_testing_case_study.ipynb  # Jupyter notebook version
└── README.md              # Project overview and instructions
```

---

##  Methodology

1. **Data Simulation**: Generate binary outcomes (click/no-click) for control and experimental groups based on user‑specified CTRs and sample size.
2. **Statistical Testing**: Compute pooled standard error, z‑statistic, and two‑tailed p‑value for a difference in proportions.
3. **Confidence Interval**: Calculate the (1-α)% CI around the difference in CTRs.
4. **Practical Significance**: Compare the CI lower bound to the user‑defined MDE.
5. **Visualization**: Present bar charts with percentages and overlay the standard normal PDF with rejection regions.

---

##  Requirements

See `requirements.txt` for exact versions. Key libraries include:

* Streamlit
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

---

##  License

This project is licensed under the MIT License. See `LICENSE` for details.

