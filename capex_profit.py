"""
capex_and_profit.py

Calculates CAPEX when additional tools are required and 
derives net profit based on wafer output revenue.

References: Question 1(b), 1(c) from ArrivalEvent project.
"""

import pandas as pd
import math

def calculate_capex(tool_req, tool_costs, initial_tools):
    """
    Determines additional tools needed each quarter and calculates CAPEX.

    :param tool_req: DataFrame with columns [Quarter, Workstation_X, ...] tool requirements
    :param tool_costs: dict or DataFrame with cost per tool type
    :param initial_tools: dict or DataFrame with how many tools are available at start
    :return: DataFrame with total new tools and CAPEX per quarter.
    """
    
    capex_data = []
    cumulative_tools = initial_tools.copy()  # track running total

    for idx, row in tool_req.iterrows():
        quarter = row['Quarter']
        total_capex = 0.0

        # example, iterate through columns with tool requirements
        new_tools_dict = {}
        for workstation in row.index.drop('Quarter'):
            needed = row[workstation]
            have = cumulative_tools.get(workstation, 0)
            if needed > have:
                # purchase shortfall
                diff = needed - have
                cost = tool_costs.get(workstation, 0) * diff
                total_capex += cost

                # update tool count
                cumulative_tools[workstation] = have + diff
                new_tools_dict[workstation] = diff
            else:
                new_tools_dict[workstation] = 0
        
        capex_data.append({
            'Quarter': quarter,
            'NewTools': new_tools_dict, 
            'Quarterly_CAPEX': total_capex
        })
    
    return pd.DataFrame(capex_data)

def calculate_revenue_and_profit(wafer_plan, node_specs, capex_df, margin_per_gb):
    """
    Calculates the total revenue (based on wafer outputs and yields)
    and then net profit by subtracting quarterly CAPEX.

    :param wafer_plan: DataFrame with [Quarter, NodeX_wafers, ...]
    :param node_specs: DataFrame with columns [Node, GB_per_wafer, Yield_by_quarter, ...]
    :param capex_df: CAPEX results from calculate_capex()
    :param margin_per_gb: float representing contribution margin per GB
    :return: DataFrame with columns [Quarter, Revenue, CAPEX, Net_Profit]
    """

    results = []
    for idx, row in wafer_plan.iterrows():
        quarter = row['Quarter']
        
        # Example: summing production across Node1_wafers, Node2_wafers, etc.
        total_gb = 0
        for col in row.index.drop('Quarter'):
            # parse node name
            node_name = col.split('_')[0]  # "Node1" from "Node1_wafers"
            wafers = row[col]
            
            # get capacity & yield for this node & quarter from node_specs
            # for demo, assume fixed yield & GB
            gb_per_wafer = 100000  # stub
            yield_rate = 0.95      # stub
            production_gb = wafers * gb_per_wafer * yield_rate
            
            total_gb += production_gb
        
        revenue = total_gb * margin_per_gb
        
        # find matching CAPEX in capex_df
        quarter_capex = capex_df.loc[capex_df['Quarter'] == quarter, 'Quarterly_CAPEX']
        if not quarter_capex.empty:
            capex_val = quarter_capex.values[0]
        else:
            capex_val = 0
        
        net_profit = revenue - capex_val
        results.append({
            'Quarter': quarter,
            'Revenue': revenue,
            'CAPEX': capex_val,
            'Net_Profit': net_profit
        })
    
    return pd.DataFrame(results)

if __name__ == "__main__":

    pass
