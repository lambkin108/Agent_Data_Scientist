import asyncio
import sys

from metagpt.roles.di.data_interpreter import DataInterpreter


async def main(requirement: str = ""):
    di = DataInterpreter()
    await di.run(requirement)


if __name__ == "__main__":
    # Default requirement if none is provided
    default_requirement = "Solve this math problem: The greatest common divisor of positive integers m and n is 6. The least common multiple of m and n is 126. What is the least possible value of m + n?"
    
    # Get requirement from command line arguments
    if len(sys.argv) > 1:
        # Join all arguments after the script name to form the requirement
        requirement = " ".join(sys.argv[1:])
    else:
        requirement = default_requirement
        print(f"No requirement provided. Using default: {default_requirement}")
    
    # Run the data interpreter with the requirement
    asyncio.run(main(requirement))