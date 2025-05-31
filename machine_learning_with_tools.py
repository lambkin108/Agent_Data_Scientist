import sys
import asyncio

from metagpt.roles.di.data_interpreter import DataInterpreter


async def main(requirement: str):
    role = DataInterpreter(use_reflection=True, tools=["<all>"])
    await role.run(requirement)


if __name__ == "__main__":
    data_path = "your/path/to/titanic"
    train_path = f"{data_path}/split_train.csv"
    eval_path = f"{data_path}/split_eval.csv"
    default_requirement = f"This is a titanic passenger survival dataset, your goal is to predict passenger survival outcome. The target column is Survived. Perform data analysis, data preprocessing, feature engineering, and modeling to predict the target. Report accuracy on the eval data. Train data path: '{train_path}', eval data path: '{eval_path}'."
    
    # Get requirement from command line arguments
    if len(sys.argv) > 1:
        # Join all arguments after the script name to form the requirement
        requirement = " ".join(sys.argv[1:])
    else:
        requirement = default_requirement
        print(f"No requirement provided. Using default: {default_requirement}")
    
    asyncio.run(main(requirement))