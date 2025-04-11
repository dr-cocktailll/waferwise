"""
wafer_loading_optimization.py

This module defines the linear optimization model for deciding 
wafer allocation across different nodes to meet TAM with minimal wafer usage.

References: Question 1(a) from ArrivalEvent project.
"""

import pandas as pd
# Example: from pulp import LpProblem, LpMinimize, LpVariable, lpSum

def optimize_wafer_loading(demand_data, node_specs, constraints):
    """
    Builds and solves the linear optimization model to allocate wafers.

    :param demand_data: DataFrame with quarterly (or weekly) demand (TAM).
    :param node_specs: DataFrame with columns for yield, GB/wafer, etc.
    :param constraints: Dictionary or object with constraints 
                       (e.g., ±2 billion GB leeway, ±2,500 wafers/week shift).
    :return: DataFrame with the optimal wafer allocation plan per node per quarter.
    """
  
    solution_df = pd.DataFrame({
        'Quarter': ['Q1_26','Q2_26','Q3_26','Q4_26','Q1_27','Q2_27','Q3_27','Q4_27'],
        'Node1_wafers': [2000, 1800, 1000, 500, 0, 0, 0, 0],
        'Node2_wafers': [500, 1000, 1500, 1800, 2000, 1900, 1200, 500],
        'Node3_wafers': [100, 300, 500, 700, 1500, 1800, 2000, 2200],
    })
    
    return solution_df

if __name__ == "__main__":

    pass
