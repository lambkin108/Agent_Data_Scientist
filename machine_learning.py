#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import fire
import os
from typing import Optional, Dict, Any

from metagpt.roles.di.data_interpreter import DataInterpreter


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
    default_requirement = "Run data analysis on sklearn Wine recognition dataset, include a plot, and train a model to predict wine class (20% as validation), and show validation accuracy. And summarize your result."
    default_react_mode = 'plan_and_act'
    
    # Get requirement from command line arguments
    requirement = sys.argv[1] if len(sys.argv) > 1 else default_requirement
    react_mode = sys.argv[2] if len(sys.argv) > 2 else default_react_mode
    
    # 只在使用默认值时提示
    if len(sys.argv) <= 1:
        print(f"No requirement provided. Using default: {default_requirement}")

    mi = DataInterpreter(react_mode=react_mode)
    await mi.run(requirement)


if __name__ == "__main__":
    fire.Fire(run_analysis)