#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fire
import os
from typing import Optional, Dict, Any

from metagpt.roles.di.data_interpreter import DataInterpreter

# Default configurations
DEFAULT_CONFIG = {
    "wine": {
        "dataset": "sklearn_wine",
        "validation_split": 0.2,
        "description": "Wine recognition dataset analysis with classification model"
    },
    "sales_forecast": {
        "dataset": "train.csv",
        "validation_weeks": 40,
        "description": "Walmart sales forecast with WMAE metric"
    }
}

# Template requirements
TEMPLATE_REQS = {
    "wine": """Run data analysis on {dataset} dataset, include a plot, and train a model to predict 
wine class ({validation_split:.0%} as validation), and show validation accuracy.""",
    
    "sales_forecast": """Train a model to predict sales for each department in every store 
(split the last {validation_weeks} weeks records as validation dataset, the others is train dataset), 
include plot total sales trends, print metric and plot scatter plots of
ground truth and predictions on validation data. Dataset is {data_dir}/{dataset}, 
the metric is weighted mean absolute error (WMAE) for validation data. 
Notice: *print* key variables to get more information for next task step."""
}


async def run_analysis(
    use_case: str = "wine",
    data_dir: str = "path/to/your/data",
    dataset: Optional[str] = None,
    validation_split: Optional[float] = None,
    validation_weeks: Optional[int] = None,
    custom_requirement: Optional[str] = None,
    show_config: bool = False,
) -> None:
    """
    Run data analysis using MetaGPT's DataInterpreter.
    
    Args:
        use_case: Type of analysis to run ('wine' or 'sales_forecast')
        data_dir: Directory containing datasets
        dataset: Override default dataset name
        validation_split: Override default validation split ratio (for 'wine')
        validation_weeks: Override default number of validation weeks (for 'sales_forecast')
        custom_requirement: Use a completely custom requirement text instead of templates
        show_config: Just show the configuration without running analysis
    """
    # Prepare configuration
    config = DEFAULT_CONFIG.get(use_case, DEFAULT_CONFIG["wine"]).copy()
    
    # Override configuration with provided parameters
    if dataset:
        config["dataset"] = dataset
    if validation_split is not None and use_case == "wine":
        config["validation_split"] = validation_split
    if validation_weeks is not None and use_case == "sales_forecast":
        config["validation_weeks"] = validation_weeks
    
    # Generate requirement from template
    if custom_requirement:
        requirement = custom_requirement
    else:
        template = TEMPLATE_REQS.get(use_case, TEMPLATE_REQS["wine"])
        format_args = {**config, "data_dir": data_dir}
        requirement = template.format(**format_args)
    
    # Display configuration if requested
    if show_config:
        print(f"Use Case: {use_case}")
        print(f"Data Directory: {data_dir}")
        print("Configuration:")
        for k, v in config.items():
            print(f"  {k}: {v}")
        print("\nGenerated Requirement:")
        print(requirement)
        return
    
    # Run the DataInterpreter
    mi = DataInterpreter()
    await mi.run(requirement)


if __name__ == "__main__":
    fire.Fire(run_analysis)