"""
Research Agent Pipeline

This example demonstrates a research pipeline that gathers information about a person
using Google search and LinkedIn data, then generates a comprehensive report.
"""

import os
from google.adk.agents import SequentialAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Google API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

# Import the subagents
from .subagents.google_search import google_search_agent
from .subagents.linkedin_scraper import linkedin_agent

# Create the sequential agent
root_agent = SequentialAgent(
    name="ResearchPipeline",
    sub_agents=[google_search_agent, linkedin_agent],
    description="A pipeline that gathers information about a person using Google search and LinkedIn data"
) 