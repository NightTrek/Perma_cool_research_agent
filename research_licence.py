from crewai import Task, Crew
from agents.customer_research_agent import get_customer_research_agent
from cool_types import Type6LicenceHolder, Company

def create_customer_profile_task(licence: Type6LicenceHolder):
    return Task(
        description=f"""
        Given a customer profile research the customer to determin their companies products. 
        Identify a list of products they sell if possible.
        Identify and esitmate a company revenue size
        identify a list of company executives and decision makers
        Read the linkdin profile for the executives to try and find contact information.
        identify emails for each of the executives and decision makers. Make sure not to repeat the same email twice. Make sure the email is only included if its the email address of the specific executive being profiles.

        Customer profile: 
            - licenseNumber = {licence.licenseNumber}
            - licenseStatus = {licence.licenseStatus}
            - licenseDesignation = {licence.licenseDesignation}
            - issueDate = {licence.issueDate}
            - expirationDate = {licence.expirationDate}
            - licenseStatusDate = {licence.licenseStatusDate}
            - businessLegalName = {licence.businessLegalName}
            - businessDbaName = {licence.businessDbaName}
            - businessOwnerName = {licence.businessOwnerName}
            - premiseStreetAddress = {licence.premiseStreetAddress}
            - premiseCity = {licence.premiseCity}
            - premiseState = {licence.premiseState}
            - premiseCounty = {licence.premiseCounty}
            - premiseZipCode = {licence.premiseZipCode}
            - businessEmail = {licence.businessEmail}
            - businessPhone = {licence.businessPhone}
        """,
        expected_output="""A customer profile JSON including the following fields.
          Output the response in json acording the following format:
        {
            "buisnessName": "{businessLegalName}",
            "licenseNumber": "{licenseNumber}",
            "licenseEmail": "{businessEmail}",
            "products": [],
            "company_website":{
                "url": str (required),
                "contactPage_url": str (required),
                "summary": str (required),
                "infomration_about_the_team": str (required)
            }
            "executives": [
                {
                    "name": str (required),
                    "executiveEmail": str (required),
                    "linkedin_url": str (required),
                    "position_at_company": str (required),
                    "customer_note": str (required),
                    "evidence": [
                        {
                            "type": str (required),
                            "value": str (required),
                            "url": str (required),
                        }
                    ] (required),
                }
            ]
        }""",
        output_json=Company,
        output_file=f"./output_research/{licence.businessLegalName}_profile.json",
        agent=get_customer_research_agent(verbose=True),
        # async_execution=True, # only enable this for openRouter based processing
    )


def run_licence_crew(licences: list[Type6LicenceHolder]):
    
    tasks = []
    for key in licences:
        tasks.append(create_customer_profile_task(key))


    crew = Crew(
        agents=[get_customer_research_agent(verbose=True)],
        tasks=tasks,
        verbose=2,
    )
    crew.kickoff()