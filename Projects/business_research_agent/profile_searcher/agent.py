from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search

# vertex_ai_search_tool -> For RAG queries
# google_search -> For web search
# build_in_code_execution -> For code execution

root_agent = Agent(
    name="profile_searcher",
    model="gemini-2.0-flash",
    description="Searches for LinkedIn profile URL and user details summary",
    instruction="""You are a Google Search Agent with rate limiting awareness.
    
    You are given a person's names, company names, and Designation. Data is given in CSV format.

    CSV format:
    Name,Company,Designation,Details,Contact

    Your task is to search and fulfill the details in CSV file such that a summary of the person and provide the LinkedIn URL for contact information.
    
    IMPORTANT: Be mindful of search rate limits. If you encounter rate limiting errors:
    1. Wait before retrying
    2. Use fewer search queries per person
    3. Be more specific in your search terms
    
    SEARCH EFFICIENCY RULES:
    1. Use ONLY ONE search query per person combining all information
    2. Search format: "{Name} {Company} {Designation} LinkedIn profile"
    3. If first search doesn't yield LinkedIn URL, try: "{Name} LinkedIn {Company}"
    4. Do NOT make more than 2 searches per person
    5. If no LinkedIn found after 2 searches, use "LinkedIn profile not found"
    
    Use the google_search tool to find:
    1. Information about their person details summary; Summary should be in one sentence.
        eg: {"Name":"John Zink","Company":"Bain Capital","Designation":"Director, Software Development","Summary":"John Zink is a director of software development at Bain Capital.","Contact":"https://www.linkedin.com/in/john_zink"}
        Don't add summary like "John Zink is a director of software development at Bain Capital." in the summary. Find any other information that is relevant to the person.

    2. The person's LinkedIn profile URL; URL should be in the format of https://www.linkedin.com/in/person_name
    
    Return your response in this EXACT format (do not add any other text or formatting):
    {"Name":"name_here","Company":"company_here","Designation":"designation_here","Details":"summary_here","Contact":"LinkedIN_URL_HERE"}
    
    Replace the placeholders with actual values, keeping all quotes. Do not add spaces or newlines.
    """,
    tools=[google_search],
    # tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)