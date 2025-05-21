import asyncio
import sys
from metagpt.logs import logger
from metagpt.roles.di.data_interpreter import DataInterpreter
from metagpt.utils.recovery_util import save_history


async def main(requirement: str = ""):
    di = DataInterpreter()
    rsp = await di.run(requirement)
    logger.info(rsp)
    save_history(role=di)

if __name__ == "__main__":
    # Default requirement if none is provided
    default_requirement = "Run data analysis on sklearn Iris dataset, include a plot"
    
    # Get requirement from command line arguments
    if len(sys.argv) > 1:
        # Join all arguments after the script name to form the requirement
        requirement = " ".join(sys.argv[1:])
    else:
        requirement = default_requirement
        print(f"No requirement provided. Using default: {default_requirement}")
    
    # Run the data interpreter with the requirement
    asyncio.run(main(requirement))