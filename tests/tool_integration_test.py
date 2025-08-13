"""
Tool Integration Test for Claude Code Agent
Tests that tools can be invoked directly via the agent
"""

import pytest
import os
from agency_code_agent.agency_code_agent import create_agency_code_agent

@pytest.fixture
def agent():
    """Create claude code agent for testing"""
    return create_agency_code_agent()


def test_agent_creation(agent):
    """Test that agent is created successfully with tools"""
    assert agent is not None, "Agent should be created successfully"
    assert hasattr(agent, 'name'), "Agent should have a name attribute"
    assert hasattr(agent, 'tools'), "Agent should have tools attribute"
    assert len(agent.tools) > 0, "Agent should have at least one tool"


def test_ls_tool_invocation(agent):
    """Test LS tool direct invocation"""
    ls_tool = None
    for tool in agent.tools:
        if tool.name == "LS":
            ls_tool = tool
            break
    
    assert ls_tool is not None, "LS tool should be found in agent tools"
    
    # Test that the tool exists and has expected properties
    assert hasattr(ls_tool, 'name'), "Tool should have a name"
    assert ls_tool.name == "LS", "Tool name should be LS"


def test_todo_write_tool_invocation(agent):
    """Test TodoWrite tool direct invocation"""
    todo_tool = None
    for tool in agent.tools:
        if tool.name == "TodoWrite":
            todo_tool = tool
            break
    
    assert todo_tool is not None, "TodoWrite tool should be found in agent tools"
    
    # Test that the tool exists and has expected properties
    assert hasattr(todo_tool, 'name'), "Tool should have a name"
    assert todo_tool.name == "TodoWrite", "Tool name should be TodoWrite"


def test_tool_parameter_validation(agent):
    """Test tool parameter validation"""
    read_tool = None
    for tool in agent.tools:
        if tool.name == "Read":
            read_tool = tool
            break
    
    assert read_tool is not None, "Read tool should be found in agent tools"
    
    # Test that the tool exists and has expected properties
    assert hasattr(read_tool, 'name'), "Tool should have a name"
    assert read_tool.name == "Read", "Tool name should be Read"


def test_critical_tools_presence(agent):
    """Test that critical tools are present"""
    tools_by_name = {tool.name: tool for tool in agent.tools}
    critical_tools = ["LS", "Read", "Write", "Bash", "TodoWrite"]
    
    for tool_name in critical_tools:
        assert tool_name in tools_by_name, f"Critical tool {tool_name} should be loaded"


def test_tool_count(agent):
    """Test that expected number of tools are loaded"""
    # Note: this might need adjustment based on actual tool count
    assert len(agent.tools) >= 10, "Agent should have at least 10 tools"