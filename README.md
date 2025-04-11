# waferwise
A Semiconductor Wafer Loading &amp; Tool Requirement Analysis
Overview
This project, conducted under the “Micron NUS-ISE Business Analytics Case Competition 2025,” examines wafer production planning and tool capacity allocation in a semiconductor manufacturing setting for the years 2026–2027. The overarching goal is to ensure that Total Addressable Market (TAM) demand is met while balancing production costs, tool purchase investments (CAPEX), and operational viability.

The analysis focuses on:

Wafer Loading Profile: Determining how many wafers to assign to each manufacturing “node” in each quarter.

Tool Requirements & CAPEX: Calculating how many tools must be purchased or utilized at each workstation.

Profitability & Risk Assessment: Evaluating net profit, factoring in wafer revenue and CAPEX, and using advanced statistical methods (bootstrapping, Monte Carlo) to handle random variations in processing time.

Key Objectives
Minimize Wafer Usage (Baseline Objective):

Use higher-capacity/higher-yield nodes as soon as yield rates permit, to reduce overall wafer starts needed.

Phase out lower-yield or lower-capacity nodes over time.

Incorporate Tool Requirements and Costs (Expanded Objective):

Translate wafer starts into total processing times at each workstation.

Compare required processing time to available tool time (factoring in utilization).

Determine the cost of new tools if existing tool capacity is insufficient.

Optimize Profitability:

Balance revenue against CAPEX from tool purchases.

Adjust wafer loading strategies to avoid purchasing too many additional tools.

Account for random variations (RPT or “reliability performance time”) that can lead to production shortfalls.

Project Components
1. Wafer Loading Profile (Question 1, Part a)
Objective: Minimize total wafer usage while meeting quarterly TAM demand.

Method: Linear optimization integrating constraints such as:

Per-quarter production requirements (±2 billion GB of forecast).

Physical limits on weekly changes (±2,500 wafers/week) to avoid abrupt shifts.

Different yield percentages and GB-per-wafer for each node over time.

Key Findings:

Early Quarters (Q1’26 – Q2’26): Node 1 is used heavily due to stable yield (98%) but low capacity (100K GB). Node 3 is minimally used due to very low yield (20%).

Mid Quarters (Q3’26 – Q4’26): Node 2 becomes the workhorse (95–98% yield, 150K GB per wafer). Node 3 allocation gradually increases as yield improves. Node 1 is gradually reduced.

Later Quarters (Q1’27 – Q4’27): Node 3 becomes dominant (yield 65–98%) with the highest GB capacity (200K GB), significantly reducing overall wafer counts. Node 1 is phased out entirely.

2. Tool Requirements & CAPEX (Question 1, Part b)
Tool Requirements:

Convert weekly wafer production to quarterly totals (multiply by 13 weeks).

Compute processing time needed at each workstation (wafer count × minutes/wafer).

Compare processing time to available time (13 weeks × 10,080 min/week × utilization × current tool quantity).

Result: The ratio determines how many tools are needed at each workstation.

Calculating CAPEX:

Additional tools are purchased only if the total requirement exceeds what is already available (including tools acquired in previous quarters).

CAPEX is the number of new tools multiplied by the cost per tool, summed across all workstations.

Net Profit = Revenue – CAPEX:

Revenue: Based on the total GB produced each quarter (wafer count × GB/wafer × yield) times a fixed contribution margin.

CAPEX: Additional tools purchased each quarter.

Insight: A wafer-loading plan that minimizes wafer count may still be suboptimal for profit if it requires substantial tool purchases. Adjusting which nodes are prioritized (and when) can reduce CAPEX and raise overall profit.

3. Variability & Risk Modeling (Question 2)
Random Processing Times (RPT):

Real-world semiconductor production is subject to variability from temperature changes, raw material quality, machine calibration, etc.

Instead of using a single static estimate (e.g., median time), the project applies:

Bootstrapping (resampling the dataset to capture distribution tails and outliers).

Monte Carlo simulation (10,000+ iterations) to model total processing time under different random conditions.

Failure Probability (Exceeding Available Time):

For each workstation, the simulation estimates the probability that total wafer processing exceeds available tool time for at least one week in a quarter.

Calculations show a combined 77.68% chance of at least one quarter failing to meet capacity over an 8-quarter horizon if no adjustments are made.

Impact on Profitability:

Missed production → lower GB output → reduced revenue.

Failing to meet commitments → lost sales or penalties.

Potentially higher CAPEX → purchasing more tools or overtime to reduce failure risk.

Recommended Mitigations:

Increase Tool Count where failure rates are highest (e.g., Node 1 at Workstation H).

Modify Weekly Loading Strategy to align with real-time RPT changes (dynamic allocation).

Keep Risk Threshold below 5–10%, balancing CAPEX and potential lost production.

How to Use This Project
Data Input:

Collect wafer start plans per node for each quarter.

Gather yield rates, GB per wafer, and minute load per workstation.

Obtain cost per tool and initial tool counts.

Linear Optimization (Optional):

If you wish to replicate or modify the initial wafer-loading strategy, set up a linear model (e.g., using Python pulp or similar library) with constraints: demand coverage, node capacities, yield rates, etc.

Tool Requirement & CAPEX Calculation:

Convert wafer production to total processing minutes at each workstation.

Determine whether new tools are required each quarter.

Sum CAPEX costs.

Profit & Risk Assessment:

Compute revenue = f(GB produced × margin).

Subtract CAPEX to find net profit.

Run bootstrapping/Monte Carlo on random processing times to determine the probability of exceeding available tool hours.

Evaluate the risk of shortfalls and incorporate additional buffer if needed.

Decision Making:

If the risk of failure is too high, explore scenarios:

Adding more tools for bottleneck workstations.

Changing node allocations or staggering wafer starts over the quarter.

Weigh the extra CAPEX against potential lost revenue.

Project Benefits
Demonstrates end-to-end analysis: from setting wafer starts and yield rates, to counting tools, to forecasting profit and risk.

Offers a scalable framework for real-world semiconductor planning under uncertainty.

Balances quantitative optimization with statistical modeling to capture realistic variability.

Prerequisites & Tools
Python (for linear optimization, data processing, bootstrapping, Monte Carlo simulation).

Pandas or similar libraries for data manipulation.

Matplotlib for plotting distributions or simulation outcomes (optional but recommended).

Basic understanding of operations research and statistics (especially distribution fitting).

Future Extensions
Integrate dynamic scheduling that adjusts wafer starts on a rolling weekly basis, reacting to real-time yield and RPT changes.

Expand the cost model to include operational expenses (OPEX), such as energy usage or labor for extended operating hours.

Incorporate financial discount rates or net present value (NPV) for multi-year CAPEX comparisons.

License
This project was originally developed for an academic competition. Any applicable licenses or reuse permissions depend on the competition’s guidelines and the sponsoring institution’s policies.
