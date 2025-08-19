from agency_swarm import Agent
import os
from agents import ModelSettings
from agents.extensions.models.litellm_model import LitellmModel
from openai.types.shared import Reasoning

# Get the absolute path to the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

def create_planner_agent(model: str = "openai/gpt-5", reasoning_effort: str = "high") -> Agent:
    """Factory that returns a fresh PlannerAgent instance.
    Use this in tests to avoid reusing a singleton across multiple agencies.
    """
    return Agent(
        name="PlannerAgent",
        description=(
            "A strategic planning and task breakdown specialist that helps organize "
            "and structure software development projects into manageable, actionable tasks. "
            "Provides clear project roadmaps and coordinates with the AgencyCodeAgent for execution."
        ),
        instructions="hello this is a test",
        tools_folder=os.path.join(current_dir, "tools"),
        model=LitellmModel(model=model),
        model_settings=ModelSettings(
            reasoning=Reasoning(effort=reasoning_effort) if "o3" in model else None
        )
    )

# Note: We don't create a singleton at module level to avoid circular imports.
# Use create_planner_agent() directly or import and call when needed.
