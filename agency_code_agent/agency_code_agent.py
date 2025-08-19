from agency_swarm import Agent
import os
from agents import WebSearchTool, ModelSettings
from agents import set_tracing_disabled
from openai.types.shared.reasoning import Reasoning
from agents.extensions.models.litellm_model import LitellmModel

from dotenv import load_dotenv
load_dotenv()

# Get the absolute path to the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
set_tracing_disabled(disabled=True)


def create_agency_code_agent(model: str = "gpt-5", reasoning_effort: str = "high") -> Agent:
    """Factory that returns a fresh AgencyCodeAgent instance.
    Use this in tests to avoid reusing a singleton across multiple agencies.
    """
    is_openai = "gpt" in model
    is_claude = "claude" in model
    is_grok = "grok" in model

    return Agent(
        name="AgencyCodeAgent",
        description=(
            "An interactive CLI tool that helps users with software engineering tasks. "
            "Assists with defensive security tasks only. Provides concise, direct, "
            "and to-the-point responses for command line interface interactions."
        ),
        # instructions are in shared_instructions.md for agency
        instructions=None,
        tools_folder=os.path.join(current_dir, "tools"),
        model=model if is_openai else LitellmModel(model=model),
        # only works with openai models
        tools=[WebSearchTool()] if is_openai else [],
        model_settings=ModelSettings(
            reasoning=Reasoning(effort="high") if is_openai else None,
            truncation="auto",
            extra_body={"web_search_options": {"search_context_size": "medium"}}
            if is_claude
            else {"search_parameters": {"mode": "on", "returnCitations": True}}
            if is_grok
            else None,
        )         
    )

# Note: We don't create a singleton at module level to avoid circular imports.
# Use create_agency_code_agent() directly or import and call when needed.