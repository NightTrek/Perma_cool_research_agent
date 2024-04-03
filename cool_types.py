from typing import List

from pydantic import BaseModel


class Type6LicenceHolder(BaseModel):
    licenseNumber: str
    licenseStatus: str 
    licenseDesignation: str
    issueDate: str
    expirationDate: str  
    licenseStatusDate: str | None 
    businessLegalName: str | None 
    businessDbaName: str | None 
    businessOwnerName: str | None 
    premiseStreetAddress: str | None 
    premiseCity: str | None 
    premiseState: str | None 
    premiseCounty: str | None 
    premiseZipCode: str | None
    businessEmail: str | None 
    businessPhone: str | None

    # class Config:
    #     arbitrary_types_allowed = True

    def to_str(self):
        return "License Number: " + self.licenseNumber + "\nLicense Status: " + self.licenseStatus + "\nLicense Designation: " + self.licenseDesignation + "\nIssue Date: " + self.issueDate + "\nExpiration Date: " + self.expirationDate + "\nLicense Status Date: " + str(self.licenseStatusDate) + "\nBusiness Legal Name: " + str(self.businessLegalName) + "\nBusiness DBA Name: " + str(self.businessDbaName) + "\nBusiness Owner Name: " + str(self.businessOwnerName) + "\nPremise Street Address: " + str(self.premiseStreetAddress) + "\nPremise City: " + str(self.premiseCity) + "\nPremise State: " + str(self.premiseState) + "\nPremise County: " + str(self.premiseCounty) + "\nPremise Zip Code: " + str(self.premiseZipCode) + "\nBusiness Email: " + str(self.businessEmail) + "\nBusiness Phone: " + str(self.businessPhone)


class Evidence(BaseModel):
    type_of_evidence: str
    evidence_for_field: str
    evidence_for_value: str
    url: str

class Product(BaseModel):
     name: str
     description: str


class Customer(BaseModel):
    firstName: str
    lastName: str
    email: str = None
    linkdin: str = None
    customerNote: str
    title: str = None
    # company info repeated
    website: str
    companyName: str
    companySummary: str 
    products: List[Product]
    evidence: List[Evidence] = []

class simple_customer(BaseModel):
    firstName: str
    lastName: str
    email: str = None
    linkdin: str = None
    customerNote: str
    title: str = None
    


class Company_Website(BaseModel):
    url: str
    contactPage_url: str
    summary: str
    infomration_about_the_team: str
    evidence: List[Evidence] = []

class Company(BaseModel):
     buisnessName: str
     licenseNumber: str
     licenseEmail: str
     executives: List[simple_customer]
     products: List[str]
     website_info: Company_Website
     evidence: List[Evidence] = []
