"""
Google Search Agent

This agent searches for a person's LinkedIn profile URL and company information.
"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# Create the Google search agent
google_search_agent = LlmAgent(
    name="GoogleSearchAgent",
    model="gemini-2.0-flash",
    instruction="""You are a Google Search Agent.
    
    Your task is to search for information about a person and their company.
    Use the google_search tool to find:
    1. The person's LinkedIn profile URL
    2. Information about their company
    
    Return your response in this EXACT format (do not add any other text or formatting):
    {"linkedin_url":"URL_HERE","company_info":{"name":"COMPANY_NAME","industry":"INDUSTRY","size":"SIZE","location":"LOCATION","description":"DESCRIPTION"}}
    
    Replace the placeholders with actual values, keeping all quotes. Do not add spaces or newlines.
    """,
    description="Searches for LinkedIn profile URL and company information.",
    tools=[google_search],
    output_key="search_results"
) 