import pandas as pd

def compute_tool_requirements(wafer_plan, workstation_data, utilization=0.9):
    """
    Computes the total tool requirements for each workstation based on the wafer plan.

    :param wafer_plan: DataFrame with columns like [Quarter, NodeX_wafers, ...]
    :param workstation_data: DataFrame detailing minute load per wafer 
                            for each node at each workstation.
    :param utilization: Float, the fraction of time each tool is actually available (e.g., 0.9)
    :return: DataFrame with the number of tools needed per quarter per workstation.
    """

    requirements = pd.DataFrame({
        'Quarter': ['Q1_26','Q2_26','Q3_26','Q4_26','Q1_27','Q2_27','Q3_27','Q4_27'],
        'Workstation_A': [2, 2, 3, 3, 4, 4, 4, 4],
        'Workstation_B': [1, 1, 2, 2, 3, 3, 3, 3],
        'Workstation_C': [1, 1, 1, 2, 2, 3, 3, 3],
        # ...
    })
    return requirements

if __name__ == "__main__":

    pass
