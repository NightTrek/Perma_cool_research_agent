from crewai import Crew
from agents.customer_research_agent import get_customer_research_agent
from research_licence import create_customer_profile_task
from cool_types import Type6LicenceHolder

import csv


data = []
# Open the CSV file
with open('./data/mini-type6.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Initialize an empty list to store the CSV data

    # Iterate over each row in the CSV file
    for row in csv_reader:
        licence = Type6LicenceHolder(
            licenseNumber=row[1],
            licenseStatus=row[2],
            licenseDesignation=row[5],
            issueDate=row[6],
            expirationDate=row[7],
            licenseStatusDate=row[8],
            businessLegalName=row[9],
            businessDbaName=row[10],
            businessOwnerName=row[11],
            premiseStreetAddress=row[14],
            premiseCity=row[15],
            premiseState=row[16],
            premiseCounty=row[17],
            premiseZipCode=row[18],
            businessEmail=row[19],
            businessPhone=row[20]
        )
        data.append(licence)

research_agent = get_customer_research_agent(verbose=True)

SingleLicenceTask = create_customer_profile_task(data[1])

