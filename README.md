# waferwise
A Semiconductor Wafer Loading &amp; Tool Requirement Analysis

# ArrivalEvent

A comprehensive wafer production and tool capacity planning project, developed for the **Micron NUS-ISE Business Analytics Case Competition 2025**, focusing on **semiconductor manufacturing** strategies from 2026 to 2027.

---

### Table of Contents
- [Overview](#overview)  
- [Key Objectives](#key-objectives)  
- [Methodology](#methodology)  
  - [Wafer Loading Profile](#wafer-loading-profile)  
  - [Tool Requirements & CAPEX](#tool-requirements--capex)  
  - [Variability & Risk Modeling](#variability--risk-modeling)  
- [Key Insights](#key-insights)  
- [Usage Guide](#usage-guide)  
- [Project Structure](#project-structure)  
- [Future Extensions](#future-extensions)  
- [License & Acknowledgments](#license--acknowledgments)

---

### Overview
**ArrivalEvent** is a framework designed to optimize **wafer production planning** in a semiconductor fab. It aims to:
- **Meet quarterly production targets (TAM)** with minimal waste.
- **Optimize tool usage** by pinpointing where additional tools are truly necessary.
- **Analyze variability and risk** through advanced statistical methods like **bootstrapping** and **Monte Carlo simulation**.

These strategies balance **costs**, **capacity**, and **operational feasibility** over multiple quarters.

---

### Key Objectives
1. **Minimize Wafer Usage**  
   Reduce total wafers by leveraging higher-yield/higher-capacity nodes as they mature.
2. **Optimize Profitability**  
   Incorporate **CAPEX** costs for new tools and measure net profit (*Revenue – CAPEX*).
3. **Manage Operational Risk**  
   Account for random fluctuations in processing time (RPT) to reduce production shortfalls.

---

### Methodology

#### Wafer Loading Profile
**Objective:** Assign the optimal number of wafers to each node every quarter to meet demand while minimizing wafer usage.

- **Constraints:**
  - Must be within ±2 billion GB of the **Total Addressable Market (TAM)** for each quarter.
  - Weekly wafer starts can only change by ±2,500 wafers from one quarter to the next.
- **Approach:**
  - Utilize a **Linear Optimization Model** to minimize wafer counts.
  - Factor in each node’s **yield** and **storage capacity (GB/wafer)** across quarters.
- **Results:**
  - **Early Quarters (Q1’26 – Q2’26):** Heavily rely on **Node 1** (high yield, low capacity).
  - **Mid Quarters (Q3’26 – Q4’26):** Shift focus to **Node 2** and begin ramping **Node 3**.
  - **Later Quarters (Q1’27 – Q4’27):** **Node 3** (with improving yields and highest capacity) dominates production.

#### Tool Requirements & CAPEX
**Objective:** Translate wafer starts into **tool requirements** at each workstation and compute **CAPEX** for additional tools if needed.

1. **Calculating Tool Requirements**  
   - Convert weekly wafer production to a **quarterly total** (×13 weeks).  
   - Multiply wafer counts by the **minute load** per wafer at each workstation.  
   - Compare total processing minutes to **available tool time** (13 weeks × 10,080 min/week × utilization × current tool count).

2. **Purchasing Tools**  
   - If required capacity exceeds current capacity, purchase additional tools.  
   - **CAPEX** = (Number of new tools) × (Cost per tool).

3. **Net Profit**  
   - **Revenue:** wafer output in GB × contribution margin.  
   - **Net Profit:** Revenue – CAPEX.

4. **Trade-Off**  
   - Minimizing wafer counts can become **costly** if it requires many new tools.  
   - Adjusting node usage may reduce CAPEX and boost profit.

#### Variability & Risk Modeling
**Objective:** Assess the impact of random processing times (RPT) on capacity and profitability.

1. **Random Processing Times (RPT)**  
   - Caused by temperature changes, machine calibration, supply chain fluctuations, etc.

2. **Bootstrapping & Monte Carlo Simulation**  
   - **Bootstrapping:** Resample historical RPT data to capture outliers and the true distribution.  
   - **Monte Carlo:** Run 10,000+ iterations of production scenarios to estimate the likelihood of exceeding tool capacity.

3. **Failure Probability**  
   - Probability that **total wafer processing** exceeds **available tool time** in a given week or quarter.  
   - Without mitigation, results indicated a **77.68%** chance of failing at least once across eight quarters.

4. **Impact on Profitability**  
   - Missed production → Lost revenue and possible penalties.  
   - May require extra tools (CAPEX) or extended hours (OPEX).

5. **Risk Mitigation**  
   - Increase tools where failures are most likely.  
   - Dynamically adjust weekly wafer starts based on real-time RPT trends.  
   - Aim to reduce the failure probability below a 5–10% threshold.

---

### Key Insights
1. **Balance Yield vs. CAPEX**  
   Prioritizing high-yield, high-capacity nodes cuts wafer usage but may require more complex (and expensive) tooling.  
2. **Dynamic Planning**  
   A static weekly load ignores RPT fluctuations; a dynamic approach mitigates unexpected capacity spikes.  
3. **Power of Statistical Methods**  
   Bootstrapping and Monte Carlo simulations better capture real-world risk compared to a single median estimate.

---

### Usage Guide
1. **Data Preparation**  
   - Collect quarterly wafer starts, yield rates, GB/wafer, and tool cost parameters.
2. **Optimization Setup**  
   - Use libraries like [`PuLP`](https://github.com/coin-or/pulp) in Python for linear or mixed-integer optimization.  
   - Enforce constraints (e.g., TAM, yield, capacity) to generate wafer loading strategies.
3. **Tool Requirement Calculation**  
   - Map wafer production to minutes-per-workstation.  
   - Compare with existing tool capacities.
4. **Risk Simulation**  
   - Apply bootstrapping/Monte Carlo to your RPT dataset.  
   - Evaluate weekly or quarterly failure probabilities.
5. **Decision Adjustment**  
   - If failure probability is high, consider extra tools or shifting wafer allocations.  
   - Weigh the extra CAPEX against potential lost revenue.

---

### Project Structure
/data ├─ wafer_starts.csv ├─ node_yield_rates.csv └─ rpt_samples.csv

/notebooks ├─ wafer_loading_optimization.ipynb ├─ tool_capacity_calculation.ipynb └─ risk_simulation_monte_carlo.ipynb

/scripts ├─ preprocess_data.py ├─ bootstrapping.py └─ monte_carlo.py

/results ├─ tool_requirements_summary.csv ├─ capex_spreadsheet.csv └─ net_profit_analysis.csv


---

### Future Extensions
- **Real-Time Scheduling**  
  Dynamically vary wafer starts every week based on real-time data, rather than committing to fixed quarterly plans.
- **Expanded Cost Model**  
  Include OPEX (e.g., labor, utilities) and other overhead in addition to CAPEX.
- **Multi-Objective Optimization**  
  Combine wafer minimization, profit maximization, and broader factors such as sustainability or supply chain resilience.

---

### License & Acknowledgments
This project was developed for academic purposes under the **Micron NUS-ISE Business Analytics Case Competition 2025**. Please consult competition guidelines and institutional rules for licensing information.

**Special Thanks:**  
- Mentors and instructors for guidance in operations research and statistical modeling.  
- Organizers for providing real-world insights and data parameters.

> **Disclaimer:**  
> The analysis relies on hypothetical or sample data. Actual fab conditions may require more nuanced models.


