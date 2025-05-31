import sys
import asyncio

from metagpt.roles.di.data_interpreter import DataInterpreter


async def main(requirement: str, react_mode: str = 'plan_and_act'):
    role = DataInterpreter(use_reflection=True, tools=["<all>"], react_mode=react_mode)
    await role.run(requirement)


if __name__ == "__main__":
    data_path = "your/path/to/titanic"
    train_path = f"{data_path}/split_train.csv"
    eval_path = f"{data_path}/split_eval.csv"
    default_requirement = f"This is a titanic passenger survival dataset, your goal is to predict passenger survival outcome. The target column is Survived. Perform data analysis, data preprocessing, feature engineering, and modeling to predict the target. Report accuracy on the eval data. Train data path: '{train_path}', eval data path: '{eval_path}'."
    default_react_mode = 'plan_and_act'
    
    # Get requirement from command line arguments
    requirement = sys.argv[1] if len(sys.argv) > 1 else default_requirement
    react_mode = sys.argv[2] if len(sys.argv) > 2 else default_react_mode
    
    # 只在使用默认值时提示
    if len(sys.argv) <= 1:
        print(f"No requirement provided. Using default: {default_requirement}")
 
    asyncio.run(main(requirement, react_mode))