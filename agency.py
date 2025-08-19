from agency_swarm import Agency
from agency_code_agent.agency_code_agent import create_agency_code_agent
from planner_agent.planner_agent import create_planner_agent
import os
import platform
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir, "agency_code_agent", "instructions.md"), "r") as f:
    instructions = f.read()
    instructions = instructions.format(
        cwd=os.getcwd(),
        is_git_repo=os.path.isdir(".git"),
        platform=platform.system(),
        os_version=platform.release(),
        today=datetime.now().strftime("%Y-%m-%d")
    )

# Create agents
planner = create_planner_agent()
coder = create_agency_code_agent(model="anthropic/claude-sonnet-4-20250514")

# Set up mutual handoffs after both agents are created
planner.handoffs = [coder]
coder.handoffs = [planner]

agency = Agency(
    coder,
    shared_instructions=instructions,
)

if __name__ == "__main__":
    agency.terminal_demo()