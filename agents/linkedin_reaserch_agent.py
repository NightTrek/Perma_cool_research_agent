from crewai import Agent
import sys
sys.path.append("..")
from tools.linkedin_search import LinkedinAccountDetailsTool, LinkedinAccountSearch

account_search = LinkedinAccountSearch()
account_details_scraper = LinkedinAccountDetailsTool()

def get_linkedin_research_agent(verbose=False):
    return Agent(
        role="Linkdin researcher",
        goal="Identify the customer Linkein profiles and extract relevant information",
        backstory="""
        You are an expert linkedin researcher with experience identifying profiles and extracting relevant information.
        You are an expert sales analyst with experience developing in depth customer profiles.
        You are great at identifying information about customers including their role at their company and personal background.
        You like using google to try and build as complete of a customer profile as possible.
        When you dont find information you dont assume it doesnt exist. You like to limit your assumptions to make sure you are not mislead. If you dont have direct evidence of something you dont include it in your customer profile.
        You also do a great job filtering out information about people with the same name that dont fit the customers profile.
        You are an expert in looking at cannabis licence holder and figuring out everyone who has decision making power the the company and any contact information.
        """,
        tools=[account_search, account_details_scraper],
        verbose=verbose,
    )



# automted reference finder
# automated news finding 
# citations using local retreival 
# effective Agent memory tools
