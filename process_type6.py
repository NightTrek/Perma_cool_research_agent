from cool_types import Type6LicenceHolder
from research_licence import run_licence_crew
from init import init
import csv

init()
# Open the CSV file
# with open('./data/uls-export-03-26-2024.csv', 'r') as csv_file:
with open('./data/uls-export-03-26-2024.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Initialize an empty list to store the CSV data
    data = []
    valueCountMap = {}
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append the row to the data list
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
            #  )
        data.append(licence)
        # if "@" in licence.businessEmail and "." in licence.businessEmail: 
        #     valueCountMap["email"] += 1
        for field in licence.__dict__:
            if field not in valueCountMap:
                valueCountMap[field] = 0
            if getattr(licence, field) not in ["Data Not Available", "Not Published"]:
                valueCountMap[field] += 1
    print(data[0].to_str())
    print(f"Total intries procesed {len(data)}")
    for key in valueCountMap:
        print(f"We have {valueCountMap[key]} of {key}")

                  
    run_licence_crew(data[18:])