import asyncio
import sys
from metagpt.logs import logger
from metagpt.roles.di.data_interpreter import DataInterpreter
from metagpt.utils.recovery_util import save_history


async def main(requirement: str = "", react_mode: str = 'plan_and_act'):
    di = DataInterpreter(react_mode=react_mode)
    rsp = await di.run(requirement)
    logger.info(rsp)
    save_history(role=di)

if __name__ == "__main__":
    # Default requirement if none is provided
    default_requirement = "Run data analysis on sklearn Iris dataset, include a plot"
    default_react_mode = 'plan_and_act'

    # Get requirement from command line arguments
    requirement = sys.argv[1] if len(sys.argv) > 1 else default_requirement
    react_mode = sys.argv[2] if len(sys.argv) > 2 else default_react_mode
    
    # 只在使用默认值时提示
    if len(sys.argv) <= 1:
        print(f"No requirement provided. Using default: {default_requirement}")
    
    # Run the data interpreter with the requirement
    asyncio.run(main(requirement, react_mode))