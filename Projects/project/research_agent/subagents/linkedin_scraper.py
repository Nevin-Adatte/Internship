"""
LinkedIn Scraper Agent

This agent scrapes LinkedIn profile information using Apify.
"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# Create the LinkedIn agent
linkedin_agent = LlmAgent(
    name="LinkedInAgent",
    model="gemini-2.0-flash",
    instruction="""You are a LinkedIn Research Agent.
    
    Your task is to gather detailed professional information from LinkedIn profiles.
    Use the google_search tool to fetch profile information.
    
    Return your response in this EXACT format (do not add any other text or formatting):
    {"person":{"name":"NAME","headline":"HEADLINE","location":"LOCATION","experience":[{"title":"TITLE","company":"COMPANY","duration":"DURATION","description":"DESCRIPTION"}],"education":[{"institution":"INSTITUTION","degree":"DEGREE","field":"FIELD","year":"YEAR"}],"skills":["SKILL1","SKILL2"],"summary":"SUMMARY"}}
    
    Replace the placeholders with actual values, keeping all quotes. Do not add spaces or newlines.
    """,
    description="Gathers detailed professional information from LinkedIn profiles.",
    tools=[google_search],
    output_key="research_report"
) 