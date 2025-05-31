#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fire
import os
from typing import Optional, Dict, Any

from metagpt.roles.di.data_interpreter import DataInterpreter

# Template requirements
TEMPLATE_REQS = "Run data analysis on sklearn Wine recognition dataset, include a plot, and train a model to predict wine class (20% as validation), and show validation accuracy."


async def run_analysis(
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
    
    # Generate requirement from template
    if custom_requirement:
        requirement = custom_requirement
    else:
        requirement = TEMPLATE_REQS
    
    # Display configuration if requested
    if show_config:
        print("\nGenerated Requirement:")
        print(requirement)
        return
    
    # Run the DataInterpreter
    mi = DataInterpreter()
    await mi.run(requirement)


if __name__ == "__main__":
    fire.Fire(run_analysis)